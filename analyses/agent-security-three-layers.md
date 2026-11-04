# The Three Layers of Agent Security — Google DeepMind (June 2026)

`Global · AI governance · Cybersecurity · Agentic AI · Policy`

## Source

- **Title:** The Three Layers of Agent Security: A framework for policymakers
- **Author:** Google DeepMind
- **Date:** June 2026
- **Type:** Policy framework paper
- **Link:** see [`resources/papers/links.md`](../resources/papers/links.md)

## Summary

A framework aimed at policymakers for thinking about the security of AI agents — systems that plan and act on behalf of users with some autonomy. Security is organised into three layers: the individual agent, the multi-agent environment, and the broader cyber-defence ecosystem. The paper's throughline is **secure-by-design**, continuous **monitoring**, and **coordinated resilience** rather than point-in-time certification.

## Key findings

### Layer 1 — Securing individual agents

- **Upstream interventions:** model-level safeguards built in before deployment (training for instruction hierarchy, resistance to prompt injection, capability controls).
- **Downstream interventions:** runtime controls around the agent — permissions and least privilege, sandboxing, tool-use authorisation, human-in-the-loop for high-impact actions, logging and observability.
- **Standards:** the paper calls for technical standards for agent security but recognises the field is immature; it recommends **pre-standardisation R&D and consensus-building** (shared threat models, evaluation suites, red-teaming norms) before locking in requirements.

### Layer 2 — Multi-agent risks

- **Cascading failures:** errors or compromises propagating across chains of interacting agents, including through shared tools, data sources or protocols.
- **Weaponisation of information environments:** agents manipulating or being manipulated through the content they read (indirect prompt injection at scale), and coordinated agent activity distorting markets, platforms or discourse.
- Mitigations: provenance and authentication between agents, rate and scope limits, circuit-breakers, and monitoring at the system (not just agent) level.

### Layer 3 — Empowering cyber defenders

- Agents will be used offensively; the policy response is to make sure defenders have **equal or better** access to agentic capabilities.
- Recommends investment in defensive agent tooling, vulnerability discovery and patching at scale, information-sharing, and workforce enablement.

## Practical implications

- For **governance teams**: map existing AI risk controls against the three layers; most programmes cover Layer 1 (model safety) and neglect Layers 2 and 3.
- For **deployers of agents**: implement the downstream controls now — least-privilege tool access, action logging, approval gates for irreversible actions — regardless of regulatory timing.
- For **regulators / standards bodies**: the paper is effectively a request not to over-specify technical requirements prematurely, but to fund shared evaluations and threat models first.
- Cross-reference with the OWASP AI Security and Privacy Guide and the OWASP Top 10 for LLM applications, which supply the concrete control vocabulary the DeepMind paper abstracts over.

## Open questions / critique

- The framework is vendor-authored; it is light on obligations that would fall on frontier developers themselves (e.g. mandatory disclosure of agent capabilities or incident reporting).
- Liability allocation across the agent supply chain (model provider, orchestration platform, deployer, tool provider) is not addressed.

## Source notes

Summary prepared from the DeepMind paper as published. Layer names and the upstream/downstream distinction are the paper's own terminology.
