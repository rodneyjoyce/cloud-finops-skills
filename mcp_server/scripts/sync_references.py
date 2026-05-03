#!/usr/bin/env python3
"""Copy ``cloud-finops/references/*.md`` into the bundled ``data/`` folder.

Runs automatically before each wheel build (declared in ``pyproject.toml`` as a
``hatch-build-scripts`` hook). Also intended to be run manually after
``pip install -e .`` so the editable install picks up the latest reference
content::

    python scripts/sync_references.py

The script is idempotent and clears the destination folder first to drop
references that have been removed upstream.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = REPO_ROOT / "cloud-finops" / "references"
DEST_DIR = Path(__file__).resolve().parents[1] / "src" / "cloud_finops_mcp" / "data"


def main() -> int:
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    existing = list(DEST_DIR.glob("*.md"))

    if not SOURCE_DIR.is_dir():
        # When building from a dehydrated sdist, the source folder isn't
        # available, but the sdist itself bundles the synced .md files.
        # Treat that case as a successful no-op so the wheel build hook
        # doesn't fail.
        if existing:
            print(
                f"[sync_references] Source missing; using {len(existing)} pre-bundled "
                f"reference(s) at {DEST_DIR}"
            )
            return 0
        print(
            f"[sync_references] Source directory not found and no pre-bundled "
            f"references present: {SOURCE_DIR}",
            file=sys.stderr,
        )
        return 1

    # Wipe stale .md files so deletions upstream propagate to the bundle.
    for stale in existing:
        stale.unlink()

    copied = 0
    for src in sorted(SOURCE_DIR.glob("*.md")):
        dst = DEST_DIR / src.name
        shutil.copy2(src, dst)
        copied += 1

    print(f"[sync_references] Copied {copied} reference file(s) to {DEST_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
