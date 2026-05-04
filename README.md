# cloud-finops-skills

> Built by [OptimNow](https://optimnow.io). Covers cloud financial management across
> AWS, Azure, GCP, AI inference costs, GenAI capacity planning, SaaS asset management,
> and tagging governance - grounded in enterprise delivery experience.

[![GitHub Stars](https://img.shields.io/github/stars/OptimNow/cloud-finops-skills?style=flat)](https://github.com/OptimNow/cloud-finops-skills/stargazers)
[![FinOps Framework](https://img.shields.io/badge/FinOps-Framework-blue)](https://www.finops.org/framework/)
[![Agent Skills](https://img.shields.io/badge/Agent-Skills%20Spec-green)](https://agentskills.io/specification)
[![Kiro Power](https://img.shields.io/badge/Kiro-Power-orange)](https://kiro.dev/docs/powers/installation/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Install in 5 seconds

| Tool | One-step install |
|---|---|
| <img src="https://img.shields.io/badge/-Claude%20Code-D97757?logo=anthropic&logoColor=white" alt="Claude Code" height="22"/> | At the Claude Code prompt: `/plugin marketplace add https://github.com/OptimNow/cloud-finops-skills.git` then `/plugin install cloud-finops@optimnow` |
| <img src="https://img.shields.io/badge/-Claude.ai%20%2F%20Desktop-D97757?logo=anthropic&logoColor=white" alt="Claude.ai / Claude Desktop" height="22"/> | [Download the latest release zip](https://github.com/OptimNow/cloud-finops-skills/releases/latest), then **Settings -> Skills -> Upload zip** |
| <img src="https://img.shields.io/badge/-ChatGPT-10A37F?logo=openai&logoColor=white" alt="ChatGPT" height="22"/> | Self-host: `./install.sh --tool chatgpt --grouped` _(a public Cloud FinOps GPT is on the Roadmap)_ |
| <img src="https://img.shields.io/badge/-Gemini-4285F4?logo=googlegemini&logoColor=white" alt="Gemini" height="22"/> | Self-host: `./install.sh --tool gemini` _(a public Cloud FinOps Gem is on the Roadmap)_ |
| <img src="https://img.shields.io/badge/-Cursor-000000?logo=cursor&logoColor=white" alt="Cursor" height="22"/> <img src="https://img.shields.io/badge/-Windsurf-3DDC91?logoColor=white" alt="Windsurf" height="22"/> <img src="https://img.shields.io/badge/-Codex-412991?logo=openai&logoColor=white" alt="Codex" height="22"/> <img src="https://img.shields.io/badge/-Aider-0F172A?logoColor=white" alt="Aider" height="22"/> <img src="https://img.shields.io/badge/-Copilot-181717?logo=githubcopilot&logoColor=white" alt="Copilot" height="22"/> <img src="https://img.shields.io/badge/-Kiro%20IDE-FF6F00?logoColor=white" alt="Kiro IDE" height="22"/> <img src="https://img.shields.io/badge/-Gemini%20CLI-4285F4?logo=googlegemini&logoColor=white" alt="Gemini CLI" height="22"/> | One-liner: `curl -sL https://raw.githubusercontent.com/OptimNow/cloud-finops-skills/main/install.sh \| bash -s -- --tool <name>` |
| <img src="https://img.shields.io/badge/-Auto--detect-555555?logo=gnubash&logoColor=white" alt="Auto-detect" height="22"/> | `curl -sL https://raw.githubusercontent.com/OptimNow/cloud-finops-skills/main/install.sh \| bash` |

Full options, troubleshooting, and the model-agnostic API loader: see [INSTALLATION.md](./INSTALLATION.md).

---

## What is a Skill, and why does it matter

A Skill is a structured knowledge file that you attach to an AI agent or a large language
model. It gives the model accurate, domain-specific context that it would not otherwise
have access to.

Without it, general-purpose LLMs make confident but incorrect statements on FinOps topics.
They miscalculate PTU break-even rates. They confuse Azure and AWS reservation mechanics.
They give generic advice that ignores how billing actually works on Bedrock or Azure OpenAI.
The answers sound plausible. Most of the time, they are wrong on the details that matter.

This skill corrects that by injecting verified, curated FinOps knowledge directly into the
model's context - covering billing models, cost allocation patterns, optimisation
frameworks, and governance practices across the major cloud providers and AI platforms.

**The closest analogy is RAG (Retrieval-Augmented Generation).** Like RAG, it extends a
model's knowledge beyond its training data. Unlike RAG, it requires no vector database,
no embedding pipeline, and no retrieval infrastructure. You copy a folder into your agent
setup and the model gains structured expertise on cloud financial management.

This makes it portable: the same skill works with Claude, GPT, Gemini, or any
MCP-compatible agent - with no changes to the files.

To keep responses consistent across models, add a **response contract** to your
system prompt (see `INSTALLATION.md`, "API integration / Recommended response
contract"). This ensures structured, billing-grounded answers even when model
defaults differ.

---

## Who this is for

- **FinOps practitioners** building or evaluating AI-assisted cost analysis tools
- **Cloud engineers and architects** who want a cost-aware assistant integrated into
  their workflow
- **Developers** building internal FinOps agents, chatbots, or automation pipelines
- **Finance and IT managers** evaluating the AI tooling their teams are deploying

No AI infrastructure experience is required to use this skill. If you can copy a folder
and follow the installation steps, you can add FinOps expertise to any compatible agent.

---

## What this skill covers

The skill provides accurate, framework-aligned guidance across the following domains:

- **FinOps for AI** - LLM inference economics, token cost management, agentic cost
  patterns, unit economics for AI features, ROI frameworks, and AI cost governance
- **AI value management** - AI Investment Council, stage gate model, incremental
  funding, practice operations, cross-functional governance for AI investments
- **GenAI capacity planning** - provisioned vs shared capacity, traffic shape analysis,
  spillover mechanics, throughput units, cross-provider comparison
- **Self-hosted vs managed AI inference** - decision framework for "should we self-host our
  LLM?" with per-token vs per-hour billing comparison, hidden cost surface (operational,
  reliability, compliance, talent FTEs), 5-criteria ML-Ops maturity rubric, hybrid routing
  patterns (LiteLLM, Portkey), eight client diagnostic questions, six common anti-patterns
- **Anthropic billing** - Claude model pricing, Fast mode, long-context cliffs,
  prompt caching, Batch API, governance controls
- **AWS Bedrock** - model pricing, provisioned throughput, batch inference, cost allocation
- **Azure OpenAI Service** - PTU pool model, deployment locality, spillover mechanics,
  model modernisation, optimisation framework, use case economics, cost visibility
- **GCP Vertex AI** - Gemini pricing, provisioned throughput, batch prediction, cost visibility
- **AWS FinOps** - CUR setup, Cost Explorer, EC2 rightsizing, Reserved Instances vs
  Savings Plans, Enterprise Discount Program (EDP) negotiation, RDS cost management,
  multi-organisation billing, cost allocation, SCPs, and AWS-native quick wins
- **Azure FinOps** - Azure Cost Management, Reservations, Azure Policy, FinOps Toolkit,
  Azure Hybrid Benefit, EA-to-MCA transition impact, and Azure-specific optimisation patterns
- **GCP FinOps** - Compute Engine, Cloud SQL, GCS, BigQuery, networking optimisation
- **Tagging governance** - tag taxonomy design, naming conventions, IaC enforcement,
  virtual tagging, MCP-based automation, and compliance monitoring
- **FinOps Framework** - full FinOps Foundation framework, 22 capabilities, maturity model
- **Databricks** - cost data foundations (system.billing.usage, budget policies, serverless and model-serving attribution), allocation and governance (DBU executor patterns, DBCU commitments, Photon and serverless multipliers, amortised vs PAYG split, Azure VM RI vs DBU clarification), cluster optimisation, jobs, Spark, Unity Catalog costs
- **Microsoft Fabric** - capacity FinOps (F-SKU model, Capacity Units, 24-hour CU smoothing, throttling), pause / resume, Reserved Capacity, the Pro/PPU to Fabric migration governance trap, shared-capacity allocation models, Capacity Metrics app
- **Snowflake** - warehouse optimisation, query tuning, storage, credits, QUERY_ATTRIBUTION_HISTORY, Budgets including AI feature budgets, Cortex governance, resource monitor scope limit
- **AI coding tools** - Cursor, Claude Code, Copilot, Windsurf, Codex billing models,
  cost attribution with LiteLLM proxy, seat + usage vs BYOK architecture comparison,
  optimisation levers, cross-tool spend overlap audit
- **OCI** - compute, storage, networking optimisation
- **SaaS asset management (SAM)** - SaaS discovery, license optimization, renewal
  governance, SaaS Management Platforms (SMPs), shadow IT detection, sprawl patterns,
  and the connection to AI transition readiness
- **ITAM collaboration** - FinOps-ITAM joint operating model, BYOL cost mechanics,
  marketplace channel governance, Tier 1 vendor co-management, consumption-based SaaS
  overage monitoring, entitlement integration, and maturity framework
- **GreenOps and cloud carbon** - carbon measurement tooling, FinOps-to-GreenOps
  integration, carbon-aware workload shifting, region selection, GHG Protocol reporting
- **Anomaly management** - cost anomaly detection as a standalone Inform-phase
  capability: AWS Cost Anomaly Detection / Azure / GCP native tooling, threshold
  philosophy (absolute dollars plus percentage), layered detection across service,
  region, account, and tag scopes, the masked-anomaly failure mode, new-region
  detection, integration with Security
- **Allocation and showback** - cost allocation methodology and the showback
  delivery model that earns the upgrade to chargeback. FOCUS cost columns
  (`EffectiveCost` vs `BilledCost`) with explicit AWS legacy mapping (amortised
  vs unblended) and a `blended_cost` trap warning. Defensible allocation keys
  table, shared-services hard cases (network, observability, security, ingress),
  `InvoiceId` reconciliation, unallocated spend > 10% as a tagging signal,
  showback report design and routing into team-existing surfaces, data-quality
  dispute process
- **Chargeback** - soft-to-hard chargeback maturity ladder built on top of
  allocation and showback. Covers the Finance and accounting prerequisites
  that determine whether hard chargeback is operationally possible at all:
  ERP readiness (SAP CO cycles, Oracle / Workday / NetSuite equivalents),
  inter-BU P&L impact and incentive-plan alignment, CFO sponsorship as a
  hard requirement, transfer pricing for intercompany cloud recharges
  (cost-plus methodology, re-characterisation risk), cross-border tax
  mechanics (VAT reverse-charge, withholding, permanent-establishment risk,
  EU/OECD Pillar 2 minimum tax, US GILTI/FDII/BEAT), SOX-equivalent controls,
  decision-owner table mapping each prerequisite to the right Finance role,
  methodology dispute process, the chargeback-revolt anti-pattern (12-18
  months of credibility loss when skipped)
- **Onboarding workloads** - migration-time cost hygiene as the cheapest
  moment to enforce tagging, allocation, forecasting, and commitment-strategy
  alignment. Covers the intake gate (mandatory checklist + three
  implementation patterns: PR gate, cutover gate, pre-prod gate), the 60-90
  day forecast-then-commit rule that prevents committing on a volatile
  baseline, the double-bubble cost (parallel-run source and target) with
  explicit shutoff discipline, the migration-cost-estimate-vs-actuals trap
  driven by data-centre-to-cloud network cost differences, M&A integration
  playbook (months 1-12 sequence), FOCUS-during-migration logic, cost-aware
  architecture review integration, the requirement for a named
  post-migration FinOps owner
- **Kubernetes FinOps** - the cross-cluster discipline (EKS, GKE, AKS) for
  the hardest variant of cloud-cost allocation. Covers tooling choice
  (OpenCost / Kubecost / cloud-native), FOCUS-emitting K8s allocation with
  K8s-labels-to-FOCUS-Tags mapping (so per-pod costs join non-K8s costs in
  the warehouse), container rightsizing methodology (VPA in
  recommendation-only mode, p99 + 30% memory safety margin, p95 + 50% CPU
  safety, per-workload rollout), node-level autoscaling (Karpenter beats
  Cluster Autoscaler on cost efficiency where available, consolidation
  policy tuning, Pod Disruption Budgets as non-negotiable, Spot
  diversification across instance types and availability zones), and idle
  node cost as Platform team overhead rather than redistributed across
  application teams. Provider-specific node mechanics live in the per-cloud
  files
- **Waste detection playbooks** - OptimNow's seven-category waste taxonomy
  (orphaned, idle, overprovisioned, commitment mismatches, schedule
  blindness, modernization opportunities, AI/ML inefficiency) covering
  the detection patterns, two-signal classification rule, three-tier
  confidence model (obvious / likely / possible), and realised-vs-potential
  savings discipline. Operationally backed by the OptimNow WasteLine
  appliance for AWS (49 deterministic detection rules, read-only, with
  proposal-only remediation artifacts); for Azure and GCP, points to the
  in-cloud pattern catalogues. Crawl/Walk/Run progression from manual
  quarterly hunt to continuous Fargate-scheduled detection

All guidance is framed through OptimNow's methodology: connecting cost to business value,
diagnosing before prescribing, and recommending actions matched to organisational maturity.

---

## Design principles

- **AI cost management is a first-class domain.** Most FinOps resources treat AI
  workloads as an edge case. This skill treats them as a primary concern, with
  dedicated reference files for each major AI platform.
- **Visibility before optimisation.** The skill follows a consistent sequence:
  establish what you are spending, understand what is driving it, then act. It does
  not recommend optimisation steps before the visibility preconditions are met.
- **Provider-mechanics-first, vendor-claim-skeptical.** Guidance is grounded in how
  billing actually works (CUR columns, Azure cost-management semantics, BigQuery
  export, FOCUS conformance) rather than in vendor marketing or framework
  positioning. Vendor sustainability and savings claims are read critically, with
  primary sources cited.
- **Maturity is contextual, not aspirational.** Verticals where cloud is not a
  revenue generator do not need to reach Run; Crawl plus selective Walk is the right
  state when cloud is a cost centre. Verticals where cloud IS the product need Run
  because cloud efficiency directly drives gross margin. Pushing every organisation
  toward the same maturity ceiling is malpractice.
- **Connect cost to business value.** Every recommendation answers the CFO test:
  what business outcome does this protect or unlock. Cost reduction without a value
  lens is a leak.
- **FinOps is an operating discipline, not a culture.** The discipline lives in
  allocation, anomaly management, commitment management, rightsizing, and
  governance, all of which produce measurable outputs. "Culture of FinOps" framing
  tends to substitute slideware for those outputs. In the agentic era this matters
  more, not less: agents execute discipline, not culture.

These principles will grow into a `cloud-finops/doctrine/` directory of opposable
theses with their own primary sources; see the `Roadmap` section of `CLAUDE.md`.

---

## Usage examples

These questions illustrate what this skill is designed to answer accurately.
A general-purpose LLM without this skill will produce plausible but unreliable answers
to most of them - particularly on billing mechanics, capacity economics, and
provider-specific behaviour.

<div>
  <a href="https://www.loom.com/share/cc76d419adc64b1784e58621d6934d3e">
    <p>Cloud FinOps skill - Watch Video</p>
  </a>
  <a href="https://www.loom.com/share/cc76d419adc64b1784e58621d6934d3e">
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/cc76d419adc64b1784e58621d6934d3e-906aded8593a48f3-full-play.gif#t=0.1">
  </a>
</div>

### FinOps for AI

- "We're spending $40K/month on AWS Bedrock and have no idea which features are driving it. Where do we start?"
- "How do I calculate ROI for our AI support bot?"
- "Our inference costs doubled last month - what are the most likely causes?"
- "Should we use Claude Haiku or Sonnet for our classification pipeline?"

### AI value management

- "We have 14 AI projects running across the company and no one knows the total spend. Our CFO wants a governance framework by next quarter."
- "How should we structure an AI Investment Council?"
- "What stage gate model works for AI projects that move faster than our quarterly review cycle?"
- "How do we fund AI experiments incrementally without runaway exposure?"

### GenAI capacity planning

- "We need to choose between Azure OpenAI PTUs and AWS Bedrock provisioned throughput for a production chatbot doing 500K requests/day."
- "Our traffic is bursty - does provisioned capacity make sense or should we stay on pay-as-you-go?"
- "What's the difference between spillover on Azure vs building failover logic on Bedrock?"
- "How do I calculate the break-even utilisation rate for provisioned throughput?"

### Self-hosted vs managed AI inference

- "Should we self-host Llama 4 on rented H100s instead of paying Anthropic per token?"
- "What hidden costs do TCO calculators miss when comparing vLLM on rented GPUs to managed APIs?"
- "Are we mature enough to run our own inference stack? What does that maturity actually require?"
- "How do we design a hybrid stack: self-hosted Qwen3.6 for high-volume RAG, Claude Opus for frontier reasoning?"

### Anthropic billing

- "We're running Claude Sonnet on both AWS Bedrock and the direct Anthropic API. Our monthly bill jumped from $12K to $38K after a developer enabled Fast mode in Claude Code. How do I get this under control and prevent it from happening again?"
- "What's the real cost impact of the 200K input token long-context cliff?"
- "How do prompt caching multipliers work on Anthropic - when do cache writes cost more than they save?"
- "Should we route Claude traffic through Bedrock or use the direct Anthropic API?"

### AWS Bedrock

- "How does Bedrock provisioned throughput work and when does it make sense vs on-demand?"
- "What CloudWatch metrics should we monitor for Bedrock cost and performance?"
- "How do we tag and allocate Bedrock costs across teams when per-request tags aren't supported?"
- "What's the batch inference discount on Bedrock and which workloads should use it?"

### Azure OpenAI Service

- "How do PTU reservations work and what are the waste risks?"
- "We reserved 500 PTUs but only deployed 150 - how do we fix this?"
- "Is provisioned capacity on Azure OpenAI actually cheaper than pay-as-you-go for GPT-5?"
- "How does spillover work on Azure OpenAI and how do we monitor the PAYG overflow cost?"

### GCP Vertex AI

- "What's the cost difference between Gemini Flash and Gemini Pro on Vertex AI for a classification pipeline?"
- "How does provisioned throughput on Vertex AI compare to Bedrock and Azure?"
- "What Cloud Monitoring metrics should we track for Vertex AI cost visibility?"
- "When should we use Vertex AI Batch Prediction instead of on-demand inference?"

### AWS FinOps

- "We have $80K/month in EC2. Should we buy Reserved Instances or Savings Plans?"
- "How do I set up CUR for multi-account cost allocation?"
- "What are the quick wins I should address before any commitment purchase?"
- "We're approaching $2M annual AWS spend - should we negotiate an EDP and what should we watch out for?"
- "Our RDS costs keep climbing - what's the right optimisation sequence?"
- "How do custom billing views work across multiple AWS organisations?"

### Azure FinOps

- "What's the Azure equivalent of AWS CUR?"
- "How do Azure Reservations compare to Azure Savings Plans?"
- "We need to enforce tagging across 15 subscriptions - what's the right approach?"
- "How do we use Azure Hybrid Benefit to reduce our VM costs?"
- "We're migrating from EA to MCA - what FinOps work do we need to do before the switch?"

### Tagging governance

- "What are the minimum mandatory tags we should require?"
- "How do we enforce tags without blocking deployments?"
- "What's the difference between physical and virtual tagging?"
- "How does OptimNow's MCP for Tagging work?"

### GreenOps and cloud carbon

- "We need to start reporting our cloud carbon emissions - where do we begin?"
- "How do we pick lower-carbon regions without sacrificing latency?"
- "What's the Carbon Aware SDK and can we use it to shift batch jobs to cleaner time windows?"
- "How do we add carbon tracking to our existing FinOps dashboards?"

---

## Directory structure

```
cloud-finops-skills/
├── README.md                                   ← This file
├── INSTALLATION.md                             ← Setup instructions
├── LICENSE.md                                  ← CC BY-SA 4.0
└── cloud-finops/                               ← Install this folder
    ├── SKILL.md                                ← Entry point + domain router (Claude Code, generic agents)
    ├── POWER.md                                ← Entry point (Kiro IDE)
    └── references/
        ├── optimnow-methodology.md             ← OptimNow reasoning philosophy
        ├── finops-for-ai.md                    ← AI cost management
        ├── finops-ai-value-management.md       ← AI investment governance
        ├── finops-genai-capacity.md            ← GenAI capacity models (cross-provider)
        ├── finops-ai-self-hosted-vs-managed.md ← Self-hosted vs managed AI inference decision
        ├── finops-anthropic.md                 ← Anthropic billing + governance
        ├── finops-aws.md                       ← AWS-specific FinOps
        ├── finops-bedrock.md                   ← AWS Bedrock billing
        ├── finops-azure.md                     ← Azure-specific FinOps
        ├── finops-azure-openai.md              ← Azure OpenAI Service (PTUs)
        ├── finops-gcp.md                       ← GCP-specific FinOps
        ├── finops-vertexai.md                  ← GCP Vertex AI billing
        ├── finops-tagging.md                   ← Tagging and naming governance
        ├── finops-framework.md                 ← Full FinOps Foundation framework
        ├── finops-databricks.md                ← Databricks allocation, governance, and optimisation
        ├── finops-fabric.md                    ← Microsoft Fabric capacity FinOps
        ├── finops-snowflake.md                 ← Snowflake optimisation
        ├── finops-ai-dev-tools.md             ← AI coding tools (Cursor, Claude Code, etc.)
        ├── finops-oci.md                       ← OCI optimisation
        ├── finops-sam.md                       ← SaaS asset management (SAM)
        ├── finops-itam.md                     ← ITAM collaboration (BYOL, marketplace, entitlements)
        ├── greenops-cloud-carbon.md            ← GreenOps and cloud carbon
        ├── finops-anomaly-management.md        ← Anomaly management (standalone Inform-phase capability)
        ├── finops-allocation-showback.md       ← Cost allocation methodology + showback
        ├── finops-chargeback.md                ← Chargeback maturity ladder + Finance/accounting prerequisites
        ├── finops-onboarding-workloads.md      ← Migration-time cost hygiene + M&A integration
        ├── finops-kubernetes.md                ← Kubernetes cross-cluster discipline (EKS/GKE/AKS)
        └── finops-waste-detection-playbooks.md ← Seven-category waste taxonomy + WasteLine
```

The `SKILL.md` file is the entry point for Claude Code and generic agents. `POWER.md` is
the entry point for Kiro IDE. Both route queries to the same reference files - the
domain-specific content is shared.

---

## Installation

The skill installs into 11 different tools via a single bash installer that converts
the canonical Claude / Agent-Skills format into each target tool's expected shape.
See **[INSTALLATION.md](./INSTALLATION.md)** for the full per-tool instructions.

### One-liner (auto-detect)

```bash
curl -sL https://raw.githubusercontent.com/OptimNow/cloud-finops-skills/main/install.sh | bash
```

Auto-detects which tools you have installed (Claude Code, Cursor, Windsurf, Codex, etc.)
and installs the skill for each, with the right per-tool conversion.

### One specific tool

```bash
curl -sL https://raw.githubusercontent.com/OptimNow/cloud-finops-skills/main/install.sh | bash -s -- --tool <name>
```

Supported tools: `claude-code`, `claude-projects`, `cursor`, `windsurf`, `chatgpt`,
`gemini`, `gemini-cli`, `codex`, `aider`, `copilot`, `kiro`. Run `./install.sh --list`
to see them all.

### Claude Code plugin (auto-updating alternative)

For Claude Code specifically, the skill is also distributed as a self-hosted plugin
with built-in update via `/plugin update`. Two commands at the **Claude Code prompt**
(not your shell):

```text
/plugin marketplace add https://github.com/OptimNow/cloud-finops-skills.git
/plugin install cloud-finops@optimnow
```

To pull the latest content (including the twice-monthly automated updates):

```text
/plugin update cloud-finops@optimnow
```

**Note on the URL form:** the explicit HTTPS URL above avoids an SSH-authentication
prompt that some Claude Code installs hit when given the `OptimNow/cloud-finops-skills`
shorthand. The repository is fully public over HTTPS - no credentials needed.

### Claude Desktop / claude.ai

For the web / desktop apps, the installer can build a clean upload zip:

```bash
./install.sh --tool claude-projects
```

Then upload `dist/claude-projects/cloud-finops.zip` via Settings → Skills → Upload zip.
A version-tagged build (`cloud-finops-vX.Y.Z.zip`) is also attached to every
[GitHub release](https://github.com/OptimNow/cloud-finops-skills/releases) for
users who prefer downloading over building locally.

---

## This skill is actively maintained

This is a living repository. Reference files are refreshed twice a month (around the
1st and the 15th), driven by an automated scan of 29 data sources - cloud provider
pricing pages, release notes, billing changelogs, and FinOps community publications.
Changes are reviewed before being applied, so the content reflects verified updates
rather than raw feed output.

AI cost management is moving particularly fast - new model releases, capacity options, and
billing mechanics appear every few weeks. Watch or star this repo to be notified when
updates are published.

---

## Contributing

**Process and credit.** Open an issue first for anything larger than a typo or
single fact correction, so we can scope before you write. Pull requests should
keep the existing structure of the file you are touching, follow the conventions
in [`CLAUDE.md`](./CLAUDE.md) (FCP frontmatter, no em dashes, British spelling
in prose, license footer), and pass the FCP coverage check
(`./scripts/fcp-coverage.sh --check`).

You keep authorship: every contribution lives in the commit history under your
name and shows up in `git blame`. Substantive contributors are visible in the
repo's contributors list on GitHub.

**License and what that means for you.** All contributions are licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This is an
OptimNow-maintained repo, but CC BY-SA was chosen specifically so anyone -
including you - can fork, customise, and redistribute under their own brand,
as long as they credit and share-alike. If you want a project under your own
name rather than contributing here, fork freely; see "Adapting this skill for
your organisation" below for the fork playbook. Both paths are first-class.

Practitioner experience is the highest-value contribution. Frameworks and
vendor docs are already public; what is rare is "we tried X in production,
this is what actually billed". Issues and PRs that bring that lens are welcome
in any of the layers below.

**Concrete contribution types we actively want:**

- **Pricing or billing-mechanic correction.** A CUR column name we got wrong, a
  CUD / Reservation discount depth that has shifted, a refund cap that does not
  match the latest contract terms. Cite the primary source (provider doc, your
  invoice, an enrollment agreement) so the change is verifiable.
- **New named playbook.** A waste pattern you see in the field that is not yet in
  `cloud-finops/playbooks/`. Follow the format documented in
  [`playbooks/README.md`](./cloud-finops/playbooks/README.md): symptoms / detection
  query / fix / anti-pattern / sources, ~2-4 KB. Examples we'd love: Lambda
  cold-start sprawl, Bedrock model proliferation, Snowflake warehouse fragmentation,
  Databricks all-purpose-cluster default-on, Cloud Run min-instance creep.
- **Fix or enrich an existing playbook.** A detection query that returns
  false positives in your data, an anti-pattern you saw burn a team, a fix step
  that does not work without a precondition we missed.
- **Pick up a deferred reference file.** The `Roadmap > Deferred reference
  files` section of [`CLAUDE.md`](./CLAUDE.md) lists the P2/P3 items
  (forecasting, unit economics, practice operations, education & enablement,
  benchmarking, cost warehouse) with the rationale and trigger to revisit.
  If your engagement has surfaced one of those, that is the trigger - open
  an issue with the engagement context and we will scope the file together.
- **Tool installer addition.** Adding `--tool <new-tool>` for a coding
  assistant or agent we do not yet support. Match the existing
  installer pattern in `install.sh` (idempotent, dry-run-safe, exclude
  local-only files like `.claude/` and `.backups/`).
- **Real-world case study or counter-example.** Something you tried that did
  not work, or worked under conditions we do not flag. These end up as
  anti-pattern blocks in the relevant reference or playbook.
- **Adversarial review.** Disagreement on a recommendation, with reasoning
  and ideally a source. The repo is opinionated; it should also be falsifiable.
- **Bug report.** Installer fails on your setup, a file does not render in your
  tool, a guard rail false-positives. Open an issue with the exact command and
  output.
- **Translation.** Selected references in another language, maintained as a
  parallel directory rather than a fork, when you can commit to keeping them
  in sync with the next refresh.

**What we push back on:**

- Vendor marketing material restated as fact, without a primary source or
  practitioner-grade evidence behind the claim.
- Wholesale AI-generated reference content with no human practitioner pass.
  The pipeline that powers the bi-monthly refresh has hard guard rails (see
  the `Lessons learned` section of `CLAUDE.md` for why). Hand-written
  contributions go through human review for the same reasons.
- "Best practices" lists with no business-value framing. Every recommendation
  in this repo connects cost to a business outcome; contributions should follow
  that pattern.

---

## Adapting this skill for your organisation

Fork this repository and customise the reference files for your organisation's context:
your cloud stack, your internal policies, your tag taxonomy, your preferred methodology.

A fork gives you a stable base that you can pull upstream updates into at your own pace,
without overwriting your customisations. Typical customisations include:

- Adding organisation-specific tag requirements to `finops-tagging.md`
- Replacing generic pricing examples with your negotiated rates
- Adding reference files for internal tools or platforms not covered here
- Adjusting the methodology file to reflect your team's own approach

---

## About OptimNow

OptimNow is a boutique FinOps consultancy helping organisations connect cloud and AI
spend to measurable business value. Based in France with European reach.

- Website: [optimnow.io](https://optimnow.io)
- LinkedIn: [OptimNow](https://linkedin.com/company/optimnow)
- GitHub: [github.com/OptimNow](https://github.com/OptimNow)

**Open-source tools built by OptimNow:**
- [AI Cost Readiness Assessment](https://aicostsfinops.optimnow.io)
- [AI ROI Calculator](https://optimnow.io)
- [MCP for Tagging](https://github.com/OptimNow/finops-mcp)
- [FinOps Maturity Assessment](https://optimnow.io)

---

## Acknowledgements

This skill incorporates content derived from the following sources:

- **[FinOps Foundation](https://www.finops.org/)** - framework definitions, capability
  descriptions, and maturity model structure are based on the FinOps Framework.
- **[Point Five](https://www.pointfive.co)** - cloud optimisation recommendations
  informed several provider-specific best practices and quick-win patterns.

All referenced content has been adapted with additional context from OptimNow's
consulting delivery experience. Any errors or opinionated interpretations are our own.

This skill is independently maintained and is not affiliated with or endorsed by the
FinOps Foundation.

---

## License

Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
See [LICENSE.md](./LICENSE.md).

You are free to use, adapt, and redistribute this skill - including for commercial
purposes - as long as you credit OptimNow and share any derivatives under the same license.
