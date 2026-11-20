# global-privacy-cyber-hub

Curated open resource hub for **data privacy, cybersecurity, AI governance, DPIAs, global compliance frameworks and emerging risks**.

The hub draws on regulatory opinions (EDPB, EU AI Act), industry analyses (Google DeepMind agent security, the Dutch government DPIA on Google Cloud Platform) and practical guidance (IAPP, Novation Strategy on India's DPDP Act). It is inspired by the curated collections maintained by the IAPP, OneTrust and the OECD Global Repository for Privacy-Enhancing Technologies.

> **Disclaimer.** Everything in this repository is for educational and reference purposes only. It is not legal advice and does not create a lawyer–client relationship. Always check the primary source and take jurisdiction-specific advice before acting.

---

## Purpose and scope

- Collect concise, well-sourced **summaries of key papers, opinions and DPIAs** on privacy, cyber and AI governance.
- Map the **frameworks** that matter across jurisdictions (GDPR, EU AI Act, UK, US, India DPDP, NIST, ISO).
- Provide practical **checklists and templates** (DPIA outline, legitimate-interest assessment, agent-security controls).
- Act as a **connector** to the best external hubs and open-source tooling, rather than duplicating them.
- Keep a curated list of **related repositories and awesome lists** worth starring, forking or contributing to.

Focus areas: AI governance, cloud DPIAs, agent security, privacy-enhancing technologies (PETs), and multi-jurisdictional compliance (EU, UK, US, India, GCC).

## How to navigate

| Folder | What you will find |
|---|---|
| [`analyses/`](analyses/) | Focused write-ups of the source papers — key findings, practical implications, source notes |
| [`resources/papers/`](resources/papers/) | Links to the original documents with short abstracts, plus summaries |
| [`resources/frameworks/`](resources/frameworks/) | GDPR, EU AI Act, DPDP, NIST, ISO and other framework notes |
| [`resources/tools/`](resources/tools/) | Open-source tools, templates and automation ideas |
| [`resources/checklists/`](resources/checklists/) | Practitioner checklists derived from the analyses |
| [`ai-agents/`](ai-agents/) | **Data privacy and cyber risks of AI agents** — risk taxonomy, 50+ incident catalogue (2025–26), annotated risk literature, regulator map (CNIL, AEPD, ICO, NCSC, Five Eyes, CAISI, AI Act FAQ) |
| [`case-studies/`](case-studies/) | Incident write-ups tested against the frameworks — Binance hack (Oct 2026), OpenAI/Hugging Face autonomous-agent intrusion (Jul 2026), EFS blood-plasma freezers (Nov 2026), Operation Snowball (Nov 2026), plus breach-liability cases: Uber/Sullivan, SolarWinds, Marriott and Yahoo M&A, Equifax/Capital One/Optus/Medibank class actions, Meta €1.2bn, Shukran loyalty breach (Nov 2026), Anthropic/Claude Korea PIPC investigation (Nov 2026), Maersk legacy-system extortion (Nov 2026), XAI for disease classification review (Memon et al., 2026), Shanghai LLM compute-theft sentence (Nov 2026), Uber/Fireworks AI vendor breach (Nov 2026), GPU monitoring manipulation (Nov 2026), SQL Server hijacking with Gh0st RAT (Nov 2026), Check Point Gaia zero-day (Nov 2026), Optimizely third-party script compromise (Nov 2026), Equinor IT cyberattack (Nov 2026) |
| [`training-labs/`](training-labs/) | **Hands-on practice** — AI security and red-teaming labs (Gandalf Agent Breaker, Crucible, HackAPrompt, Prompt Airlines, PortSwigger web LLM labs) 17 general cyber platforms and a 20-site reference list, with safe-use rules (Nov 2026) |
| [`updates/`](updates/) | Automated daily digest of privacy, cyber and AI-governance news from IAPP, EDPB, ICO, CNIL, ENISA, NCSC, FTC, NIST, CISA, FPF, EFF |
| [`connectors/`](connectors/) | External hubs (IAPP, OECD, OneTrust, FPF, OWASP, ENISA) and technical connectors |
| [`related-forks.md`](related-forks.md) | Awesome lists and related projects to star, fork or reference |

## Highlighted analyses

| Analysis | One-line takeaway |
|---|---|
| [DPIA on Google Cloud Platform](analyses/gcp-dpia-summary.md) | Dutch government DPIA (June 2026) finds 11 low risks across Compute Engine, Cloud SQL, Cloud Storage and BigQuery; useful template for cloud compliance checklists |
| [EDPB Opinion 28/2024 on AI models](analyses/edpb-ai-models.md) | AI models trained on personal data are not automatically anonymous; three-step legitimate-interest test for development and deployment |
| [EDPB Guidelines 1/2024 on legitimate interest](analyses/edpb-guidelines-legitimate-interest.md) | Three cumulative conditions, documented assessment, reasonable expectations; Version 2.0 adopted 10 Nov 2026 |
| [EDPB 2027 enforcement on automated recruitment (Art. 22)](analyses/edpb-cef-2027-automated-recruitment-art22.md) | Reported CEF 2027 topic; Dun & Bradstreet and Universal Versand AG opinion on automated decisions |
| [The Three Layers of Agent Security](analyses/agent-security-three-layers.md) | DeepMind's policy framework: secure individual agents, manage multi-agent risk, empower cyber defenders |
| [High-risk without safeguards? (EU AI Act, medical AI)](analyses/medical-ai-act-safeguards.md) | Health Innovation Package proposals would keep medical AI "high-risk" on paper while stripping most AI Act safeguards |
| [DPDP in Practice (India)](analyses/india-dpdp-practice.md) | Phased commencement to May 2027, narrow lawful bases, every breach reportable, high penalty ceilings |
| [UAE PDPL: missing Executive Regulations](analyses/uae-pdpl-implementing-regulations-gap.md) | In force since 2022 but implementing regulations still not issued per law firms (mid-2026); new federal AI and Data Authority announced 14 June 2026; distrust commercial sites claiming otherwise |
| [DIFC Regulation 10 lifecycle](analyses/difc-regulation-10-lifecycle.md) | In force 1 Sep 2023; deployer/operator duties, Autonomous Systems Officer and certification for high-risk processing; 2026 consultation and Accelerator |
| [Transatlantic transfers after the FTC ruling](analyses/transatlantic-transfers-ftc.md) | US Supreme Court ruling on FTC independence reopens uncertainty for the EU–US DPF and UK–US Data Bridge |
| [Luxembourg NIS2: ILR annual security-measures reporting](analyses/nis2-luxembourg-ilr-security-measures-reporting-2027.md) | ILR Regulation N26/10 (26 Oct 2026): essential entities file measures, risk scenarios and multi-year plan by 15 Mar 2027; single-source, gaps flagged |
| [The AI model distillation paradox (Lawfare)](analyses/ai-model-distillation-paradox-lawfare-2026.md) | Fair use for training vs "malicious" distillation: IP, terms of service, export controls and data-protection angles (Oct 2026 commentary) |
| [Cloud concentration: the "centrality menace" revisited (TechnoLlama)](analyses/cloud-centrality-menace-technollama-2026.md) | Microsoft 365 outage as a case for minimum viable service, identity resilience, digital sovereignty and DORA/CTP-style oversight (Nov 2026 commentary) |
| [ENISA State of Cybersecurity in the Union 2026](analyses/enisa-state-of-cybersecurity-union-2026.md) | Threat level "substantial"; EU Cybersecurity Index 71.53/100; DDoS, public administration, AI as amplifier; NIS2 transposition gaps (10 Nov 2026) |
| ["Your attackers' AI knows you better than yours does" (Forbes Tech Council)](analyses/ai-amplifies-security-posture-forbes-2026.md) | AI amplifies existing posture: Japan IDC Frontier and South Korea ARTEX examples checked against other reporting; vendor-authored opinion (Nov 2026) |
| [PwC: securing OT against AI and geopolitical risk](analyses/pwc-ot-geopolitical-ai-risk-2026.md) | OT/ICS exposure, segmentation, vendor access and maturity tiers; incident examples as described by PwC, unverified (Nov 2026) |
| [APLN: cyber-nuclear nexus and escalation pathways](analyses/apln-cyber-nuclear-nexus-escalation-pathways-2026.md) | Fei Su (SIPRI): cyber incidents near strategic systems, attribution ambiguity, Salt Typhoon/Viasat and Beijing Time cases, AI-enabled risk; two cases partly checked (Nov 2026) |
| [Booz Allen Cyber Weapon Index](analyses/booz-allen-cyber-weapon-index-2026.md) | Vendor benchmark of frontier models' offensive cyber capability: VRS, kill-chain attainment, US vs China, refusals vs local models (Oct 2026) |
| [Saudi draft Responsible AI Policy (Clifford Chance)](analyses/saudi-sdaia-responsible-ai-policy-clifford-chance-2026.md) | SDAIA draft moves from voluntary principles to supervision: four risk tiers, registration, ethics badges, pre-deployment review for high-risk AI, sandbox; secondary source, no article numbers (Nov 2026) |
| [Temu: DSA preliminary findings on illegal products (European Commission)](analyses/temu-dsa-preliminary-findings-illegal-products-2026.md) | Art. 35 mitigation failures (test reports, moderation, repeat sellers) after the €200M May 2026 fine; fine up to 6% possible; press-release text not read (17 Nov 2026) |
| [Kolt: Governing AI Agents (Notre Dame Law Review)](analyses/kolt-governing-ai-agents-notre-dame-law-review-2026.md) | Agency law and principal-agent theory applied to AI agents; limits of incentives, monitoring, enforcement; inclusivity, visibility and liability principles; machine-assisted read, not checked page by page (101 ND L. Rev. 335, 2026) |
| [AEPD and HDPA: Secure Processing Environments (Nov 2026)](analyses/aepd-hdpa-secure-processing-environments-2026.md) | Joint Spanish and Greek DPA guidance on SPEs under the DGA and EHDS: effective control over third-party and cloud providers, certification not enough, Five Safes, TEEs versus SPEs, homomorphic-encryption use case; initial guidance, not binding |
| [UK committee: Guardrails for growth, AI safety and security (Nov 2026)](analyses/uk-bist-committee-guardrails-for-growth-ai-safety-2026.md) | Commons BIST Committee report as summarised by Labour Digital: proposed AI Safety and Security Bill, separate regulator, mandatory incident reporting; primary report not read |
| [Java4Shell: CISA urges patching a HotSpot Base64 flaw (Nov 2026)](analyses/java4shell-cisa-alert-hotspot-base64-2026.md) | CVE-2026-114938 (CVSS 8.1) as reported by The Hacker News: out-of-bounds write, Keycloak conditions, inventory advice; CISA's alert and Oracle's CSPU advisory (both read via pasted text) plus press report for Keycloak and test details |
| [Brazil ANPD: Discord "Go Live" suspension upheld (Nov 2026)](analyses/anpd-discord-go-live-suspension-appeal-denied-2026.md) | Board vote denying Discord's appeal: precautionary feature suspension under the Digital ECA is not a judicial-reservation sanction; unofficial English translation, original not seen |
| [ClickFix fake CAPTCHA scam (The Conversation, Nov 2026)](analyses/clickfix-fake-captcha-the-conversation-2026.md) | Explainer on fake human-verification pages that make users paste commands and install infostealers; full text read via user paste; defences and incident steps included |
| [Bridgewater: AI and the cyber "virus" (Nov 2026)](analyses/bridgewater-ai-cyber-virus-2026.md) | Investment-firm research arguing AI shortens patch windows (11 days disclosure-to-exploit) and current policy is insufficient; summary of the page only, figures unverified |
| [CFR (Segal): why everything seems to be crashing (Nov 2026)](analyses/cfr-segal-why-everything-is-crashing-2026.md) | Argues the Nov 2026 run of outages looks like fragility from fast AI-driven patching, not attack; calls for clear communication; full article text read via user paste |
| [EU–US AI sovereignty contest (Kennedys)](analyses/eu-us-ai-sovereignty-contest-kennedys-2026.md) | AI Act reach v US export controls; CADA four-level cloud sovereignty framework and Chips Act 2.0; US law can switch off AI capability; secondary source, unverified against primaries (Nov 2026) |
| [Cybersecurity of sensitive non-personal data](analyses/sensitive-non-personal-data-security.md) | Trade secrets, OT/process data, CUI, model weights and research data: five legal hooks beyond privacy law, with a verification table (Nov 2026) |
| [10 Tips for Global Compliance (IAPP)](analyses/iapp-global-compliance-tips.md) | Practical operating model for multi-jurisdictional privacy programmes |

## Frameworks spotlight

- [ISO/IEC 27090:2026 — AI security](resources/frameworks/iso-27090-ai-security.md): the new ISO standard on security threats to AI systems (published 14 Oct 2026), with related publications and its relationship to 27001/42001/27091 and EU AI Act Art. 15.
- [ISO/SAE TR 8477:2026 — Road vehicle cybersecurity V&V](resources/frameworks/iso-sae-tr-8477-cybersecurity-vv.md): informative technical report on planning and evidencing cybersecurity verification and validation under ISO/SAE 21434 (ISO page: under publication, Edition 1, Oct 2026), with links to PAS 8475 and SAE J3322.

## Connectors

See [`connectors/external-hubs.md`](connectors/external-hubs.md) for the full annotated list. Headline links:

- **IAPP** — resource centre, PETs repository, templates and legislative trackers: <https://iapp.org/resources/>
- **OECD** — Global Repository for Privacy-Enhancing Technologies: <https://www.oecd.org/>
- **OneTrust** — resource library on AI-ready governance, consent, third-party risk: <https://www.onetrust.com/resources/>
- **Future of Privacy Forum** — PETs repository and policy analysis: <https://fpf.org/>
- **OWASP** — AI Security and Privacy Guide: <https://owasp.org/www-project-ai-security-and-privacy-guide/>
- **Microsoft Presidio** — PII detection and anonymisation: <https://github.com/microsoft/presidio>
- **Fides (Ethyca)** — open-source privacy engineering: <https://github.com/ethyca/fides>

## Related forks and awesome lists

See [`related-forks.md`](related-forks.md). Primary references: `yilmaztolga/awesome-data-privacy` and `getprobo/awesome-compliance`.

## Contributing

Contributions are welcome — new summaries, framework notes, checklists or connector links. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) first. Open an issue to propose a new source before writing a full analysis so that scope stays coherent.

## Licence

Code and tooling: [MIT](LICENSE). Documentation and analyses: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless a file states otherwise. Summaries of third-party documents are the author's own synthesis; the underlying works remain the property of their respective rights-holders.

Topics: `data-privacy` · `cybersecurity` · `gdpr` · `ai-governance` · `dpia` · `pets` · `compliance` · `dpdp` · `agent-security`
