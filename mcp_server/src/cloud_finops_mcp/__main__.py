"""Entry point: ``python -m cloud_finops_mcp`` and ``cloud-finops-mcp`` console script."""

from __future__ import annotations

import asyncio

from .server import run


def main() -> None:
    """Synchronous wrapper used by the console-script entry point."""
    asyncio.run(run())


if __name__ == "__main__":
    main()
