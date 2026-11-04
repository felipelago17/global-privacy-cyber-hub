# External hubs and connectors

Curated links to the collections this hub is modelled on, plus tools and integration ideas. The aim is to **point to** the best external resources, not to replicate them. Links are to top-level pages that are stable; drill down from there.

## Primary hubs

### IAPP — International Association of Privacy Professionals
- **Resource Center:** <https://iapp.org/resources/> — templates and tools (privacy notices, DPAs, DPO reports), legislative trackers, white papers.
- **Privacy-Enhancing Technologies repository** — curated PETs materials and use cases.
- **AI Governance Center** — AI governance frameworks, EU AI Act resources, the AIGP body of knowledge.
- **Global legislative trackers** — US state privacy law tracker, global comprehensive privacy law map, AI legislation tracker.
- *Why it matters:* the broadest practitioner library; good for templates and keeping up with new laws.

### OECD — Global Repository for Privacy-Enhancing Technologies
- **OECD home:** <https://www.oecd.org/> (search "Global Repository for Privacy-Enhancing Technologies").
- Launched around October 2026 as part of the **Data Free Flow with Trust (DFFT)** workstream; builds on the OECD's 2023 *Emerging Privacy-Enhancing Technologies* report.
- Organised around **legal obligations**, **technical standards**, **use cases** and guidance on specific PETs (differential privacy, synthetic data, federated learning, secure multi-party computation, TEEs).
- *Why it matters:* the authoritative cross-jurisdictional map of how regulators view PETs; useful when arguing a PET satisfies a legal requirement.

### OneTrust — Resources library
- **Library:** <https://www.onetrust.com/resources/> — guides and checklists on AI-ready governance, privacy automation, consent and preference management, third-party risk, ISO 27001 readiness, runtime AI governance.
- Historical IAPP–OneTrust collaborations on consent and data-subject-rights platforms and benchmarking reports.
- *Why it matters:* operational templates and workflow descriptions for programme automation; vendor-authored, so read with that in mind.

## Other high-value connectors

| Hub | Link | Use it for |
|---|---|---|
| **Future of Privacy Forum (FPF)** | <https://fpf.org/> | PETs repository, AI and youth-privacy policy analysis, US state law issue briefs |
| **OWASP AI Security and Privacy Guide** | <https://owasp.org/www-project-ai-security-and-privacy-guide/> | Concrete controls for AI systems; pairs with the OWASP Top 10 for LLM Applications |
| **OWASP Top 10 for LLM Applications** | <https://genai.owasp.org/> | Prompt injection, insecure output handling, supply-chain and agent risks |
| **Microsoft Presidio** | <https://github.com/microsoft/presidio> | Open-source PII detection and anonymisation for text and images |
| **Fides (Ethyca)** | <https://github.com/ethyca/fides> | Open-source privacy engineering: data mapping, DSAR automation, consent |
| **ENISA** | <https://www.enisa.europa.eu/> | EU cybersecurity guidance, threat landscape, PETs and data-protection engineering reports |
| **EDPB** | <https://www.edpb.europa.eu/> | Guidelines, opinions (incl. Opinion 28/2024), binding decisions |
| **UK ICO** | <https://ico.org.uk/> | Guidance on AI, PETs, DPIAs, international transfers (IDTA) |
| **NIST** | <https://www.nist.gov/privacy-framework> and <https://www.nist.gov/itl/ai-risk-management-framework> | Privacy Framework, AI RMF, Cybersecurity Framework 2.0 |
| **CNIL** | <https://www.cnil.fr/en> | AI how-to sheets, PIA tool, anonymisation guidance |
| **India MeitY / DPB** | <https://www.meity.gov.in/> | DPDP Act, Rules and notifications |
| **UAE regulators** | TDRA, ADGM ODP, DIFC Commissioner | PDPL, ADGM and DIFC data-protection regimes for GCC comparisons |

## Technical connectors (ideas and starting points)

These are optional. If implemented, keep scripts in a `scripts/` folder and workflows in `.github/workflows/`, and document each one here.

1. **Regulatory update puller** — a GitHub Action that fetches RSS/Atom feeds from the EDPB, ICO, CNIL, NIST and the US Federal Register (privacy/cyber/AI terms) and appends a dated digest to `resources/updates/`. Modelled on Felipe's AI-Regulatory-Monitor pipeline.
2. **Data-mapping and DSAR workflow links** — pointers to Fides and to open-source DSAR tooling rather than custom code.
3. **PETs experimentation** — links to reference implementations: OpenDP (differential privacy), Flower (federated learning), Presidio (anonymisation), OpenMined (PySyft).
4. **PII scanning pre-commit hook** — optional Presidio-based check to stop personal data being committed to the repo by accident.
5. **Link checker** — a scheduled workflow (e.g. `lychee`) to flag dead links in this file and `resources/papers/links.md`.

## Maintenance

- Review this file quarterly; regulators reorganise their sites often.
- Prefer top-level, stable URLs; deep links go in the relevant analysis file instead.
- Add a one-line "why it matters" for every new entry.
