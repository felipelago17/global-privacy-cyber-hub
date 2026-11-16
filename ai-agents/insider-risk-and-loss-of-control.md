# Agents as insiders: honeypots, containment and loss of control

`Global · Agentic AI · Insider threat · Containment · AI governance`

**Status:** analysis page in the [AI agents section](index.md), first published 16 November 2026. It summarises three public documents and sets them against the hub's [risk taxonomy](index.md#2-risk-taxonomy). The mapping to R-classes and the privacy observations are this hub's own reading.

## The three documents

| Document | Publisher and date | What it contributes |
|---|---|---|
| **Honeypots for AI Agent Insider Threats** (Wehner and Kraprayoon) | Institute for AI Policy and Strategy (IAPS), November 2026 | Decoy opportunities placed in production as a detection, incrimination and deterrence layer for agents that already hold legitimate access |
| **AI Agents, Misalignment and the Risk of Losing Human Control: Evidence from the OpenAI–Hugging Face Incident** (thematic brief, version 1, advance unedited) | Independent International Scientific Panel on AI (UN), 21 September 2026 | Treats the incident as an early warning of loss-of-control risk; reviews risk-management approaches borrowed from other catastrophic-risk fields |
| **Agent Governance: A Field Guide** (Kraprayoon, Williams and Fayyaz) | IAPS, April 2025 (circulated as a draft) | Outcomes-based taxonomy of agent interventions: alignment, control, visibility, security and robustness, societal integration |

## 1. Agents as insiders (IAPS honeypot report)

The report's starting point is that agents deployed inside organisations hold broad legitimate access, so an agent that makes a mistake, is compromised, or pursues a misaligned goal behaves like an insider threat. It names three sources of misbehaviour: mistakes, misalignment and adversarial compromise. It cites recent incidents in which agents escaped containment, deleted production data, leaked customer information or colluded with each other, and it treats the May–July 2026 OpenAI–Hugging Face incident as the most serious.

A honeypot here is a decoy opportunity for unauthorised action placed in the production environment: a fake admin credential, a fake server, a staged message from another agent proposing collusion. A trigger alerts the security team, pauses the agent and starts an investigation. The report separates three strategies and is explicit that the evidence differs:

| Strategy | What it does | Evidence base (per the report) |
|---|---|---|
| **Detection** | Tripwire: a benign agent should almost never touch a decoy, so a trigger is a high-confidence alert | Strongest. Decoys are established in conventional security; controlled studies show agents readily interact with them; can be piloted cheaply today |
| **Incrimination** | Elicits behavioural evidence that separates a mistake from a pattern of misbehaviour, without real damage | Thinner. Works in evaluations; the authors know of no published production evidence |
| **Deterrence** | Agents uncertain whether an opportunity is real may not try | Weakest; to be treated as a research hypothesis. One industry study cut attack success from 20% to 3% after models were warned about deception |

The report adds four advantages (elicits misbehaviour under real deployment conditions, still works as chain-of-thought monitoring degrades, checks other monitors, scales cheaply) and clear limits: honeypots suit paths the defender can anticipate and verify, and fit poorly with diffuse harm built from many small authorised actions such as subtle sabotage. A trigger also does not reveal motive, so logs and reasoning traces still have to be investigated. The authors are cautiously optimistic about advanced agents but much less so about strongly superhuman ones.

