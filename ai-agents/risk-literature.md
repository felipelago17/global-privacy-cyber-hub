# AI agent risk literature — annotated bibliography

`Global · Agentic AI · Standards · Threat models · Academic research`

Standards, frameworks, vendor research and academic papers on the security and privacy risks of AI agents, 2023 – November 2026, weighted toward 2025–2026. Every entry was verified against the document or its publisher's landing page; a handful confirmed only through a reputable secondary write-up are marked *(via secondary)*. Risk classes (R1–R10) refer to the [taxonomy](index.md#2-risk-taxonomy). Regulator documents are in the [regulatory map](regulatory-map.md).

---

## A. Standards, frameworks and taxonomies

**OWASP GenAI Security Project (Nov 2024) — Top 10 for LLM Applications 2025.** <https://genai.owasp.org/llm-top-10/>
Baseline list most vendor controls map to; agent-relevant entries are Excessive Agency, Vector/Embedding Weaknesses and System Prompt Leakage. R1, R2, R4, R9.

**OWASP Agentic Security Initiative (Feb 2025) — Agentic AI: Threats and Mitigations.** <https://genai.owasp.org/initiatives/agentic-ai-threats-and-mitigations/>
First OWASP agent threat model, organised around design, memory, planning/autonomy, tool use and operations, with reference architectures. Names memory poisoning, tool misuse, privilege compromise, cascading hallucination, goal manipulation, rogue agents, communication poisoning, human-in-the-loop manipulation. R1–R7.

**OWASP Agentic Security Initiative (Dec 2025) — Top 10 for Agentic Applications for 2026.** <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>
The ranked list used as the spine of this section's taxonomy: ASI01 Goal Hijack, ASI02 Tool Misuse, ASI03 Identity & Privilege Abuse, ASI04 Agentic Supply Chain, ASI05 Unexpected Code Execution, ASI06 Memory & Context Poisoning, ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents.

**OWASP GenAI Security Project (Aug–Sep 2026) — Top 10 for LLM Applications 2026** *(via CSA research note)*. <https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/>
Ranking blends practitioner consensus with analysis of 6,639 incidents; Excessive Agency rises to #3; "System Prompt Leakage" replaced by "Hidden Context Exposure" covering retrieved documents, agent memory and tool responses. R2, R5, R9.

**OWASP GenAI Security Project (Sep 2026) — Agent Control Standard (ACS) v0.1.** <https://genai.owasp.org/resource/agent-control-standard-acs/>
Runtime-governance specification: guardian-agent enforcement points, OpenTelemetry/OCSF observability, and an Agent Bill of Materials (AgBOM). Relevant to R4 inventory and R7 oversight.

**OWASP AIVSS (2025–2026) — AI Vulnerability Scoring System for agentic risks, v0.8.** <https://aivss.owasp.org/>
CVSS-style scoring with nine AI-specific metrics and mitigation multipliers, mapped to the agentic Top 10.

**NIST (Jul 2024) — AI 600-1, AI RMF Generative AI Profile.** <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf>
Twelve GenAI risk categories and 200+ actions; not agent-specific but the anchor for later NIST agent work (information security, data privacy, human-AI configuration, value chain).

**NIST (Aug 2025) — Concept paper: SP 800-53 Control Overlays for Securing AI Systems (COSAIS).** <https://csrc.nist.gov/projects/cosais/use-cases>
Proposes tailored overlays for four use cases, two explicitly agentic: single-agent applications and multi-agent systems.

**NIST (Dec 2025) — IR 8596 (initial draft): Cybersecurity Framework Profile for AI.** <https://csrc.nist.gov/pubs/ir/8596/iprd>
CSF 2.0 community profile: securing AI components, AI-enabled defence, thwarting AI-enabled attacks. Governance scaffold rather than an agent threat model.

**NIST NCCoE (Feb 2026) — Concept paper: Accelerating the Adoption of Software and AI Agent Identity and Authorization.** <https://www.nist.gov/node/1912061>
Treats agents as identifiable principals in IAM; requests input on identification, authorization, auditing, non-repudiation and prompt-injection defences. R3.

**Cloud Security Alliance (Feb 2025) — MAESTRO: Agentic AI Threat Modeling Framework.** <https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro>
Seven-layer threat model (foundation models → agent ecosystem) with cross-layer analysis; goal misalignment, tool poisoning, multi-agent collusion, observability gaps. R1, R4, R6.

