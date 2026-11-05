# Agent security checklist

**Source:** [DeepMind, The Three Layers of Agent Security](../../analyses/agent-security-three-layers.md) (June 2026), with control vocabulary from the OWASP Top 10 for LLM Applications.

## Layer 1 — Individual agent

### Upstream (model / design)
- [ ] Model selected has documented resistance to prompt injection and instruction-hierarchy training
- [ ] Capability scope defined: what the agent may do, with which tools, on which data
- [ ] Threat model written for the agent (assets, attackers, entry points incl. untrusted content)

### Downstream (runtime)
- [ ] **Least privilege** on every tool and credential; no standing admin rights
- [ ] Sandboxing / isolation for code execution and file access
- [ ] **Approval gates** for irreversible or high-impact actions (payments, deletions, external sends)
- [ ] Untrusted content (web pages, emails, documents) treated as data, not instructions; input filtering where feasible
- [ ] Output handling: no direct execution of model output without validation
- [ ] Full action logging (prompts, tool calls, results) retained and reviewable
- [ ] Rate limits and spend limits per agent
- [ ] Kill switch / disable path tested

## Layer 2 — Multi-agent environment
- [ ] Inventory of agent-to-agent interactions and shared tools/data sources
- [ ] Authentication and provenance between agents (no anonymous agent calls)
- [ ] Scope and rate limits on inter-agent requests; circuit-breakers for cascades
- [ ] System-level monitoring (not only per-agent) for anomalous coordinated behaviour
- [ ] Shared data sources assessed for poisoning / indirect-injection risk
- [ ] Incident playbook for cascading failure (isolate, roll back, communicate)

## Layer 3 — Defender enablement
- [ ] Security team has access to agentic tooling for detection, triage and patching
- [ ] Vulnerability disclosure and information-sharing channels in place (internal and sector)
- [ ] Red-teaming of agents scheduled and findings tracked
- [ ] Skills and training plan for defenders on agentic threats

## Additions from the 2025–26 incident record
Source: [AI agents — privacy and cyber risks](../../ai-agents/index.md) (Nov 2026). Each item maps to at least one catalogued incident.
- [ ] No long-lived or fully-permissioned deployment tokens discoverable by the agent (repo, env, config) — *PocketOS, Composio, OpenAI/Hugging Face*
- [ ] Project-controlled config (hooks, `.mcp.json`, env vars) never loaded before an explicit trust decision; no auto-trust in CI — *Claude Code, Cursor, Gemini CLI CVEs*
- [ ] MCP servers, extensions and skills inventoried, pinned and re-verified after updates; tool descriptions scanned for hidden instructions — *postmark-mcp, Deadbugz*
- [ ] Exfiltration side-channels closed: image-proxy fetches, allow-listed domains that can lapse, DNS from tool output — *CamoLeak, ForcedLeak, SalesBleed, SearchLeak*
- [ ] Hard constraints re-injected after context compaction — *OpenClaw inbox deletion*
- [ ] Approval UI renders exactly what will execute; execution bound to approved parameters — *Loopjacking*
- [ ] Agent has no write access to its own monitoring, alerting or audit configuration — *OpenAI, Oct 2026*
- [ ] Agent cannot create public resources (repos, pastes, shares) without a gate — *PixelLeak*
- [ ] Evaluation / red-team environments with relaxed safeguards have stronger isolation, real-time blocking and independent review — *AISI incident report, OpenAI/Hugging Face*
- [ ] Memory partitioned per agent and purpose, with expiry; access/erasure requests reach memory and logs — *AEPD, CNIL*
- [ ] Breach-response playbook has an "autonomous actor" branch — *AEPD first agent-attributed notification*

## Governance
- [ ] Agent use cases mapped to the organisation's AI risk register and, where applicable, EU AI Act / NIST AI RMF
- [ ] Liability and responsibility across the supply chain (model provider, orchestration, deployer, tool providers) documented in contracts
- [ ] Review cadence set; controls re-tested on model or tool changes
