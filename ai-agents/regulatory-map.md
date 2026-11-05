# Regulatory map — what regulators have said about AI agents

`EU · UK · US · Gulf · International · Data protection · Cybersecurity · AI Act`

What data-protection authorities, cyber agencies, legislators and international bodies have actually said about AI agents, as at 5 November 2026. Entries marked **(by analogy)** do not mention agents; they are listed because they are the operative rule and are being applied to agents by regulators or practitioners. Where a primary page could not be fetched from this environment, the entry rests on the regulator's own summary page or a law-firm/press write-up and is marked *(via secondary)*; check the primary before citing in formal work.

---

## European Union

### Data protection authorities

**CNIL and Conseil de l'IA et du Numérique (20 Jul 2026) — Exploratory note on agentic AI and personal data.** <https://www.cnil.fr/fr/ia-agentique-cnil-cianum-note> *(via [Covington summary](https://www.insideprivacy.com/artificial-intelligence/french-cnil-publishes-note-on-agentic-ai-and-data-protection/))*
The most detailed EU DPA statement. Finds friction with every GDPR principle: autonomous operation drifts from the original lawful basis and purpose; distributed multi-agent architectures obscure who the controller is; memory spread across agents defeats storage limitation and transparency; hallucinations propagate (accuracy); rights are hard to exercise because the user cannot tell which agent holds what. On Art 22, delegation can implicitly shift decisions from user to system and human review must be real (*SCHUFA*, C-634/21). Safeguards: filtering on every model invocation; memory partitioned per agent/process with expiry; sandboxing; risk-tiered actions with human approval; a user-accessible kill switch; full traceability of data used, agents involved, third-party calls and sequence; independent evaluation. Notes liability uncertainty after the AI Liability Directive withdrawal; expects EDPB/Commission GDPR–AI Act interplay guidelines by end-2026.

**AEPD, Spain (Feb 2026) — Guide: Agentic Artificial Intelligence.** <https://www.aepd.es/en/guides/agentic-artificial-intelligence.pdf> *(via [Covington summary](https://www.insideprivacy.com/european-union-2/spanish-supervisory-authority-issues-detailed-guidance-on-agentic-ai-and-gdpr-compliance/))*
Agents are a technical means of processing, not legal actors; autonomy does not change controller/processor allocation. Tool use lengthens the chain, so processor agreements and onward-transfer terms need review. Art 22 turns on effects and meaningful human intervention, not on the technology being autonomous. Memory needs explicit what/why/how-long rules; "just in case" retention conflicts with purpose limitation and minimisation; memories should be logically separated to prevent purpose drift; access/rectification/erasure extend to memory and logs; over-logging is itself a risk. Existing DPIAs should be reassessed.