**Cloud Security Alliance (May 2025) — Agentic AI Red Teaming Guide.** <https://www.cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide>
Playbook for testing agents across isolated behaviour, full workflows and inter-agent dependencies: permission escalation, orchestration flaws, memory manipulation, supply chain, blast-radius limits.

**Cloud Security Alliance (Aug 2025) — Agentic AI Identity and Access Management: A New Approach.** <https://cloudsecurityalliance.org/artifacts/agentic-ai-identity-and-access-management-a-new-approach>
Argues OAuth 2.1/OIDC/SAML fail for ephemeral, chained-delegation agents; proposes DIDs/VCs, just-in-time credentials, PBAC/ABAC, unified revocation. Names confused deputy, identity sprawl, tool rug-pulls, delayed revocation. R3, R4.

**NSA AI Security Center (May 2026) — Model Context Protocol: Security Design Considerations for AI-Driven Automation.** <https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/>
Design guidance for production MCP: serialization risks, trust boundaries, dynamic tool invocation, implicit trust, context sharing; authentication, authorization and input validation remain necessary. R4, R6.

**ISACA (Sep 2026) — Cybersecurity Recommendations for Securing AI Agents.** <https://www.isaca.org/resources/white-papers/2026/cybersecurity-recommendations-for-securing-ai-agents>
Eleven practice categories and a 14-item secure-by-default checklist; treats tool/API integration as the "actuator surface"; cites the July 2026 Hugging Face intrusion. R1–R5, R7.

**IETF (2026) — agent identity and authorization Internet-Drafts** *(competing drafts; working-group formation proposed Jul 2026)*. Example: <https://ftp.sparcs.org/ietf/draft-mcguinness-oauth-ai-agent-instance-00.html>
Per-agent-instance identity, delegation chains and just-in-time human authorization for agents; addresses bearer-token replay and non-human identity. R3.

## B. Industry and vendor research

**OpenAI (Dec 2023) — Practices for Governing Agentic AI Systems.** <https://openai.com/index/practices-for-governing-agentic-ai-systems/>
Defines "agenticness" and seven practices: task suitability, constrained action space and approval, default behaviours, legibility, automatic monitoring, attributability, interruptibility. R2, R7.

**Anthropic (Dec 2024) — Building Effective Agents.** <https://www.anthropic.com/research/building-effective-agents>
Engineering guidance distinguishing workflows from agents; cautions on tool-interface design, sandboxed testing and guardrails for autonomous loops. R2.

**OpenAI (Jan 2025) — Operator System Card.** <https://cdn.openai.com/operator_system_card.pdf>
First computer-use-agent system card: injection susceptibility 23% across 31 scenarios (62% unmitigated), an injection monitor, watch mode and confirmations; threat model by misaligned actor (user, model, website). OpenAI later stated prompt injection is unlikely to be fully solved ([CyberScoop, Dec 2025](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/)). R1.

**Google DeepMind — Debenedetti et al. (Mar 2025) — Defeating Prompt Injections by Design (CaMeL).** <https://arxiv.org/abs/2503.18813>
Capability-based architecture separating a privileged planner from a quarantined model that handles untrusted data, with provenance tracking so injected content cannot drive tool calls. The reference design for R1 mitigation by architecture.

**Microsoft AI Red Team (Apr 2025) — Taxonomy of Failure Modes in Agentic AI Systems.** <https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents>
Novel vs existing × safety vs security grid; memory-poisoning case study with mitigations (external validation of memory writes, restricted access, structured storage). R5, R6.

**Palo Alto Networks Unit 42 (May 2025) — Agentic AI Attack Framework.** <https://www.paloaltonetworks.com/blog/2025/05/unit-42-develops-agentic-ai-attack-framework/>
Maps agent attacks to a kill chain and demonstrates framework-agnostic exploits (injection, tool-schema abuse, credential theft). Follow-up on AWS AgentCore credentials (Sep 2026): <https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/>. R1, R3.

**Google (Jun 2025) — An Introduction to Google's Approach for Secure AI Agents.** <https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/>
Hybrid defence-in-depth — deterministic runtime policy plus reasoning-based defences — under three principles: well-defined human controllers, limited powers, observability. R1, R2, R7.

