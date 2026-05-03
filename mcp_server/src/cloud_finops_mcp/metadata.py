"""Reference-file index built from FCP frontmatter.

Walks the bundled ``data/`` directory at startup, parses YAML frontmatter from
each ``.md`` file, and builds an in-memory index used by the tool surfaces.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).resolve().parent / "data"

# FCP fields we expose. Anything not listed here is ignored by the index.
FCP_SCALAR_FIELDS = (
    "fcp_domain",
    "fcp_capability",
    "fcp_maturity_entry",
)
FCP_LIST_FIELDS = (
    "fcp_capabilities_secondary",
    "fcp_phases",
    "fcp_personas_primary",
    "fcp_personas_collaborating",
)


@dataclass
class Reference:
    """One indexed reference file."""

    name: str
    path: Path
    description: str
    lines: int
    fcp_domain: str | None = None
    fcp_capability: str | None = None
    fcp_capabilities_secondary: list[str] = field(default_factory=list)
    fcp_phases: list[str] = field(default_factory=list)
    fcp_personas_primary: list[str] = field(default_factory=list)
    fcp_personas_collaborating: list[str] = field(default_factory=list)
    fcp_maturity_entry: str | None = None

    def to_dict(self) -> dict:
        """Stable JSON-friendly shape returned by the MCP tools."""
        return {
            "name": self.name,
            "description": self.description,
            "fcp_domain": self.fcp_domain,
            "fcp_capability": self.fcp_capability,
            "fcp_capabilities_secondary": self.fcp_capabilities_secondary,
            "fcp_phases": self.fcp_phases,
            "fcp_personas_primary": self.fcp_personas_primary,
            "fcp_personas_collaborating": self.fcp_personas_collaborating,
            "fcp_maturity_entry": self.fcp_maturity_entry,
            "lines": self.lines,
        }


def _split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Empty frontmatter dict if none present."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    body = parts[2].lstrip("\n")
    return fm, body


def _extract_description(fm: dict, body: str) -> str:
    """Pull a one-line description.

    Preference order: ``description`` frontmatter field → first non-blank
    blockquote line → first non-blank prose line.
    """
    if isinstance(fm.get("description"), str) and fm["description"].strip():
        return fm["description"].strip()

    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue  # skip headings, we want the explainer line
        if stripped.startswith(">"):
            return stripped.lstrip("> ").strip()
        return stripped

    return ""


def _normalize_list(value) -> list[str]:
    """Coerce frontmatter list fields into ``list[str]``; tolerate scalars."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if item is not None]
    return [str(value)]


def _parse_reference(path: Path) -> Reference:
    text = path.read_text(encoding="utf-8")
    fm, body = _split_frontmatter(text)

    name = str(fm.get("name") or path.stem)
    description = _extract_description(fm, body)
    lines = text.count("\n") + (0 if text.endswith("\n") else 1)

    return Reference(
        name=name,
        path=path,
        description=description,
        lines=lines,
        fcp_domain=fm.get("fcp_domain") if isinstance(fm.get("fcp_domain"), str) else None,
        fcp_capability=fm.get("fcp_capability") if isinstance(fm.get("fcp_capability"), str) else None,
        fcp_capabilities_secondary=_normalize_list(fm.get("fcp_capabilities_secondary")),
        fcp_phases=_normalize_list(fm.get("fcp_phases")),
        fcp_personas_primary=_normalize_list(fm.get("fcp_personas_primary")),
        fcp_personas_collaborating=_normalize_list(fm.get("fcp_personas_collaborating")),
        fcp_maturity_entry=(
            fm.get("fcp_maturity_entry") if isinstance(fm.get("fcp_maturity_entry"), str) else None
        ),
    )


@lru_cache(maxsize=1)
def get_index() -> list[Reference]:
    """Return the full index of bundled references, sorted by name."""
    if not DATA_DIR.exists():
        return []
    refs = [_parse_reference(p) for p in DATA_DIR.glob("*.md")]
    refs.sort(key=lambda r: r.name)
    return refs


def get_by_name(name: str) -> Reference | None:
    """Look up a reference by its ``name`` (frontmatter or filename stem)."""
    for ref in get_index():
        if ref.name == name:
            return ref
    return None


def reset_cache() -> None:
    """Test hook: drop the cached index so the next call rebuilds it."""
    get_index.cache_clear()
