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

## Governance
- [ ] Agent use cases mapped to the organisation's AI risk register and, where applicable, EU AI Act / NIST AI RMF
- [ ] Liability and responsibility across the supply chain (model provider, orchestration, deployer, tool providers) documented in contracts
- [ ] Review cadence set; controls re-tested on model or tool changes