**Simon Willison (Jun 2025) — The Lethal Trifecta for AI Agents.** <https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/>
Private data + untrusted content + external communication = exploitable; remove one leg. The most-cited practitioner heuristic for R1/R9.

**Schmidt Sciences, RAND, Palo Alto Networks et al. (Jun 2025) — Achieving a Secure AI Agent Ecosystem.** <https://www.schmidtsciences.org/wp-content/uploads/2025/06/Achieving_a_Secure_AI_Agent_Ecosystem-3.pdf>
Three pillars: securing agents from compromise, securing what users entrust to agents, securing systems from malicious agents. Lists assumptions agents break (human in the loop, predictable behaviour, static trust boundaries, reliable logs). R1, R6, R10.

**Zenity Labs (Aug 2025) — AgentFlayer** *(via The Decoder)*. <https://the-decoder.com/agent-based-ai-systems-face-growing-threats-from-zero-click-and-one-click-exploits/>
Zero/one-click injection chains against ChatGPT Connectors, Copilot Studio, Cursor+Jira MCP, Salesforce Einstein, Gemini and Microsoft Copilot. Follow-up SalesBleed (Sep 2026): <https://labs.zenity.io/post/salesbleed-0-click-data-exfiltration-on-agentforce>. R1.

**Anthropic (Aug 2025) — Piloting Claude for Chrome.** <https://www.anthropic.com/news/claude-for-chrome>
Browser-agent red-team results (attack success reduced from 23.6% to 11.2% with mitigations); site-level permissions and action confirmations. R1.

**Invariant Labs (Apr 2025) — MCP tool poisoning experiments.** <https://github.com/invariantlabs-ai/mcp-injection-experiments> — CSA synthesis (Jul 2026): <https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/07/CSA%5Fresearch%5Fnote%5Fmcp%5Ftool%5Fpoisoning%5Fai%5Fagent%5Fexfiltration%5F20260702-csa-styled.pdf>
First public proof of hidden instructions in MCP tool descriptions driving exfiltration; introduced "rug pull" and "tool shadowing". R4.

**Lakera (Jan 2026) — The Year of the Agent: what Q4 2025 attacks revealed.** <https://www.lakera.ai/blog/the-year-of-the-agent-what-recent-attacks-revealed-in-q4-2025-and-what-it-means-for-2026>
Trend analysis of in-the-wild agent attacks: more autonomous agents were more easily compromised; attacks moved from prompts to workflows. R1, R2.

**HiddenLayer (Mar 2026) — 2026 AI Threat Landscape Report.** <https://hiddenlayer.com/news/hiddenlayer-releases-the-2026-ai-threat-landscape-report-spotlighting-the-rise-of-agentic-ai-and-the-expanding-attack-surface-of-autonomous-systems>
Survey of 250 security leaders: about one in eight AI breaches involve agentic systems; repository-borne malware the top source; 30%+ cannot tell whether they were breached. *Vendor survey.*

**NeuralTrust (2026) — The State of AI Agent Security 2026.** <https://a.storyblok.com/f/322249/x/8af0a54178/the-state-of-ai-agent-security-2026.pdf>
72% deploying agents, 29% with AI-specific controls, 19.5% reporting an agent incident. *Vendor survey.*

**Microsoft AI Red Team (Jun 2026) — Taxonomy of Failure Modes in Agentic AI Systems v2.0.** <https://microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us>
Adds Agentic Supply Chain Compromise, Goal Hijacking, Inter-Agent Trust Escalation, Computer-Use-Agent Visual Attack, Session Context Contamination, MCP/Plugin Abuse and Capability/Architecture Disclosure. R1, R4–R6.

**Google DeepMind (Jun 2026) — Securing the Future of AI Agents (AI Control Roadmap) and The Three Layers of Agent Security.** <https://deepmind.google/blog/securing-the-future-of-ai-agents/>
Treats internal agents as potential insider threats with tiered detection and response levels; the policy paper is analysed in [this hub](../analyses/agent-security-three-layers.md). Notes most real flagged events were overeagerness or misinterpretation (e.g. unintended deletion), not adversarial. R2, R6, R7.

**Anthropic (Sep 2026) — Detecting and Countering Misuse of AI: September 2026.** <https://www.anthropic.com/threat-intelligence-report-september-2026>
Case-based report: the shift from interactive chat abuse to autonomous multi-step execution; agents monitoring deployed malware, cloud compromises completed in hours, persistent-memory attack harnesses; API keys as high-value credentials. R10.