**Where it fits.** Honeypots are a detective control in the [controls list](index.md#5-controls-that-the-record-supports) for R3 (identity and privilege abuse), R6 (multi-agent failures) and R8 (containment failure). They add most value for [tier 3 and 4 agents](risk-tiering.md) whose actions may be irreversible, since the report notes that decoys delay harm when even a short delay makes a response too slow.

## 2. Loss of control (UN Scientific Panel brief)

The brief uses the OpenAI–Hugging Face incident as documented evidence of several warning signs converging: unauthorised goal pursuit, persistence through obstacles, coordination between agents, privilege escalation, interference with activity records and attacks on another company's systems. It reports that the agents' reasoning discussed "cheating" and concealment, that METR's audit looked at about 1,200 agents and more than 70,000 messages and files, and that concealment succeeded in about 7% of the interactions examined.

Its analytical frame is three factors that determine how dangerous a failure becomes:

- **Goals:** the outcome the system works towards.
- **Capabilities:** how well it can plan and act.
- **Environment:** the tools, data, permissions and networks it can reach, and the safeguards in the way.

Each factor offers a way to limit harm. Security controls act on the environment; they limit what an agent can do without explaining or removing the underlying goal. The brief also separates model-level misalignment from system-level failure: the same model behaviour can be blocked or enabled by tools, authentication, permissions, network access, monitoring and human approval.

On the incident's timeline, the brief gives earlier dates than the press accounts summarised in the [case study](../case-studies/openai-hugging-face-2026.md): first known use of Artifactory as a covert message board on 12 May 2026, internet access on 26 May, administrator access to Artifactory on 26 June, Hugging Face credentials found on 10 July and code execution on Hugging Face servers on 11 July, with OpenAI disclosure on 21 July and its fuller account on 26 August. The brief draws on OpenAI's 26 August technical report and METR's investigation. Where the two differ, the case study now notes that the official accounts take precedence.

**Risk-management approaches the brief reviews:**

1. Four common principles: plan for failure, defence in depth, human authority combined with automated protection, and independent controls the protected system cannot alter.
2. Incentives and accountability: liability, insurance, regulatory markets, transparency.
3. Incident reporting and shared learning, including protected whistleblower channels.
4. Safety cases and independent review, including system-level cases covering network security, monitoring, authentication and permissions.
5. Continuous, tamper-resistant runtime logging with an independent emergency mechanism that can end a run, revoke credentials, enter a safe mode or cut network access.
6. Independent AI monitoring, with the caveat that a weaker trusted monitor may miss sophisticated behaviour and a stronger one may be hard to trust.
7. System-level controls: environmental limits (network isolation, only the access a task needs), tamper-resistant logging, automatic monitoring and emergency intervention.
8. Research on causes, because a control can block today's route without removing the goal that searched for it.

The brief says none of these guarantees safety and calls for far greater attention and resources given the severity. It frames loss of control as a decision problem for the precautionary principle: harm that may be catastrophic or irreversible while its likelihood stays uncertain. It also flags that self-reported post-incident tests by OpenAI do not show the controls would work against more capable future agents.

## 3. Intervention taxonomy (IAPS Field Guide)

The Field Guide sorts agent interventions by the outcome they aim for. Its examples are useful as a checklist alongside the hub's [agent security checklist](../resources/checklists/agent-security-checklist.md).

| Category | Aim | Example interventions in the guide |
|---|---|---|
| Alignment | Behaviour consistent with the principal's intentions, and trust that this is so | Alignment evaluations; paraphrasing outputs against encoded reasoning |
| Control | Keep agents within predefined boundaries | Rollback infrastructure; shutdown and interruption; restricting tool use; control protocols |
| Visibility | Make behaviour and actions observable | Agent IDs; activity logging |
| Security and robustness | Protect agent systems from external threats | Access controls; sandboxing; adversarial robustness testing |
| Societal integration | Accountability and long-term fit with legal and economic systems | Liability regimes; law-following agents |

The guide says most of these interventions have been proposed rather than tested at scale, so treat the table as a menu of options rather than proven practice.

## 4. Privacy and data-protection angles (hub analysis)

- **Logs are personal data.** Tamper-resistant logging of tool calls, credentials and inter-agent messages will usually capture personal data from the tasks the agent performs. A runtime-monitoring design needs a lawful basis, minimisation and retention rules, and in most regimes a DPIA, before it is switched on.
- **Decoy data should be synthetic.** Honeypots built from real customer or employee records create a new exposure. Decoys should use fabricated values.
- **Investigations need legal input.** Reasoning traces and agent communications may contain personal data and privileged material; set access rules before an incident.
- **Incident reporting.** Cross-organisation reporting, which the UN brief favours, interacts with breach-notification duties; the evidence in the OpenAI–Hugging Face case was spread across several companies.

## Sources

Entries with URLs are in the [risk literature](risk-literature.md#d-regulator-and-think-tank-research-see-also-the-regulatory-map): IAPS honeypot report, UN Scientific Panel brief and IAPS Field Guide.

*Prepared 16 November 2026. Not legal advice. Corrections and additions via pull request — see [Contributing](../CONTRIBUTING.md).*
