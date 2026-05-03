# CLAUDE.md

Project context for AI assistants and human contributors working on this repository.

---

## What this repo is

A structured, model-agnostic FinOps knowledge skill for AI agents. The `cloud-finops/`
folder contains reference files that give any LLM accurate Cloud FinOps expertise -
Claude, GPT, Gemini, or any MCP-compatible agent.

- **SKILL.md** - entry point for Claude Code and generic agents
- **POWER.md** - entry point for Kiro IDE (same references, different format)
- **references/** - domain-specific content files (billing mechanics, pricing, optimisation patterns)
- **INSTALLATION.md** - one cross-tool installer covering 11 tool integrations, plus
  a model-agnostic response contract (system-prompt-injection section) for non-Claude
  models

Both entry points route to the same reference files. No content is duplicated.
The response contract in INSTALLATION.md (the "API integration" section) ensures
structured, billing-grounded answers across all models, even when model defaults
differ.

---

## Repository structure

```
cloud-finops-skills/
├── CLAUDE.md              <- You are here
├── README.md              <- Public-facing documentation
├── INSTALLATION.md        <- Setup instructions (11 tool integrations) + response contract
├── LICENSE.md             <- CC BY-SA 4.0
├── install.sh             <- One-liner installer script
├── assets/                <- Screenshots for installation guide
├── cloud-finops/          <- The skill (this is what gets installed)
│   ├── SKILL.md           <- Entry point + domain router
│   ├── POWER.md           <- Kiro IDE entry point
│   └── references/        <- 28 reference files, all with YAML FCP frontmatter
│       ├── optimnow-methodology.md         <- OptimNow reasoning lens, 4 pillars
│       ├── finops-framework.md             <- FinOps Foundation framework reference
│       ├── finops-for-ai.md                <- AI cost management discipline
│       ├── finops-ai-value-management.md   <- AI Investment Council, stage gates
│       ├── finops-genai-capacity.md        <- Provisioned vs shared capacity
│       ├── finops-ai-self-hosted-vs-managed.md  <- Self-host vs managed inference
│       ├── finops-ai-dev-tools.md          <- Cursor / Claude Code / Copilot / Windsurf / Codex
│       ├── finops-anthropic.md             <- Anthropic billing
│       ├── finops-aws.md                   <- AWS FinOps + commitment portfolio
│       ├── finops-bedrock.md               <- AWS Bedrock
│       ├── finops-azure.md                 <- Azure FinOps + commitment portfolio
│       ├── finops-azure-openai.md          <- Azure OpenAI / PTUs
│       ├── finops-gcp.md                   <- GCP FinOps
│       ├── finops-vertexai.md              <- GCP Vertex AI
│       ├── finops-oci.md                   <- OCI
│       ├── finops-databricks.md            <- Databricks (DBCU, allocation)
│       ├── finops-fabric.md                <- Microsoft Fabric (F-SKU, CU)
│       ├── finops-snowflake.md             <- Snowflake
│       ├── finops-tagging.md               <- Tagging governance + MCP automation
│       ├── finops-itam.md                  <- ITAM / BYOL / marketplace
│       ├── finops-sam.md                   <- SaaS asset management
│       ├── greenops-cloud-carbon.md        <- GreenOps + cloud carbon
│       ├── finops-anomaly-management.md    <- Anomaly management (standalone Inform-phase)
│       ├── finops-allocation-showback.md   <- Allocation methodology + showback
│       ├── finops-chargeback.md            <- Chargeback + Finance/accounting prerequisites
│       ├── finops-onboarding-workloads.md  <- Migration-time cost hygiene + M&A
│       ├── finops-kubernetes.md            <- K8s cross-cluster discipline (EKS/GKE/AKS)
│       └── finops-waste-detection-playbooks.md  <- Seven-category waste taxonomy + WasteLine
└── pipeline/              <- Content update pipeline (gitignored, private)
    ├── run_scan.py        <- Weekly scan entry point
    ├── run_apply.py       <- Review and apply entry point
    ├── config.yaml        <- Pipeline configuration
    ├── sources.yaml       <- 29 content sources (RSS, pricing pages, blogs)
    ├── scanner/           <- Fetcher + Sonnet-based classifier
    ├── proposer/          <- CHANGES.md report generator
    ├── applier/           <- Opus-based diff generator and file editor
    ├── alerter/           <- Gmail draft builder
    └── state/             <- Runtime state (scan results, history)
```

---

## Content update pipeline

The `pipeline/` folder contains a weekly content scanner that detects FinOps-relevant
changes across 29 sources and proposes updates to the reference files. It is gitignored
and not part of the public distribution.

The pipeline is human-in-the-loop: nothing is changed automatically. Every proposed
update goes through review (list, preview diffs, approve/reject) before touching any
reference file. See `pipeline/README.md` for the full workflow.

---

## Lessons learned

### Pipeline applier truncated 8 reference files (April-May 2026)

The bi-monthly pipeline `applier/` truncated 8 reference files across two runs:
- PR #8 (commit 647a7ef, 15 April 2026) damaged finops-azure.md (later restored
  by commit dfab33b) and introduced the trailing-`> Sources` truncation in
  finops-itam.md and finops-sam.md
- "Content update - 1 May 2026" (commit 3e64f59) made 130 insertions / 5566
  deletions across 6 files - aws, azure, gcp, framework, ai-dev-tools, for-ai -
  in what was supposed to be an additive content update

The recovery (May 2026) restored each file from a pre-truncation commit and
re-injected the few real additions identified in the diffs.

**What we learned:**
- LLM-generated diffs on long files (>1500 lines) can hallucinate truncation,
  produce diffs whose "after" state is shorter than the "before"
- A "Content update" that removes thousands of lines is a regression by
  construction, not a content choice. Aggregate stats (lines_added vs
  lines_removed) catch this faster than line-by-line review
- Without a footer-presence check, a truncated file looks valid in a `git diff`
  review (the diff stops where the file stops) - the only signal is the missing
  footer at the end
- The previous recovery (PR #8 -> commit dfab33b) fixed the symptom without
  fixing the pipeline, so the same failure mode recurred 16 days later

**Guard rails added:**
- `applier/` rejects any diff whose net change is < -20% of the file's line count
- `applier/` post-apply check requires the OptimNow footer line to be present;
  fail the commit otherwise
- `applier/` snapshots every reference file to `cloud-finops/references/.backups/`
  with a timestamp before each apply run
- The pipeline is frozen (`pipeline/run_apply.py.FROZEN`) until these guard rails
  are validated against a dry run on a sample of historical updates

**Documentation drift correction:**
The same recovery surfaced ~10 spots where doc had not kept pace with reference
growth (AGENTS.md and llms.txt listed only 17 references when 28 existed; install.sh
ChatGPT/Gemini routing missed the 6-7 newest domains; "6 setup options" appeared
in 4 files when INSTALLATION.md had moved to 11 tools). The PR-checklist in this
file now requires updating AGENTS.md, llms.txt, and the install.sh per-tool
routing whenever a reference is added.

### When in doubt, validate the baseline before comparing

When asked to compare this skill to another repo, an agent that compares against
the truncated state will conclude the other repo is more comprehensive than it
really is. Always check that key reference files end with the OptimNow footer
(and not mid-sentence) before drawing any coverage comparison.

---

## Roadmap

This section lists work that is intentionally not shipped and the trigger to revisit. It is
the durable record of "what's deliberately out of scope right now and why" - distinct from
GitHub issues, which track in-flight work.

### In-flight (write when prerequisites land)

- **WasteLine extension to Azure and GCP.** `finops-waste-detection-playbooks.md` covers the
  seven-category waste taxonomy and references the WasteLine appliance for AWS automation;
  Azure and GCP coverage currently routes to the in-cloud pattern catalogues
  (`finops-azure.md` 48-pattern, `finops-gcp.md` 26-pattern). When WasteLine ships Azure and
  GCP providers, update the operational tooling section to reflect the broader coverage and
  remove the "for Azure and GCP, see in-cloud catalogues" caveat.

### Depth passes (extend existing files when bandwidth allows)

- **Extend GreenOps depth to Azure and GCP.** The May 2026 GreenOps pass added AWS-specific
  depth to `references/greenops-cloud-carbon.md` (Sustainability Console v2 with Methodology v3
  alignment, the unused-capacity ventilation trap, critical reading of AWS sustainability claims,
  AWS region intensity anchors with the 15x gap, hardware/storage anchors, Well-Architected
  Sustainability Pillar SUS01-SUS06 with critical-read notes). The next pass should bring the
  same depth to Azure and GCP:
  - **Azure**: Emissions Impact Dashboard refresh (current methodology version, scope coverage,
    location-based vs market-based handling), Azure region intensity anchors with concrete
    numbers, Azure-specific hardware anchors (Cobalt 100, Ampere Altra, Spot equivalents), and
    Azure Well-Architected sustainability guidance critical reading.
  - **GCP**: Carbon Footprint refresh (granularity, scope coverage, location-based vs
    market-based view), GCP region intensity anchors, GCP-specific hardware anchors (Axion, Tau
    T2A, Spot/preemptible equivalents).
  - Keep the engagement-framing section vendor-agnostic - it does not need to be duplicated
    per provider. The trade-off tables, four-quadrant cost-vs-carbon framework, and CSRD
    stakeholder roles already apply across all three providers.

### Deferred reference files

These files were identified in the white-space analysis (May 2026) and explicitly deferred,
with the rationale captured here so future work picks them up at the right moment rather
than re-litigating priority. Tracking issue: `OptimNow/cloud-finops-skills#55`.

| Proposed file | Priority | Trigger to revisit | Why deferred |
|---|---|---|---|
| `finops-tools-services.md` | P2 | Next engagement raises a vendor-evaluation question | OptimNow has implicit views (FinOps Toolkit, MCP, OpenCost) but no formal write-up; better to write against a real client question than a generic checklist |
| `finops-practice-operations.md` | P2 | Next Walk to Run client engagement starts | `optimnow-methodology.md` covers the consultancy-positioning lens; this would be the operator-grade discipline below it (three-cadence operating model, per-Capability scorecard, allied-discipline integration charter) |
| `finops-forecasting.md` | P2 | Non-AI forecasting demand emerges | `finops-ai-value-management.md` covers AI forecasting; non-AI demand has not surfaced in current engagements |
| `finops-unit-economics.md` | P2 | Non-AI unit-economics demand emerges | Same reasoning as forecasting; AI-side covered by AI value management and finops-for-ai files |
| `finops-education-enablement.md` | P2 | Demand emerges; consider folding into practice-operations | Smaller scope than the other P2 files; could double as a section in practice-operations |
| `finops-benchmarking.md` | P3 | Client engagement specifically requires it | Clients rarely ask; external benchmarking has well-known data-quality issues. Could be a section in `finops-framework.md` |
| `finops-cost-warehouse.md` | P3 | Engagement requires it (e.g. Snowflake-FinOps integration) | Heavy lift, specialist content (FOCUS conformed-dim modelling, dbt + semantic layer, CUR2 / Azure Cost Mgmt / BigQuery loading patterns, late-binding analytics) |

When picking up a deferred item: read the rationale above, check the white-space analysis
context (Cletrics comparison report dated 2026-05-03 in `~/Downloads/`, plus implementation
plan in `~/.claude/plans/optimnow-cloud-finops-recommendations-followup.md`), and confirm
the trigger is real before starting the file.

### Closed gaps (May 2026 batch)

These files shipped during the white-space analysis follow-up (PRs #48, #50, #51, #52, #54,
#56) and now exist in the catalogue. Listed here for the record:

- `finops-anomaly-management.md` (PR #48) - Anomaly Management as standalone Inform capability
- `finops-allocation-showback.md` (PR #50) - Allocation methodology + showback delivery
- `finops-chargeback.md` (PR #51) - Chargeback + Finance/accounting prerequisites
- `finops-onboarding-workloads.md` (PR #52) - Migration-time cost hygiene + M&A
- `finops-kubernetes.md` (PR #54) - Cross-cluster K8s discipline (EKS/GKE/AKS)
- `finops-waste-detection-playbooks.md` (PR #56) - Seven-category waste taxonomy + WasteLine
- YAML FCP frontmatter pass across all 22 pre-existing references (PR #53)

---

## Model compatibility

The skill files are plain markdown - any LLM can read them. What differs across models
is how well they follow the structure and avoid hallucinating billing rules.

- **Claude** (Code, .ai, API) - reads SKILL.md natively, no extra configuration needed
- **Kiro IDE** - reads POWER.md natively
- **GPT, Gemini, other models** - inject the reference files as context and add the
  response contract from INSTALLATION.md (Option 6) to the system prompt

The response contract ensures consistent output structure (Context, Recommendation,
Metrics, Business impact) and prevents models from inventing pricing figures or
discount mechanics.

---

## How to add a new reference file

Follow these five steps whenever you add a new domain:

1. **Create the reference file** in `cloud-finops/references/`
   - Name it `finops-{domain}.md` (or `{category}-{domain}.md` for non-FinOps topics like `greenops-cloud-carbon.md`)
   - Follow the structure of an existing reference file as a template
   - Include practical guidance, not abstract theory
   - **Open the file with YAML FCP frontmatter** (see "Reference-file frontmatter" section below)

2. **Add a routing entry in SKILL.md**
   - Add a row to the "Domain routing" table with the query topic and file path
   - Add a row to the "Reference files" table with the filename, description, and approximate line count

3. **Add a routing entry in POWER.md**
   - Add a row to the "Domain routing" table (same format as SKILL.md)
   - Add relevant keywords to the `keywords` list in the YAML frontmatter

4. **Update README.md**
   - Add a bullet under "What this skill covers"
   - Add the file to the "Directory structure" listing
   - Add usage examples if applicable

5. **Bump the plugin version**
   - `.claude-plugin/plugin.json` minor version (e.g. 1.19.0 to 1.20.0) for user-visible feature changes
   - `.claude-plugin/marketplace.json` description (update the reference file count and topic list)

---

## Reference-file frontmatter

All 28 reference files carry YAML FCP frontmatter that maps the file to the FinOps Framework
Capability it serves. New files must follow the same convention. Minimum schema:

```yaml
---
name: {file-identifier}                              # e.g. finops-aws
fcp_domain: "{one of 4 FCP domains}"                 # Understand Usage & Cost / Quantify Business Value / Optimize Usage & Cost / Manage the FinOps Practice
fcp_capability: "{primary capability}"               # the capability the file serves first
fcp_capabilities_secondary: ["{cap}", "{cap}"]       # optional - other capabilities the file touches
fcp_phases: ["{Inform}" or "{Optimize}" or "{Operate}", ...]   # one or more
fcp_personas_primary: ["{persona}", ...]             # FinOps Practitioner / Engineering / Finance / Product / Procurement / Leadership / SRE / Platform Engineering / Sustainability / Security / ITAM / etc.
fcp_personas_collaborating: ["{persona}", ...]       # optional
fcp_maturity_entry: "Crawl" | "Walk" | "Run"         # the gate below which the file is premature
---
```

Why this matters:
- Programmatic routing (future "load all references where fcp_capability=Anomaly Management"
  filter is feasible)
- Maturity gates (downstream tools and readers can detect when a reference is premature for
  their organisation's stage)
- Persona awareness (makes it explicit who each reference is written for, useful when
  curating subsets for specific audiences)
- Author discipline (declaring the FCP capability forces a check on whether the file
  actually serves what it claims to serve)

Do **not** add a `description` field to reference-file frontmatter. The visible blockquote
description on line 3 (after the H1) already serves that role; a frontmatter description
would render twice in some tools. The exception is `cloud-finops/SKILL.md` which DOES need
a `description` field for the Claude.ai upload skill loader (see "Content rules" below).

---

## Content rules

**Writing style**
- Use straight dashes (`-`), never em dashes
- Use British spelling for public-facing content (optimisation, organisation, behaviour)
- Be direct and practical. Diagnose before prescribing
- Connect cost recommendations to business outcomes

**SKILL.md frontmatter**
- The `description` field must be **under 1024 characters** (Claude.ai upload limit)
- Only `name` and `description` are required in the YAML frontmatter
- Do not add a `license` field to the frontmatter (it renders as visible text in Claude.ai)

**License**
- All content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- Credit OptimNow as the original author
- Include the license footer on new reference files if following the existing pattern

**Do not commit**
- `INTERNAL_NOTES.md` is gitignored and must never be committed
- `pipeline/` is gitignored and must not be made public without explicit decision

---

## Testing changes

After editing reference files, verify them by asking questions in the domain you changed.
Good test patterns:

- Ask a question that requires specific billing mechanics (pricing, break-even, discount rules)
- Ask a maturity-sensitive question (the response should adapt to Crawl/Walk/Run context)
- Ask a cross-domain question that requires loading multiple references
- Test with a non-Claude model using the response contract to verify portability

---

## Pull request checklist

- [ ] New reference file follows the `finops-{domain}.md` naming convention
- [ ] YAML FCP frontmatter included on the new file (see "Reference-file frontmatter")
- [ ] Routing table updated in both SKILL.md and POWER.md
- [ ] README directory listing and "What this skill covers" section updated
- [ ] CLAUDE.md "Repository structure" directory listing updated
- [ ] AGENTS.md and llms.txt updated to reflect the new reference (see "Lessons
      learned" section for the documentation-drift correction)
- [ ] install.sh per-tool routing updated: ChatGPT inline routing table, Gemini
      grouped knowledge, and Cursor description must mention the new domain
- [ ] File ends with the OptimNow footer (`> *Cloud FinOps Skill by [OptimNow]...
      CC BY-SA 4.0...*`); no truncation mid-sentence or mid-table
- [ ] Plugin version bumped in `.claude-plugin/plugin.json` (minor for user-visible feature)
- [ ] Marketplace description in `.claude-plugin/marketplace.json` reflects the new
      reference file count and topic list
- [ ] SKILL.md description stays under 1024 characters
- [ ] No em dashes in any public content
- [ ] No sensitive or internal files included
- [ ] Content is practical and based on how billing actually works, not on documentation summaries
- [ ] If the file deferred or replaced is in the Roadmap section, the Roadmap section is
      updated accordingly