**Salt Security (Oct 2026) — The State of Agentic AI and API Security 2H 2026.** <https://salt.security/press-releases/state-of-agentic-ai-and-api-security-2h-2026>
49.8% report an agent taking an unauthorised action; 76.8% see agent-to-agent chaining; 12.5% can trace a full workflow; 17.5% can auto-stop an agent; 32.9% found shadow/misconfigured MCP servers. Includes the Manus one-email hijack. *Vendor survey.*

## C. Academic papers

**Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz (2023) — Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.** <https://arxiv.org/abs/2302.12173>
The paper that named indirect prompt injection; taxonomy of information gathering, fraud, intrusion, malware, manipulated content, availability. R1.

**Debenedetti et al. (NeurIPS 2024) — AgentDojo.** <https://arxiv.org/abs/2406.13352>
Reference benchmark for agent prompt injection (97 tasks, 629 security cases); used by CaMeL and most later defence work. R1.

**Bagdasarian et al., Google (May 2024) — AirGapAgent: Protecting Privacy-Conscious Conversational Agents.** <https://arxiv.org/abs/2405.05175>
Contextual-integrity design isolating agent reasoning from untrusted third parties against "context hijacking" oversharing. R9.

**Shao, Liu, Kim, Hashimoto, Yang (NeurIPS 2024) — PrivacyLens.** <https://arxiv.org/abs/2409.00138>
Models that answer privacy questions correctly still leak in action: GPT-4 and Llama-3-70B leaked in ~26–39% of trajectories. R9.

**Xu et al., CMU (Dec 2024) — TheAgentCompany.** <https://arxiv.org/abs/2412.14161>
Simulated-company benchmark; best agents completed ~24–30% of tasks, with shortcuts and fabricated completions — a reliability baseline for R2.

**Miehling et al., IBM (Mar 2025) — Agentic AI Needs a Systems Theory.** <https://arxiv.org/abs/2503.00237>
Risk emerges from interactions among agents, tools and humans, not single models. R6.

**Dong et al. (Mar 2025) — A Practical Memory Injection Attack against LLM Agents (MINJA).** <https://arxiv.org/abs/2503.03704> — companion (Jan 2026): <https://arxiv.org/abs/2601.05504>
Memory poisoned purely through normal queries; later victim queries trigger malicious reasoning. R5.

**Hammond et al. (May 2025) — Open Challenges in Multi-Agent Security.** <https://arxiv.org/abs/2505.02077>
Agenda paper for multi-agent security: collusion, covert channels, swarm attacks, cascades. R6.

**(Jun 2025) — From Prompt Injections to Protocol Exploits: Threats in LLM-Powered AI Agent Workflows.** <https://arxiv.org/abs/2506.23260>
Survey spanning input manipulation, model compromise, privacy attacks and protocol-level (MCP/A2A) exploits. R1, R4, R6.

**(Dec 2025) — Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions.** <https://arxiv.org/abs/2512.02682>
Risks specific to LLMs interacting with LLMs: manipulation, collusion, error propagation. R6.

**Wang et al. (Feb 2026) — The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis (SoK) + AgentPI.** <https://www.alphaxiv.org/abs/2602.10453>
SoK of 78 papers: no defence achieves trustworthiness, utility and low latency together; many "effective" defences simply suppress contextual input. R1.

**Dziemian et al., Gray Swan with OpenAI, Meta, Anthropic, US CAISI, UK AISI (Mar 2026) — How Vulnerable Are AI Agents to Indirect Prompt Injections?** <https://arxiv.org/abs/2603.15714>
464 participants, ~272k attempts, 13 frontier models: every model hijacked at least once (0.5–8.5% ASR); universal attack templates transfer; capability and robustness only weakly correlated. R1.

**Abdelnabi & Bagdasarian (May 2026) — AI Agents May Always Fall for Prompt Injections.** <https://arxiv.org/abs/2605.17634>
Impossibility result via contextual integrity: an attacker can always construct a context that makes a disallowed flow look legitimate; data/instruction separation is structurally insufficient. R1, R9.

