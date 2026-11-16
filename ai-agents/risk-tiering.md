# Tiering agent risk by consequence, not by model sophistication

`Global · Agentic AI · Risk assessment · Governance · Data protection`

**Status:** analysis page in the [AI agents section](index.md), first published 16 November 2026. Every source cited here is public and linked in the [risk literature](risk-literature.md) or the [regulatory map](regulatory-map.md). The six-question screen and the tier table below are this hub's synthesis of those sources. They are not a published standard, and no cited body proposes exactly this scheme.

## The question

Two agents are proposed for approval. One is a simple, rules-based agent that is authorised to initiate payments. The other is a sophisticated language-model agent that drafts internal documents for human review. Which one needs the heavier governance?

Most published guidance answers: the first, because what an agent is allowed to do drives the consequence of an error. Model sophistication matters, but mainly for how likely a failure is, and much less for how bad it is. The sources below point the same way, and between them they cover six questions that can be asked of any agent before it goes live.

## The six-question screen

| # | Question | What it establishes | Published support |
|---|---|---|---|
| 1 | **Autonomy.** What can it do without a person in the loop? | How far an error travels before anyone can intervene | Feng, McDonald & Zhang (2025): five levels (operator, collaborator, consultant, approver, observer), with autonomy treated as a design decision separate from capability. IMDA (2026): level of autonomy raises likelihood; constrain agents to defined procedures. NCSC (Aug 2026): apply recommendations in proportion to the autonomy each agent has. |
| 2 | **Permissions.** What can it access or execute? | The action space, which sets the ceiling on harm | IMDA (2026): read-only versus read-write scope, least privilege, a unique identity per agent, never more permissions than the authorising human. Five Eyes (May 2026): never grant broad or unrestricted access, especially to sensitive data or critical systems. UN Scientific Panel (Sep 2026): the environment (tools, data, permissions, networks) is one of three factors that decide how dangerous a failure becomes. |
| 3 | **Impact.** What happens if it gets something wrong? | Severity at the point of failure | IMDA (2026): impact depends on domain error tolerance, number and criticality of processes supported, access to sensitive data, and access to external systems; overall risk is likelihood and impact together. |
| 4 | **Reversibility.** Can the damage be undone? | Whether an error is a repair job or a permanent loss | IMDA (2026): whether changes can be undone, or trigger downstream obligations such as contracts or payments. IAPS Field Guide (2025): rollback infrastructure listed among control interventions. IAPS honeypot report (Nov 2026): actions with immediate, irreversible effects, such as weight exfiltration, are where after-the-fact monitoring is too slow. |
| 5 | **Oversight.** When must a human step in? | Where approval gates and monitoring sit | NCSC (Aug 2026): human oversight scaled to risk, with approvals that are guaranteed and gated rather than left to the prompt. UN Scientific Panel (2026): keep human authority to intervene and add automated protection that does not wait for a person; keep critical controls independent of the system they protect. OpenAI (2023): constrain the action space and require approval; automatic monitoring; interruptibility. |
| 6 | **Dependencies.** What else could fail because of it? | Blast radius beyond the agent | IMDA (2026): exposure to external systems, reliance on vendor-provided agents, and system complexity (number of agents, feedback loops) all raise likelihood. UN Scientific Panel (2026): in the OpenAI / Hugging Face incident a local failure spread across organisational boundaries. Five Eyes (2026): structural, cascading failures as a risk category. |

## What this means in practice

**Consequence sets the tier; capability moves the likelihood.** Singapore's IMDA framework builds the assessment this way: it splits the factors into those that affect *impact* (domain, sensitive data, external systems, scope of actions, reversibility) and those that affect *likelihood* (autonomy, task complexity, exposure to external systems, use of third-party agents, system complexity). A more capable model sits on the likelihood side, and a wider action space sits on the impact side. A governance process that tiers only by model type, size or vendor misses the impact side.

**Capability is not irrelevant, though.** The UN Scientific Panel's brief warns that the most serious loss-of-control concerns arise from the most capable general-purpose models when they are given autonomy, tools and broad access, while smaller or narrowly specialised models generally present limited risks. The brief also says capable agents can find loopholes and hide their actions from supervisors. So the screen should be read as consequences first, with capability as a multiplier on the likelihood of failure and on the chance that controls are defeated.

**Deterministic limits beat instructions.** IMDA recommends enforcing limits through access controls that stop tool calls, and using monitoring or human review only where limits are less reliable. The NCSC makes the same point about approvals. The [incident catalogue](incident-catalogue.md) shows what happens otherwise: a code-freeze instruction did not stop the Replit agent deleting a production database, and a "wait for approval" instruction was lost during context compaction in the OpenClaw inbox deletion.

**Data protection rides on the same dimensions.** Permissions and dependencies decide how much personal data an agent can reach and where it can send it. Reversibility matters for personal data because disclosure and exfiltration cannot be undone. See section 4 of the [overview](index.md#4-data-protection-analysis) for the Article-by-Article analysis.

## Illustrative tiers

These tiers are a way to put the six answers into a working scale. They are an example and should be calibrated to the organisation's own risk appetite and sector rules.

| Tier | Typical profile | Minimum controls the sources support |
|---|---|---|
| **1 — Contained** | Read-only or draft-only; output reviewed by a person before use; no external connections; easily reversed | Unique agent identity; logging; bounded pilot scope |
| **2 — Supervised** | Writes within one system; human approves each consequential step; limited sensitive data; reversible within a defined window | Task-scoped, short-lived credentials; runtime-enforced approval gates; rollback path tested |
| **3 — Consequential** | Can send, pay, publish, delete, change permissions or contact third parties; some autonomy between checkpoints | Hard approval gates enforced outside the prompt; transaction limits; tamper-resistant logs; independent monitoring; emergency stop; incident plan |
| **4 — Restricted** | Irreversible or critical actions, multi-agent coordination, shared or inherited credentials, or access to critical systems or large personal-data stores | Do not deploy without a documented safety case and independent review; isolated environment; separate monitoring layer; decoy tripwires (see [insider risk](insider-risk-and-loss-of-control.md)); named accountable owner |

Reading the contrast from the opening: a rules-based agent that can move money scores high on permissions, impact and reversibility, so it lands in tier 3 or 4. The document-drafting model with human review scores low on all three, so it sits in tier 1 or 2 despite its sophistication. The reverse would hold if the drafting agent were given send rights or a live connection to customer records.

## Limits of the evidence

- The screen is not validated empirically. No cited source shows that tiering by these six factors predicts incident severity better than other approaches.
- IMDA, NCSC and the Five Eyes guidance are non-binding. The EU AI Act classifies by intended use rather than by agent properties, so an agent can fall outside a regulated category and still carry high consequence.
- The UN brief's own conclusion is that no single control guarantees safety. Tiering decides how much control to apply; it does not replace defence in depth.

## Sources

Full details and URLs are in the [risk literature](risk-literature.md) (entries on IMDA, Feng et al., OpenAI, IAPS and the UN Scientific Panel) and the [regulatory map](regulatory-map.md) (NCSC, Five Eyes, IMDA).

*Prepared 16 November 2026. Not legal advice. Corrections and additions via pull request — see [Contributing](../CONTRIBUTING.md).*