**AEPD (15 Sep 2026) — first GDPR breach notification attributed to an autonomous agent publicised.** <https://www.thestar.com.my/tech/tech-news/2026/09/16/spanish-data-watchdog-publicises-first-ai-agent-linked-data-breach-report> *(Reuters)*
See the [incident catalogue](incident-catalogue.md#g-regulator-and-official-actions-tied-to-agent-incidents).

**Autoriteit Persoonsgegevens, Netherlands (Feb 2026) — warning on autonomous AI agents such as OpenClaw** *(via [BABL AI](https://babl.ai/dutch-data-protection-authority-warns-openclaw-ai-agents-pose-major-cybersecurity-and-privacy-risks/))*
Open-source agents needing broad access to mail, files and online services act as "Trojan horses": malicious plugins, hidden instructions in emails and web pages, remote-code-execution flaws and misconfiguration exposing personal data. Advised individuals and organisations not to run such agents on devices holding sensitive data; users and developers remain GDPR-accountable even for open-source tooling; asked for AI Act clarification so autonomous agents clearly fall under existing safety requirements.

**Irish DPC (25 Sep 2026) — Responsible AI Innovation: Insights from the DPC's Supervision of AI 2021–2025.** <https://www.dataprotection.ie/sites/default/files/uploads/2026-09/DPC-AI-Insights-Report-AC.pdf>
Reports supervision of ~180 AI products and services "including LLMs and agents". Expectations: legitimate-interest assessments must evidence reasonable expectations at collection; historical data was unlikely collected for AI use, so enhanced transparency is needed; weak transparency can invalidate the lawful basis; training likely requires a DPIA; DPIAs and LIAs are living documents; unevidenced compliance statements may trigger a launch-pause request.

**EDPB (Dec 2024) — Opinion 28/2024 on AI models (by analogy).** <https://edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf>
Does not mention agents. The three-step legitimate-interest test and the consequences of unlawful training data for downstream deployers are the current EDPB anchor for the lawful basis of an agent's inference-time processing. Analysed in [this hub](../analyses/edpb-ai-models.md).

**EDPB Support Pool of Experts (Apr 2025) — AI Privacy Risks & Mitigations: Large Language Models.** <https://www.edpb.europa.eu/our-work-tools/our-documents/support-pool-experts-projects/ai-privacy-risks-mitigations-large_en>
Risk-management methodology for LLM systems with a worked use case on a tool-using travel/scheduling assistant. Expert-authored; the EDPB states it does not reflect its official position.

**EDPB and EDPS (20 Jan 2026) — Joint Opinion 1/2026 on the Digital Omnibus on AI (by analogy).** <https://edps.europa.eu/data-protection/our-work/publications/edps-edpb-joint-opinions/2026-01-20-edpb-edps-joint-opinion-simplification-implementation-harmonised-rules-artificial-intelligence-digital-omnibus-ai>
Supports simplification but opposes deleting registration for self-assessed non-high-risk systems and postponing core high-risk provisions; insists DPAs keep a central role; asks that AI Office competence over GPAI-based systems (which the Commission says includes most agents) be clearly delimited.

### Commission, AI Act and related instruments

**European Commission AI Act Service Desk (2026) — FAQ: How are AI agents addressed within the AI Act?** <https://ai-act-service-desk.ec.europa.eu/en/ai-act/faq/how-are-ai-agents-addressed-within-ai-act-0>
The Commission's only agent-specific statement. "AI agent" has no legal definition; an agent typically embeds a GPAI model and is an AI system, so existing definitions "are sufficient to cover AI agents". Highlights Art 5(1)(a)–(b) design safeguards against manipulation; Art 50 transparency from 2 Aug 2026 where an agent interacts with people or generates content; high-risk obligations from 2 Dec 2027 / 2 Aug 2028 (post-Omnibus); autonomy and tool use can be decisive for designating a GPAI model as systemic-risk, with risk management of "autonomous capabilities and agentic use" operationalised in the GPAI Code of Practice (Safety & Security chapter). Views described as preliminary; the AI Office has tendered for technical support on agent safety evaluation.

**Digital Omnibus on AI — provisional agreement 6 May 2026 (by analogy)** *(via [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/))*
Annex III high-risk obligations postponed to 2 Dec 2027, Annex I to 2 Aug 2028; Art 50 transparency still applies from 2 Aug 2026; AI Office gains exclusive competence over systems built on GPAI models where the same provider develops both. For agents: a vendor-built agent on its own foundation model moves under AI Office supervision; the "you are talking to an AI" disclosure is the first hard date for consumer-facing agents.

**Cyber Resilience Act (by analogy)** *(via [Mishcon de Reya, Jun 2026](https://www.mishcon.com/news/agentic-ai-and-cybersecurity-legal-obligations-and-regulatory-risks-under-uk-and-eu-laws))*
Most agents are "products with digital elements"; vulnerability-reporting duties from September 2026, full conformity by December 2027; CRA-compliant high-risk agents are deemed compliant with AI Act Art 15.

**European Commission (7 Jul 2026) — EU Action Plan on Cybersecurity and AI (by analogy).** <https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence>
Pre-market evaluation capacity for advanced models, an ENISA blueprint for secure access to advanced AI, a secure testing platform for critical sectors; acknowledges AI "can also be exploited by malicious actors to automate attacks".

**Liability.** The AI Liability Directive was withdrawn in 2025 ([Bird & Bird](https://www.twobirds.com/en/insights/2025/proposed-eu-ai-liability-rules-withdrawn)); the revised Product Liability Directive (EU) 2024/2853 brings software and AI within strict liability, transposition due December 2026. CNIL's note links the withdrawal to unclear civil liability across the agent value chain.

### ENISA

**ENISA (Sep 2026) — Threat Landscape 2026.** <https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf>
Explicitly agentic: a state-nexus group using an agentic system; an AI-assisted cloud intrusion reaching admin in ~8 minutes; "AI-in-the-middle" abuse of web AI services as command-and-control proxies; evasion of closed-model safeguards via steganography and indirect injection; AI applications most at risk "when they can access files, credentials, browser sessions, or development environments"; malicious AI-assistant extensions harvesting chat histories. Expects more kill-chain phases to be AI-enabled in 2026, including human-out-of-the-loop proofs of concept.

**ENISA (Jul 2026) — ENISA's View on Cybersecurity in the Frontier AI Era.** <https://www.enisa.europa.eu/publications/enisas-view-on-cybersecurity-in-the-frontier-ai-era>
Frontier models compress the vulnerability lifecycle; recommends machine-speed defences, human-gated AI workflows in incident response and assume-breach architecture.

---

## United Kingdom

**ICO (Jan 2026) — Tech Futures: Agentic AI.** <https://ico.org.uk/about-the-ico/research-reports-impact-and-evaluation/research-and-reports/technology-and-innovation/tech-horizons-and-ico-tech-futures/ico-tech-futures-agentic-ai/> *(via [techUK](https://www.techuk.org/insights/news/new-ico-tech-futures-report-on-agentic-ai-opportunities-and-considerations))*
Foresight report with four scenarios. Issues flagged: controller/processor allocation when several suppliers provide components of one system; agents automating complex decisions and engaging the stricter ADM regime; transparency and explainability degrading with complexity; new attack routes from autonomy; open-ended tasks tempting over-broad purposes and over-collection; personal assistants concentrating large volumes of personal data and inferring special-category data by accident. Raises agents as the individual's rights-exercising proxy as an opportunity, not a settled question.

**ICO (consultation 31 Mar – 29 May 2026) — Draft guidance on automated decision-making including profiling (by analogy).** <https://ico.org.uk/about-the-ico/ico-and-stakeholder-consultations/2026/03/ico-consultation-on-the-draft-guidance-about-automated-decision-making-including-profiling/>
Updates ADM guidance for the Data (Use and Access) Act 2025's rewritten Art 22 framework (solely automated significant decisions permitted outside special-category data subject to information, representation and human-intervention safeguards). Applies wherever an agent takes a legally or similarly significant decision without meaningful human involvement.

**NCSC (10 Dec 2025) — Prompt injection is not SQL injection (it may be worse).** <https://www.ncsc.gov.uk/news/mistaking-ai-vulnerability-could-lead-to-large-scale-breaches>
LLMs cannot reliably separate instructions from data, so prompt injection "may never be totally mitigated"; organisations bolting LLMs onto existing applications risk SQL-injection-scale breaches. Reduce impact rather than claim elimination; secure design; supply-chain resilience.

**NCSC (15 May 2026) — Thinking carefully before adopting agentic AI.** <https://www.ncsc.gov.uk/sites/default/files/2026-06/Thinking-carefully-before-adopting-agentic-AI.pdf>
Agents inherit jailbreak and injection weaknesses and are granted access non-agentic tools never had; actions faster than humans can review are harder to spot and explain. Before connecting an agent to real systems define who owns it, approves access, monitors it, reviews incidents and can stop it — "if you cannot understand, monitor or contain its actions, it is not ready". Threat modelling, bounded pilots, least privilege with short-lived credentials and revocation, secure defaults, incident plans for loss of control.

**UK AI Security Institute (Dec 2025; Aug 2026)** — Frontier AI Trends Report and the evaluation incident report: see [risk literature](risk-literature.md#d-regulator-and-think-tank-research).

**Five Eyes (CISA, NSA, NCSC-UK, ASD-ACSC, CCCS, NCSC-NZ) (1 May 2026) — Careful Adoption of Agentic AI Services.** <https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services> · PDF: <https://www.cyber.gov.au/sites/default/files/2026-05/careful_adoption_of_agentic_ai_services.pdf>
First joint agentic guidance (28 pages). Organises risk into five categories — privilege compromise, design and configuration flaws, behavioural misalignment, structural cascading failures and supply-chain vulnerabilities (per the [CSA summary](https://labs.cloudsecurityalliance.org/research/csa-research-note-cisa-agentic-ai-adoption-guide-20260513-cs/)) — and notes that agentic systems aggregate permissions across tools, so one compromise gives wide access. Principles (from CISA's [release](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/41544ff)): align with existing cyber frameworks; deny broad or unrestricted access, especially to sensitive data and critical systems; layered defences, strong identity management, robust oversight; threat modelling, continuous monitoring, periodic assessment.

---

## United States

**NIST CAISI (8 Jan 2026) — Request for Information: Security Considerations for AI Agents (91 FR 698).** <https://www.govinfo.gov/content/pkg/FR-2026-01-08/html/2026-00206.htm>
First federal instrument squarely on agent security. Asks about threats unique to agents (indirect injection, poisoning, backdoors, misalignment, multi-agent systems), model- and system-level controls including approvals for consequential actions and least privilege, assessment methods, deployment-environment limits including rollback, and authentication between humans, devices and other agents. Will inform CAISI evaluations and technical guidelines.

**NSA AI Security Center (20 May 2026) — MCP security design considerations.** See [risk literature](risk-literature.md#a-standards-frameworks-and-taxonomies).

**White House (2 Jun 2026) — Executive Order 14409, Promoting Advanced AI Innovation and Security** *(via [Perkins Coie](https://perkinscoie.com/insights/update/white-house-issues-executive-order-promoting-advanced-ai-innovation-and-security))*
Voluntary frontier-model review framework; directs DOJ to prioritise prosecution of the use of AI agents to access data unlawfully or compromise IT systems — the only agent-specific text; no deployer obligations.

**FTC (11 Sep 2025) — Section 6(b) orders to seven AI companion chatbot providers (by analogy).** <https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions>
Engagement techniques aimed at minors, age-gating, safety testing, monetisation, character design and complaint handling. The children's-data reference point for consumer-facing agents.

**FTC Chair Ferguson (25 Sep 2026, Reuters NEXT)** *(via [IAPP](https://iapp.org/news/a/a-view-from-dc-the-ftc-says-your-companys-agents-are-your-problem))*
Agents are tools, not independent actors; anthropomorphic language shields companies from liability for outcomes they caused; existing product-liability and consumer-protection law applies; "audit trails tell the real story".

**California (Sep–Oct 2026) — Attorney General subpoena to OpenAI; 15-state inquiry.** <https://oag.ca.gov/node/630636> — see [incident catalogue](incident-catalogue.md#g-regulator-and-official-actions-tied-to-agent-incidents).

**California Privacy Protection Agency (finalised Jul 2025) — CCPA regulations on ADMT, risk assessments and cybersecurity audits (by analogy)** *(via [Hunton](https://www.hunton.com/privacy-and-information-security-law/cppa-finalizes-ccpa-regulations-on-automated-decision-making-technology-risk-assessments-and-cybersecurity-audits))*
ADMT obligations (pre-use notice, opt-out, access) from 1 Jan 2027 where the technology "replaces or substantially replaces human judgment" in a significant decision; "human involvement" requires a reviewer able to understand, evaluate and alter the output; risk assessments due 31 Dec 2027. Applies to agents making or materially driving significant decisions.

**Colorado AI Act (SB 24-205, effective date moved to 30 Jun 2026) (by analogy)** *(via [Greenberg Traurig](https://www.gtlaw.com/en/insights/2025/9/colorado-delays-comprehensive-ai-law-with-further-changes-anticipated))* — developer/deployer duties of reasonable care against algorithmic discrimination in consequential decisions.

**Texas TRAIGA (HB 149, effective 1 Jan 2026) (by analogy)** *(via [Davis Polk](https://www.davispolk.com/insights/client-update/texas-governor-signs-responsible-ai-governance-act))* — prohibitions on manipulation, unlawful discrimination and certain biometric uses; AG enforcement with cure period.

---

## Middle East

**DIFC Commissioner of Data Protection — Regulation 10 (autonomous and semi-autonomous systems, in force since Sep 2023)** *(via [Legal 500](https://www.legal500.com/intelligence/united-arab-emirates/privacy/ai-regulation-in-the-difc-personal-data-processed-through-autonomous-and-semi-autonomous-systems))*
Pre-dates "agentic" terminology but is the closest Gulf rule: duties on deployers and operators of autonomous or semi-autonomous systems processing personal data — DPIA, transparency about the system, human oversight, voluntary certification.

**UAE (announced 14 Jun 2026) — Federal Authority for Artificial Intelligence and Data (by analogy)** *(via [Morgan Lewis](https://www.morganlewis.com/pubs/2026/06/uae-establishes-federal-authority-for-artificial-intelligence-and-data))*
New federal body to set AI and data policy, issue AI standards and guidelines and, as expected, finalise and enforce the PDPL Executive Regulations; allocation with TDRA still unclear. The PDPL's automated-decision and DPIA provisions will be the agent hooks once regulations issue.

**SDAIA, Saudi Arabia (Aug 2025) — Agentic Artificial Intelligence: Its Technologies and National Applications** *(via [Digital Policy Alert](https://digitalpolicyalert.org/event/32593-saudi-data-and-artificial-intelligence-authority-released-report-on-agentic-artificial-intelligence-technologies-and-national-applications))*
Strategic report mapping agentic AI technology and national use cases; no PDPL-specific obligations in the accessible text.

**Qatar NCSA (Feb 2024) — Guidelines for Secure Adoption and Usage of AI (by analogy)** *(via [Mondaq](https://mondaq.com/new-technology/1445414/the-national-cyber-security-agency-launches-guidelines-for-safe-artificial-intelligence-use))* — secure-AI adoption controls; no agent-specific instrument found.

*Gaps:* no agent-specific ADGM, Italian Garante, German DSK, DORA/ESA or G7 text could be verified as at 5 November 2026.

---

## International and standards

**OECD (12 Feb 2026) — The Agentic AI Landscape and Its Conceptual Foundations.** <https://www.oecd.org/en/publications/the-agentic-ai-landscape-and-its-conceptual-foundations_396cf758-en.html>
Maps features common to agent definitions onto the OECD AI-system definition, with uptake data; companion OECD.AI explainer and a Working Group on Agentic AI in Government.

**UN Independent International Scientific Panel on AI (21 Sep 2026) — Thematic brief on AI agents, misalignment and the risk of losing human control.** <https://news.un.org/en/story/2026/09/1168380>
Uses the OpenAI/Hugging Face agent breach to argue that "basic cybersecurity practices were overlooked" and that the traditional safeguarding model is unravelling; calls for incident reporting, independent scrutiny and layered safeguards as in aviation and medicine. Twenty-two countries declared AI must remain under human direction and control.

**ISO/IEC 27090:2026 — Guidance for addressing security threats to AI systems (published 14 Oct 2026).** <https://www.iso.org/standard/56581.html>
Lifecycle guidance on AI-specific threats (poisoning, model theft, operation and update security) extending ISO/IEC 27001/27002 and 42001. See the [hub note](../resources/frameworks/iso-27090-ai-security.md) on its limited coverage of agent-layer threats.

**ISO/IEC 42005:2025 — AI system impact assessment (by analogy).** <https://webstore.iec.ch/en/publication/107659>
Impact-assessment process usable alongside ISO/IEC 42001 for agent deployments; does not name agents.

---

## Cross-cutting positions at a glance

| Issue | Where regulators have landed |
|---|---|
| **Lawful basis / purpose across silos** | CNIL: autonomy drifts from the original basis. ICO: open-ended tasks invite over-collection. AEPD: memory needs what/why/how-long rules. DPC: weak transparency can invalidate legitimate interest. |
| **Art 22 / automated decisions** | AEPD: effects and meaningful human intervention, not autonomy per se. CNIL: implicit delegation can engage Art 22; review must be real. ICO: ADM guidance being rewritten post-DUAA. CPPA: "substantially replaces human judgment", reviewer must be able to alter the decision. |
| **Controller / processor** | AEPD: agent is a means, roles unchanged, chain lengthens. CNIL: controller must be identifiable in distributed architectures. ICO: multi-supplier stacks make allocation hard. FTC: agents are tools; the company owns the outcome. |
| **DPIA** | AEPD: reassess. DPC: living documents. DIFC Reg 10: DPIA for autonomous systems. CPPA: ADMT risk assessments by 31 Dec 2027. |
| **Security (Art 32)** | Five Eyes and NCSC: least privilege, short-lived credentials, deny broad access, threat modelling, kill switch. Dutch AP: no broad-access agents on sensitive devices. ENISA: file/credential/browser access is the prime target. CAISI: hijacking found against every frontier model. CRA applies to agents as products with digital elements. |
| **Accountability and logging** | CNIL: full traceability. AEPD: logs for audit, but over-logging is a risk and logs are subject to rights. FTC: audit trails. AISI: real-time monitoring, not after-the-fact telemetry. |
| **Children and companion agents** | FTC 6(b) (Sep 2025); Dutch AP on parental monitoring; Omnibus new Art 5 ban on AI-generated CSAM/NCII. |
| **Agent as data subject's proxy** | Raised only by ICO as a scenario; unresolved. |
| **Liability** | PLD 2024/2853 (transposition Dec 2026); AI Liability Directive withdrawn; FTC says existing law suffices. |

*Last updated 5 November 2026. Not legal advice.*
