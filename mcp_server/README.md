# cloud-finops-mcp

MCP server exposing the [OptimNow Cloud FinOps skill](https://github.com/OptimNow/cloud-finops-skills)
(28 references) as queryable tools for any MCP-aware client (Claude Code, Cursor,
Codex CLI, Windsurf, Aider, Cline, etc.).

The skill itself ships in canonical Claude Agent-Skills format and is also installable
via the cross-tool installer (`./install.sh`) for direct context injection. This MCP
server is the **enrichment path**: instead of loading the full 28-file skill into the
prompt, the agent calls tools to discover, filter, and fetch only what it needs.

## What the server exposes

Three tools, all read-only:

| Tool | Purpose |
|---|---|
| `list_references()` | List all 28 references with their FCP metadata. |
| `get_reference(name)` | Fetch the full markdown body of one reference. |
| `find_references(domain?, capability?, phase?, persona?, maturity?)` | Faceted query over the FinOps Capability/Phase frontmatter. |

The faceted query supports any combination of:

- `domain` - FinOps Framework domain (e.g. `Optimize Usage & Cost`, `Quantify Business Value`)
- `capability` - FinOps capability (matches both primary and secondary)
- `phase` - `Inform`, `Optimize`, `Operate`
- `persona` - matches both primary and collaborating personas
- `maturity` - `Crawl`, `Walk`, `Run`

All filters AND together. String matches are case-insensitive and exact.

## Install

```bash
pip install cloud-finops-mcp
```

Or run without installing via [`uv`](https://docs.astral.sh/uv/):

```bash
uvx cloud-finops-mcp
```

## Configure your MCP client

After install, point your client at the `cloud-finops-mcp` console script.

### Claude Code

Project-level (`.mcp.json` at the repo root) or user-level (`~/.claude/mcp.json`):

```json
{
  "mcpServers": {
    "cloud-finops": {
      "command": "cloud-finops-mcp"
    }
  }
}
```

Restart Claude Code, then run `/mcp` to confirm the server is connected.

### Cursor

`~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "cloud-finops": {
      "command": "cloud-finops-mcp"
    }
  }
}
```

### Codex CLI

`~/.codex/config.toml`:

```toml
[mcp_servers.cloud-finops]
command = "cloud-finops-mcp"
```

### Windsurf

`~/.windsurf/mcp.json`:

```json
{
  "mcpServers": {
    "cloud-finops": {
      "command": "cloud-finops-mcp"
    }
  }
}
```

### Any other MCP client

The server speaks MCP over stdio. Point any compatible client at `cloud-finops-mcp`
(or `python -m cloud_finops_mcp`).

## Example tool calls

Agent prompt: *"Use the cloud-finops MCP to find references for the Optimize phase
aimed at Engineering."*

Calls `find_references(phase="Optimize", persona="Engineering")` and gets back the
filtered subset (AWS, Azure, GCP, Bedrock, Databricks, etc.) without loading the full
skill into the prompt.

Agent prompt: *"Pull the AWS reference."*

Calls `get_reference(name="finops-aws")` and gets back the full markdown body
(~300 lines) instead of the entire 28-file knowledge base.

## When to use this vs the installer

| If you... | Use |
|---|---|
| Want the skill loaded as static context for every chat | The cross-tool installer (`./install.sh`) |
| Have a big-codebase session with limited context budget | The MCP server (fetch on demand) |
| Want to filter references by FinOps domain/capability/phase/persona/maturity | The MCP server (`find_references`) |
| Use a client that doesn't support MCP | The cross-tool installer |

The two paths are complementary. You can install both.

## Development

```bash
git clone https://github.com/OptimNow/cloud-finops-skills.git
cd cloud-finops-skills/mcp_server
python scripts/sync_references.py        # populate src/cloud_finops_mcp/data/
pip install -e ".[dev]"
pytest
```

## Versioning

The PyPI package version tracks the skill release tag. Tagging `v1.13` on the
parent repo triggers both the skill release zip and a new `cloud-finops-mcp` PyPI
publish so the bundled references match what the rest of the repo ships.

## License

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) - same as the parent
skill. Credit OptimNow.
