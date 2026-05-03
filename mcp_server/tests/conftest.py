"""Shared test fixtures.

The tests run against the real bundled ``data/`` folder. We assume
``scripts/sync_references.py`` has been run at least once; otherwise the
fixture below will populate it on the fly so ``pytest`` works in a fresh
checkout.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(__file__).resolve().parents[1] / "src" / "cloud_finops_mcp" / "data"
SOURCE_DIR = REPO_ROOT / "cloud-finops" / "references"


def _ensure_data() -> None:
    if any(DATA_DIR.glob("*.md")):
        return
    if not SOURCE_DIR.is_dir():
        pytest.skip(f"reference source missing at {SOURCE_DIR}")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for src in SOURCE_DIR.glob("*.md"):
        shutil.copy2(src, DATA_DIR / src.name)


@pytest.fixture(autouse=True, scope="session")
def _populate_data() -> None:
    _ensure_data()
    # Ensure a fresh import picks up data/ — important when the tree was
    # populated mid-session.
    sys.modules.pop("cloud_finops_mcp.metadata", None)
