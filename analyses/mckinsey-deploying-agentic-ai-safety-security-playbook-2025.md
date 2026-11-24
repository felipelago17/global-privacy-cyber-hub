# McKinsey: Deploying agentic AI with safety and security, a playbook for technology leaders (Oct 2025)

`Agentic AI · Security governance · IAM for agents · Traceability · Consultancy playbook · Single source · Secondary summary`

Status as of 24 Nov 2026. This page rests on a tool-generated summary of the McKinsey Quarterly article plus search excerpts, not on a full read of the text. The summary gives the publication date as 16 Oct 2025 and the authors as Benjamin Klein, Charlie Lewis and Rich Isenberg, with named contributors. Statistics below are McKinsey's own or cited by McKinsey from other surveys, and I have not checked the underlying studies. Third-party write-ups (Workato, WebProNews, VerifyWise) describe the article differently in places and are not used as evidence here.

## Core argument

Agentic systems can reason, plan and act with little human oversight. The authors call them "digital insiders" that can cause harm through misalignment or compromise. They address CIOs, CROs, CISOs and DPOs and argue that safety and security must be built in from the start, not added later.

## Figures the article cites

- Agentic AI could contribute roughly USD 2.6 to 4.4 trillion a year across more than 60 gen AI use cases (McKinsey research, May 2024).
- About 1 percent of surveyed organisations say their AI adoption is mature (McKinsey, Jan 2025).
- About 80 percent of organisations report risky agent behaviour such as improper data exposure or unauthorised system access (SailPoint survey, May 2025).

## Risks identified

| Risk | Idea |
|---|---|
| Chained vulnerabilities | A flaw in one agent spreads and is amplified across others |
| Cross-agent task escalation | A compromised agent abuses trust to gain privileges |
| Synthetic-identity risk | Attackers forge or impersonate agent identities |
| Untraceable data leakage | Unlogged agent-to-agent exchanges hide leaks from audit |
| Data corruption propagation | Poor-quality data spreads silently through connected agents |

## Playbook, by stage

**Before deployment:** extend identity and access management and third-party risk management to agents; update risk taxonomies and assess each agentic use case; set lifecycle governance (ownership, human oversight, KPIs, escalation triggers), and document each agent's model, hosting, data sources, criticality, access rights and dependencies.

**Before launching a use case:** keep a central inventory of agent projects (owner, data use, status) and assess skills gaps such as AI security engineering and threat modelling.

**During deployment:** authenticate, log and permission agent-to-agent traffic; apply IAM to agents and add input and output guardrails; vet third-party agents like internal systems; log prompts, decisions, intermediate reasoning, state changes and outputs; plan for worst cases with termination and fallback mechanisms and sandboxed environments with defined network and data access.

## References named

ISO 27001, NIST CSF and SOC 2 (said not yet to cover agentic risk fully), GDPR Article 22, the US Equal Credit Opportunity Act, NYC Local Law 144, the EU AI Act, and the interoperability protocols MCP, Agent Connect Protocol, Agent2Agent and Agent Communication Protocol. The article notes that these protocols are still immature.

## Why a privacy and cyber hub should care

- **Agent identity is a control gap.** The playbook's IAM and synthetic-identity points line up with the credential-led intrusions in the [Unit 42 CL-STA-1238 page](unit42-cairn-cl-sta-1238-ai-driven-attacks-2026.md).
- **Logging serves privacy and security.** Prompt and decision logs support audit and incident response, but they also hold personal data, so retention and access rules apply to the logs themselves.
- **Inventory first.** A central register of agents is the precondition for DPIAs, records of processing and Article 22 analysis. See the hub's [agent risk tiering](../ai-agents/risk-tiering.md) and [insider risk and loss of control](../ai-agents/insider-risk-and-loss-of-control.md) pages, and [agent security in three layers](agent-security-three-layers.md).
- **Incident response.** Termination and fallback mechanisms are what the [MoFo agent incident response page](mofo-privacy-minute-ai-agent-incident-response-2026.md) asks teams to rehearse.

## Gaps and cautions

- Secondary reading of a consultancy article; it is a framework, not evidence of incidents or a legal standard.
- The statistics are McKinsey's or third-party survey figures I did not verify.
- The article says little, per my summary, on how to measure the guardrails' effectiveness.
- Some web summaries cite a November 2025 McKinsey survey with different numbers; I did not confirm those against McKinsey and they are not used.
- Not legal or security advice.
