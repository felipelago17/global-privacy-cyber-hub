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
| [`connectors/`](connectors/) | External hubs (IAPP, OECD, OneTrust, FPF, OWASP, ENISA) and technical connectors |
| [`related-forks.md`](related-forks.md) | Awesome lists and related projects to star, fork or reference |

## Highlighted analyses

| Analysis | One-line takeaway |
|---|---|
| [DPIA on Google Cloud Platform](analyses/gcp-dpia-summary.md) | Dutch government DPIA (June 2026) finds 11 low risks across Compute Engine, Cloud SQL, Cloud Storage and BigQuery; useful template for cloud compliance checklists |
| [EDPB Opinion 28/2024 on AI models](analyses/edpb-ai-models.md) | AI models trained on personal data are not automatically anonymous; three-step legitimate-interest test for development and deployment |
| [The Three Layers of Agent Security](analyses/agent-security-three-layers.md) | DeepMind's policy framework: secure individual agents, manage multi-agent risk, empower cyber defenders |
| [High-risk without safeguards? (EU AI Act, medical AI)](analyses/medical-ai-act-safeguards.md) | Health Innovation Package proposals would keep medical AI "high-risk" on paper while stripping most AI Act safeguards |
| [DPDP in Practice (India)](analyses/india-dpdp-practice.md) | Phased commencement to May 2027, narrow lawful bases, every breach reportable, high penalty ceilings |
| [Transatlantic transfers after the FTC ruling](analyses/transatlantic-transfers-ftc.md) | US Supreme Court ruling on FTC independence reopens uncertainty for the EU–US DPF and UK–US Data Bridge |
| [10 Tips for Global Compliance (IAPP)](analyses/iapp-global-compliance-tips.md) | Practical operating model for multi-jurisdictional privacy programmes |

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
