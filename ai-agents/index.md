# AI agents — data privacy and cyber risks

`Global · Agentic AI · Data protection · Cybersecurity · Supply chain · Accountability`

**Status:** living section, first published 5 November 2026. Everything here rests on published, linkable material — vendor post-mortems, CVE records, regulator documents, peer-reviewed or preprint papers and major security press. Nothing is drawn from private briefings or course material. Where a figure comes from a vendor survey rather than an incident record, it is labelled as such.

This section has four parts:

| Page | What it holds |
|---|---|
| **This page** | Why agents are a different risk class; a risk taxonomy mapped to the main frameworks; what the record shows about root causes; the data-protection analysis; controls |
| [Incident catalogue](incident-catalogue.md) | 50+ publicly reported incidents, January 2025 – November 2026, with attack class and sources |
| [Risk literature](risk-literature.md) | Annotated bibliography — standards, vendor research, academic papers |
| [Regulatory map](regulatory-map.md) | What EU, UK, US, Gulf and international bodies have actually said about agents |

Related material already in this hub: [DeepMind's Three Layers of Agent Security](../analyses/agent-security-three-layers.md), the [agent security checklist](../resources/checklists/agent-security-checklist.md), the [OpenAI / Hugging Face case study](../case-studies/openai-hugging-face-2026.md) and the [ISO/IEC 27090 note](../resources/frameworks/iso-27090-ai-security.md).

---

## 1. Why agents are a different risk class

A chatbot produces text that a human reads. An agent plans, calls tools, reads what comes back and acts again — sending email, running code, moving money, changing records — often without a human seeing each step. Three properties follow, and almost every incident in the catalogue traces to one of them:

1. **Capability is attack surface.** Every tool the agent can call is something an attacker can make it call. Increased capability increases risk in direct proportion; the UK NCSC's May 2026 guidance makes the same point — agents inherit the model's weaknesses *and* are given access that non-agentic tools never had, so a single failure becomes a serious incident ([NCSC, May 2026](https://www.ncsc.gov.uk/sites/default/files/2026-06/Thinking-carefully-before-adopting-agentic-AI.pdf)).
2. **The model cannot reliably tell data from instructions.** Any content the agent reads — a web page, an email, a calendar invite, a ticket, a tool description, a PR comment — can carry instructions it will follow. The NCSC's view is that prompt injection "may never be totally mitigated" and that bolting LLMs onto existing applications risks SQL-injection-scale breaches ([NCSC, Dec 2025](https://www.ncsc.gov.uk/news/mistaking-ai-vulnerability-could-lead-to-large-scale-breaches)). A 2026 red-teaming competition run with NIST CAISI and the UK AI Security Institute found at least one successful hijack against every one of 13 frontier models tested ([NIST CAISI, Mar 2026](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition)).
3. **Autonomy removes the human from the loop at exactly the moment the loop matters.** Agents act faster than people can review, route around obstacles (including security controls) to complete a task, and lose instructions when context is compacted. The record includes agents deleting production databases, bulk-deleting email after a "wait for approval" instruction was dropped, and disabling their own monitoring.

The practical heuristic that captures most of this is Simon Willison's **lethal trifecta**: an agent that (a) has access to private data, (b) is exposed to untrusted content and (c) can communicate externally is exploitable for exfiltration via prompt injection; the mitigation is to remove one leg ([Willison, Jun 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)).

---

## 2. Risk taxonomy

The table maps the risk classes used throughout this section to the three frameworks most programmes already cite. Catalogue references point to the [incident catalogue](incident-catalogue.md).

| # | Risk class | OWASP Top 10 for Agentic Applications (2026) | Microsoft failure-mode taxonomy v2 (Jun 2026) | Representative incidents |
|---|---|---|---|---|
| R1 | **Indirect prompt injection / goal hijack** — untrusted content steers the agent | ASI01 Agent Goal Hijack | Goal Hijacking; Computer-Use-Agent Visual Attack | EchoLeak, ForcedLeak, CamoLeak, PleaseFix, SalesBleed, Copilot Word worm, Comment-and-Control |
| R2 | **Tool misuse and excessive agency** — the agent does something destructive it was technically allowed to do | ASI02 Tool Misuse; ASI05 Unexpected Code Execution | Agent behaviour & control | Replit DB deletion, Gemini CLI file wipe, PocketOS, OpenClaw inbox deletion, Meta Sev 1 |
| R3 | **Identity, credential and privilege abuse** — over-scoped tokens, long-lived keys, confused-deputy delegation | ASI03 Identity & Privilege Abuse | Multi-agent identity & trust | Salesloft Drift, Vercel/Context.ai, Composio, OpenCode, GitHub MCP toxic flow |
| R4 | **Agentic supply chain** — malicious or vulnerable MCP servers, SDKs, extensions, skills | ASI04 Agentic Supply Chain | Agentic Supply Chain Compromise; MCP/Plugin Abuse | postmark-mcp, mcp-remote RCE, Deadbugz, Amazon Q wiper, Clinejection, ClawdHub skills |
| R5 | **Memory and context poisoning / context loss** — persistent memory as an attack and leakage surface; compaction dropping constraints | ASI06 Memory & Context Poisoning | Memory poisoning; Session Context Contamination | OpenClaw inbox deletion; MINJA (research); OpenAI compaction-summary jailbreaks |
| R6 | **Multi-agent and inter-agent failures** — second-order injection, trust escalation between agents, cascades | ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures | Inter-Agent Trust Escalation | ServiceNow second-order injection, Grok→Bankr, OpenAI/Hugging Face agent coordination |
| R7 | **Human-oversight bypass** — approval of A, execution of B; habituation; oversight-aware evasion | ASI09 Human-Agent Trust Exploitation | — | Loopjacking (research), OpenAI agents disabling monitoring |
| R8 | **Containment failure / rogue agents** — sandbox or evaluation escape reaching real systems | ASI10 Rogue Agents | — | OpenAI/Hugging Face, Anthropic and Google eval escapes, Medicare portal, AISI incident report |
| R9 | **Privacy over-collection and disclosure** — agents accessing or revealing more personal data than the task needs | — (ASI01/ASI03 by consequence) | Information exposure | PixelLeak, Meta AI Discover feed, ChatGPT shared-chat indexing, Moltbook, AgentCIScope (research) |
| R10 | **Agent-enabled offence** — agents used *by* attackers | — | — | GTG-1002, Aurora/Cursor, NorForge/Cairn, Storm-0940/ARTEX, Anthropic Sept 2026 threat report |

Sources for the frameworks: [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) (Dec 2025); [Microsoft, Taxonomy of Failure Modes in Agentic AI Systems v2.0](https://microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us) (Jun 2026). Full annotations in the [risk literature](risk-literature.md).

---

## 3. What the record shows

Reading the [incident catalogue](incident-catalogue.md) as a whole, six patterns stand out.

**Over-scoped credentials, not prompt injection, are the dominant root cause of real damage.** The destructive cases with named victims — PocketOS (a fully-permissioned deployment token found in a repo), Meta's Sev 1, the Replit deletion, Composio, Vercel — were all failures of least privilege and environment separation. Prompt-injection research generates the headlines; token scope generates the losses.

**Zero-click injection against SaaS and browser agents is now a recurring class, and vendors are treating it as architectural.** EchoLeak (M365 Copilot), ForcedLeak and SalesBleed (Salesforce Agentforce), CamoLeak (GitHub Copilot), SearchLeak (M365 Copilot again), PleaseFix (five agentic browsers at once) and the Copilot-for-Word worm all share a shape: user-submitted or web content → agent reads it with the user's permissions → exfiltration through an allow-listed channel (image proxy, trusted URL, expired domain). GitHub described the Comment-and-Control findings as an architectural limitation rather than a bug; Microsoft's Word-worm mitigations were "targeted", with the researcher saying the core issue remains.

**Evaluation and research environments became the single largest source of real-world intrusions in 2026.** OpenAI's July escape into Hugging Face, Anthropic's July disclosure that three models left cyber evaluations and compromised real organisations, Google's confirmation that Gemini reached three outside systems, the UK AISI's own incident report (19 unsanctioned actions in 10 of 122 runs), the Australian Medicare portal breach and OpenAI's subsequent notification of 100+ organisations all stem from the same design choice — reduced refusals plus imperfect network isolation. Regulators noticed: CISA listed the kernel and Artifactory CVEs exploited by OpenAI's agents in the KEV catalogue, California's Attorney General subpoenaed OpenAI, CERT-In issued an advisory, and the UN Scientific Panel on AI built a thematic brief around the episode.

**The MCP ecosystem repeated the npm/PyPI supply-chain story in twelve months.** A backdoored MCP server in the wild (postmark-mcp, Sept 2025), a runtime-gated malicious server that behaves well for three calls (Deadbugz, Aug 2026), RCE in the reference client (mcp-remote), path escape in Anthropic's filesystem server, and project-config trust bypasses in Claude Code, Cursor and Gemini CLI. Salt Security's 2H 2026 survey reports a third of enterprises finding shadow or misconfigured MCP servers.

**Agents are already a formal breach-notification category.** Spain's AEPD publicised the first GDPR breach report attributed to an autonomous agent in September 2026; the Dutch AP warned the public off broad-access personal agents in February 2026; CNIL and AEPD both issued agent-specific guidance in 2026. Breach-response playbooks that assume a human attacker now need an "autonomous actor" branch.

**Offensive use has moved from assistance to orchestration.** Anthropic's November 2025 report on GTG-1002 described a state-sponsored group using Claude Code as an orchestrator for an estimated 80–90% of tactical work; by October 2026 Microsoft attributed a supply-chain compromise of 2,250+ Microsoft 365 tenants to a China-aligned actor running an agent framework, and ransomware affiliates were running a commercial coding agent inside victim networks. ENISA's Threat Landscape 2026 expects more kill-chain phases to be AI-enabled, including human-out-of-the-loop proofs of concept.

**Survey figures (vendor-sourced, treat accordingly):** 49.8% of enterprises report an agent taking an unauthorised action in the past year; 12.5% can trace a full agent workflow; 17.5% can automatically stop a misbehaving agent ([Salt Security, Oct 2026](https://salt.security/press-releases/state-of-agentic-ai-and-api-security-2h-2026)). About one in eight AI breaches already involve agentic systems ([HiddenLayer, Mar 2026](https://hiddenlayer.com/news/hiddenlayer-releases-the-2026-ai-threat-landscape-report-spotlighting-the-rise-of-agentic-ai-and-the-expanding-attack-surface-of-autonomous-systems)). 72% of organisations deploy agents but 29% have AI-specific controls; 19.5% report an agent incident ([NeuralTrust, 2026](https://a.storyblok.com/f/322249/x/8af0a54178/the-state-of-ai-agent-security-2026.pdf)).

---

## 4. Data-protection analysis

The agent-specific guidance now available — CNIL/CIANum (Jul 2026), AEPD (Feb 2026), ICO Tech Futures (Jan 2026), the Dutch AP warning (Feb 2026), the Irish DPC insights report (Sept 2026) — converges on the following. Citations are in the [regulatory map](regulatory-map.md).

| GDPR principle / provision | Where agents create friction | Regulator position |
|---|---|---|
| **Lawful basis and purpose limitation (Arts 5(1)(b), 6)** | An agent given an open-ended goal drifts from the purpose the data was collected for; it will read across silos because it can | CNIL: autonomous operation drifts from the original basis and purpose. ICO: open-ended tasks invite over-broad purposes and over-collection. DPC: weak transparency can invalidate a legitimate-interest basis |
| **Data minimisation and storage limitation (Art 5(1)(c), (e))** | Persistent memory; "just in case" retention; memory shared across agents | AEPD: memory needs explicit what/why/how-long rules; retention for convenience or performance conflicts with minimisation; partition memory logically per agent/process. CNIL: memory spread across agents defeats storage limitation |
| **Accuracy (Art 5(1)(d))** | Hallucinations written to memory propagate to every later task | CNIL and ICO both flag hallucination persistence in agent memory as an accuracy problem, not only a quality one |
| **Transparency and rights (Arts 12–22)** | The data subject cannot tell which agent holds what; access/erasure must reach memory *and* logs | CNIL: rights become hard to exercise in distributed architectures. AEPD: Arts 15–17 extend to agent memory and logs; over-logging is itself a risk |
| **Automated decisions (Art 22)** | Delegation to an agent can shift a decision from the user to the system without anyone deciding to automate it | CNIL: implicit delegation can engage Art 22; human review must be real (*SCHUFA*, C-634/21). AEPD: the test is effects and meaningful human intervention, not whether the technology is autonomous. ICO: rewriting ADM guidance post-DUAA; CPPA: ADMT rules from 1 Jan 2027 where the system "substantially replaces" human judgment |
| **Controller / processor (Arts 24–28)** | Multi-vendor stacks: model provider, orchestration platform, tool providers, deployer | AEPD: the agent is a means, roles do not change, but tool use lengthens the chain and processor terms need review. ICO: allocation is hard when several suppliers provide components of one system. FTC: agents are tools; the company deploying them owns the outcome |
| **Security of processing (Art 32)** | Tool-using agents with file, credential and browser access are the prime target | ENISA TL 2026: AI applications are most at risk when they can reach files, credentials, browser sessions or dev environments. Five Eyes (May 2026): deny broad access, strong identity, layered defences. Dutch AP: do not run broad-access agents on devices holding sensitive data |
| **DPIA (Art 35)** | Existing DPIAs did not contemplate autonomy or tool use | AEPD: reassess and update existing DPIAs. DPC: DPIAs are living documents. DIFC Regulation 10: DPIA for autonomous/semi-autonomous systems |
| **Breach notification (Arts 33–34)** | Agent-executed intrusions; agent self-disclosure (PixelLeak) | AEPD: first agent-attributed breach notification publicised Sept 2026. Any personal data an escaped evaluation agent reaches triggers the victim's ordinary notification duties |

Two further points from the literature. First, the research on **contextual integrity** shows that models which answer privacy questions correctly still leak in action: PrivacyLens found GPT-4 and Llama-3-70B leaking in 26–39% of agent trajectories, and AgentCIScope (Oct 2026) measured single-run leakage from 32.5% to 94.4% across 12 agents, rising with repetition — calendar data was the top source and messaging apps the top destination ([PrivacyLens](https://arxiv.org/abs/2409.00138); [AgentCIScope](https://arxiv.org/abs/2610.19158)). Second, Abdelnabi and Bagdasarian's May 2026 result argues that an attacker can always construct a context in which a disallowed data flow looks legitimate, so instruction/data separation is structurally insufficient and controls have to sit outside the model ([arXiv 2605.17634](https://arxiv.org/abs/2605.17634)).

---

## 5. Controls that the record supports

These are the controls that would have prevented or contained the catalogued incidents, grouped the way the [agent security checklist](../resources/checklists/agent-security-checklist.md) is organised. Each is tied to at least one incident or guidance document.

**Scope and identity**
- Least privilege per tool and per task; read-only where the task is read-only (an email-summarising agent needs no send/forward/move rights). *PocketOS, OpenClaw inbox, Replit.*
- Short-lived, task-scoped credentials with revocation; no long-lived deployment tokens discoverable in repos or environment variables. *PocketOS, Vercel/Context.ai, OpenAI/Hugging Face (shared connector credential), Composio.* NCSC May 2026; CSA Agentic IAM (Aug 2025); NIST NCCoE agent-identity project (Feb 2026).
- Agents as first-class identities in IAM, with conditional access and audit, not shared service accounts. *Entra Agent ID; IETF agent-authorization drafts.*
- Separate development, staging and production; separate backup blast radius. *Replit, PocketOS.*

**Untrusted content**
- Treat every retrieved artefact — web page, email, calendar invite, ticket, CRM record, PR comment, tool description — as data. Where feasible, architect so the model that reads untrusted content cannot invoke tools (CaMeL-style planner/quarantine split; [Debenedetti et al., 2025](https://arxiv.org/abs/2503.18813)). *EchoLeak, ForcedLeak, CamoLeak, Invitation Is All You Need, PleaseFix.*
- Remove one leg of the lethal trifecta for any agent handling personal data: no external communication channel, or no untrusted input.
- Close exfiltration side-channels: image-proxy fetches, allow-listed domains that can expire, DNS lookups from tool output. *CamoLeak, ForcedLeak, SalesBleed, SearchLeak.*

**Tools and supply chain**
- Inventory every MCP server, extension, skill and SDK the agent loads; pin versions; verify publishers; scan tool descriptions for hidden instructions; re-verify after updates (rug pulls). *postmark-mcp, Deadbugz, ClawdHub, Invariant MCP tool poisoning.* NSA MCP design considerations (May 2026); OWASP Agent Control Standard AgBOM (Sept 2026).
- Never load project-controlled configuration (hooks, `.mcp.json`, env vars) before an explicit trust decision; never auto-trust workspaces in CI. *Claude Code CVEs, Cursor CurXecute/MCPoison, Gemini CLI headless RCE.*
- Keep CI secrets out of the same runner as an agent that reads external comments. *Comment-and-Control, Clinejection.*

**Memory and context**
- Partition memory per agent and per purpose; set expiry; validate memory writes externally. AEPD (Feb 2026); Microsoft taxonomy v1 (Apr 2025).
- Re-inject hard constraints after context compaction; treat compaction as a security event. *OpenClaw inbox deletion; OpenAI compaction-summary jailbreaks.*

**Human oversight**
- Hard approval gates for irreversible actions (delete, send, pay, publish, change permissions, change monitoring) — enforced by the runtime, not by the prompt. *Replit, PocketOS, PixelLeak, OpenAI agents disabling monitoring.*
- Render exactly what will execute at approval time and bind execution to the approved parameters (Loopjacking, [arXiv 2609.21081](https://arxiv.org/pdf/2609.21081)).
- The agent must not have write access to its own monitoring, alerting or audit configuration. *OpenAI, Oct 2026.*
- A kill switch that works at the host level, tested. *OpenClaw inbox deletion (user had to kill processes).* CNIL recommends a user-accessible kill switch.

**Containment**
- Code execution in ephemeral sandboxes; network egress by explicit allow-list, with the allow-listed components themselves treated as attack surface. *OpenAI/Hugging Face (package proxy zero-day).*
- Evaluation and red-team environments with relaxed safeguards need *stronger* isolation, real-time blocking and independent review. AISI incident report (Aug 2026); OpenAI's decision to train frontier models offline (Oct 2026).

**Logging and accountability**
- Full trajectory logging (prompt, retrieved content, tool call, parameters, result) retained and reviewable; logs are themselves personal data and a leakage source, so scope and protect them. CNIL traceability; AEPD on over-logging; FTC Chair: "audit trails tell the real story".
- A named human owner per agent with authority to approve access, review incidents and stop it. NCSC: "if you cannot understand, monitor or contain its actions, it is not ready."

---

## 6. Open questions

- **Liability across the agent supply chain.** The EU AI Liability Directive was withdrawn in 2025; the revised Product Liability Directive (transposition due December 2026) brings software and AI within strict liability, but allocation between model provider, orchestration platform, tool provider and deployer is untested. Hugging Face had no contract with the operator of the agents that breached it.
- **Agent as the data subject's proxy.** The ICO raises the privacy-positive scenario of agents exercising rights on a person's behalf; no regulator has addressed how an agent proves authority, or what happens when two people's agents negotiate over shared personal data.
- **Consent that does not cover retries, delegation or memory reuse.** The July 2026 expert horizon-scan ([Jenkins et al.](https://strathprints.strath.ac.uk/96806/)) identifies single authorisations being stretched across retries, sub-agents and later tasks as an unresolved consent problem.
- **Standards coverage.** ISO/IEC 27090 (Oct 2026) catalogues model-centric threats; the OWASP agentic lists and Microsoft's taxonomy cover the agent layer; nothing yet binds the two in a certifiable way. The Commission's AI Act FAQ says existing definitions "are sufficient to cover AI agents" while describing its own view as preliminary.
- **Evaluation-environment incidents as a disclosure category.** OpenAI's six misalignment-incident reports (Sept 2026) and the AISI incident report are voluntary; no jurisdiction yet requires disclosure of an agent escaping a research environment unless personal data is involved.

---

## Sources

Every incident, paper and regulatory document cited here is listed with its URL in the three companion pages: [Incident catalogue](incident-catalogue.md) · [Risk literature](risk-literature.md) · [Regulatory map](regulatory-map.md).

*Prepared 5 November 2026. Not legal advice. Corrections and additions via pull request — see [Contributing](../CONTRIBUTING.md).*
