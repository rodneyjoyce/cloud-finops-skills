"""MCP server wiring.

Registers the three v1 tools with FastMCP and runs the stdio transport.
The actual tool logic lives in :mod:`cloud_finops_mcp.tools` so it can be
unit-tested without an MCP client.
"""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from . import __version__
from . import tools as _tools

mcp = FastMCP(
    "cloud-finops",
    instructions=(
        "Cloud FinOps reference library by OptimNow. "
        "Use list_references() to discover the 28 bundled references "
        "(grouped by FinOps Capability/Phase frontmatter), "
        "find_references(domain=, capability=, phase=, persona=, maturity=) "
        "to narrow by FCP facets, and get_reference(name=) to fetch one. "
        "Content covers AWS, Azure, GCP, AI/GenAI economics, data platforms, "
        "and cross-cutting topics (allocation, anomaly, chargeback, tagging, "
        "Kubernetes, waste-detection, GreenOps)."
    ),
)


@mcp.tool()
def list_references() -> dict[str, Any]:
    """List every bundled FinOps reference with its FCP metadata.

    Returns a dict shaped ``{"references": [...], "total": N}`` where each
    entry includes ``name``, ``description``, FCP fields (``fcp_domain``,
    ``fcp_capability``, ``fcp_phases`` etc.) and ``lines``.
    """
    return _tools.list_references()


@mcp.tool()
def get_reference(name: str) -> dict[str, Any]:
    """Fetch the full markdown content of one reference by name.

    Args:
        name: Reference name as returned by ``list_references`` (e.g.
            ``"finops-aws"``, ``"finops-genai-capacity"``,
            ``"optimnow-methodology"``).

    Returns the dict ``{"name": ..., "content": "...", "lines": N}``. On miss,
    returns ``{"error": ..., "suggestions": [...]}`` with up to three
    string-distance matches so the caller can self-correct.
    """
    return _tools.get_reference(name)


@mcp.tool()
def find_references(
    domain: str | None = None,
    capability: str | None = None,
    phase: str | None = None,
    persona: str | None = None,
    maturity: str | None = None,
) -> dict[str, Any]:
    """Filter references by FinOps Capability/Phase (FCP) frontmatter.

    All filters are optional and combine with AND semantics. String matching
    is case-insensitive and exact (not substring). Examples:

    - ``find_references(domain="Optimize Usage & Cost")``
    - ``find_references(phase="Optimize", persona="Engineering")``
    - ``find_references(capability="Rate Optimization")``
    - ``find_references(maturity="Crawl")``

    Args:
        domain: FinOps Framework domain (e.g. ``"Optimize Usage & Cost"``,
            ``"Quantify Business Value"``, ``"Manage the FinOps Practice"``).
        capability: FinOps capability (matches ``fcp_capability`` and
            ``fcp_capabilities_secondary``).
        phase: FinOps phase (``"Inform"``, ``"Optimize"``, ``"Operate"``).
        persona: Persona (matches ``fcp_personas_primary`` and
            ``fcp_personas_collaborating``).
        maturity: Entry maturity level (``"Crawl"``, ``"Walk"``, ``"Run"``).

    Returns ``{"filters": {...}, "references": [...], "total": N}``.
    """
    return _tools.find_references(
        domain=domain,
        capability=capability,
        phase=phase,
        persona=persona,
        maturity=maturity,
    )


async def run() -> None:
    """Run the MCP server over the stdio transport."""
    # FastMCP exposes both synchronous and asynchronous run helpers; we use
    # the async one so the entry point can be called from ``asyncio.run``.
    await mcp.run_stdio_async()


__all__ = ["mcp", "run", "__version__"]