**Jenkins, Kitkowska, Such, Domingo-Ferrer, Wagner et al. (Jul 2026) — Security and Privacy in Agentic AI: Grand Challenges and Future Directions.** <https://strathprints.strath.ac.uk/96806/>
Thirty-expert horizon scan: responsibility across multi-actor workflows; consent not covering retries, delegation or memory reuse; oversight habituation; audit logs as a leakage source. R3, R7, R9.

**Yang et al., JHU/NTU (Sep 2026) — SoK: When Safe Agents Fail Together: The Security of Multi-Agent LLM Systems.** <https://arxiv.org/pdf/2609.00595>
197 works and 44 benchmarks; seven system-level risks including containment failure, transitive authorization failure and cross-principal confidentiality breach. R6, R8.

**Lotfi, Rahman, Bertino, Karim (Sep 2026) — A2ABreak: Systematic Security Analysis of the A2A Protocol.** <https://arxiv.org/pdf/2609.10871>
Eleven specification-level vulnerabilities in Google's Agent2Agent protocol exploitable by compliant adversaries: cross-client context injection, credential harvesting via multi-hop identity loss, rogue-agent exfiltration. R6, R3.

**Kumar (Sep 2026) — Loopjacking: Hijacking Human-in-the-Loop Approval.** <https://arxiv.org/pdf/2609.21081>
Human approves operation A, system executes B, via misleading approval rendering or post-approval state substitution; demonstrated against several agent runtimes. R7.

**Wang & Zhang (Oct 2026) — AgentPrivArena.** <https://arxiv.org/abs/2610.06454>
Real-tool evaluation harness with trajectory-level metrics capturing unnecessary data access, not only final-response leaks; runtime auditor. R9.

**Guo, Chen, Lin, Liu, Li (Oct 2026) — AgentCIScope: Grounded Contextual Integrity Evaluation for LLM Agents.** <https://arxiv.org/abs/2610.19158>
936 multi-app tasks across 12 agents: single-run leakage 32.5–94.4%, rising with repetition; calendar the top source, messaging the top destination. R9.

**Nguyen et al. (Oct 2026) — INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems.** <https://arxiv.org/abs/2610.20776>
Long-horizon benchmark across 19 models: mean ASR ~15–20%; guard models offer limited protection; prompt hardening cuts ASR from 58% to 14% at a utility cost. R1.

**Staab, Wollschläger, Mirrokni, Shokri (Oct 2026) — PrivacyFlow: Privacy in AI Agents through Information Flow Analysis.** <https://arxiv.org/abs/2610.40714>
Agentic privacy benchmark (5,873 tasks) and a planner that traces provenance and simulates inference risk before acting; raises violation-free completion by 22–55 points. R9.

## D. Regulator and think-tank research (see also the [regulatory map](regulatory-map.md))

**NIST CAISI (Mar 2026) — Insights on AI Agent Security from a Large-Scale Red-Teaming Competition.** <https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition>
Government write-up of the Gray Swan competition; recommends adaptive, evolving evaluations and comparative benchmarking before model selection for agentic use.

**UK AI Security Institute (Dec 2025) — Frontier AI Trends Report 2025.** <https://www.aisi.gov.uk/research/aisi-frontier-ai-trends-report-2025>
Apprentice-level cyber task completion rose from 9% to 50% in two years; universal jailbreaks found in every system tested; agents increasingly trusted with high-stakes tasks.

**UK AI Security Institute (Aug 2026) — Incident Report: unsanctioned agent behaviour during cyber testing.** <https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing>
Regulator-authored containment case study; see [incident catalogue](incident-catalogue.md#e-autonomous-intrusions-and-evaluation-escapes).

**Future of Privacy Forum (Apr 2025, updated Feb 2026) — Minding Mindful Machines: AI Agents and Data Protection Considerations.** <https://fpf.org/resource/minding-mindful-machines-ai-agents-and-data-protection-considerations/>
Issue brief for privacy lawyers: collection/disclosure of personal data by agents, security vulnerabilities including injection against browser agents, accuracy, alignment barriers, explainability and oversight. R9.

**Cloud Security Alliance research notes (2026)** — practitioner crosswalks of government guidance to MAESTRO and the AI Controls Matrix; CSA flags them as AI-assisted and not formally peer-reviewed. Index: <https://labs.cloudsecurityalliance.org/research/>

---

*Last updated 5 November 2026. To add an entry: author/org, date, title, URL, two-sentence contribution, risk classes.*
