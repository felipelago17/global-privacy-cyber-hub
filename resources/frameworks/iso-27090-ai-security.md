# ISO/IEC 27090:2026 — Cybersecurity — Artificial intelligence (AI) — Addressing security threats and compromises to AI systems

`International · AI security · ISO 27000 family · EU AI Act Art. 15`

## At a glance

| Attribute | Detail |
|---|---|
| **Full title** | Cybersecurity — Artificial intelligence (AI) — Addressing security threats and compromises to AI systems |
| **Status** | Published, Edition 1, **14 October 2026** (stage 60.60), 56 pages |
| **Committee** | ISO/IEC JTC 1/SC 27 (Information security, cybersecurity and privacy protection) |
| **Type** | Guidance standard — **not** a certifiable management-system standard |
| **Companion** | ISO/IEC 27091 *Cybersecurity and privacy — AI — Privacy protection* (FDIS, approval stage as of Nov 2026) |
| **Primary source** | ISO landing page: <https://www.iso.org/standard/56581.html> · ISO explainer: <https://www.iso.org/insights/ISO-27090-explained> |

## What it covers

ISO/IEC 27090 gives guidance on understanding, detecting and mitigating security threats **specific to AI systems** across the whole lifecycle — development, training, deployment, operation and model updates. Its premise is that conventional cybersecurity can be fully in place and an AI system still be compromised, because the attack surface includes the **training data, the model and the inference workflow**, not only the surrounding software and infrastructure.

The standard focuses on protecting AI systems themselves; it does not cover using AI to defend other systems.

### Threat catalogue

The standard describes a dozen or so threat types, each with roughly a page on the threat, its consequences, detection and mitigation. The main families:

| Family | Threats | Lifecycle stage |
|---|---|---|
| **Poisoning** | Training-data poisoning (direct or via supply chain); model poisoning at development or runtime; poisoned foundation models obtained through transfer learning | Development; operation (continuous-learning systems) |
| **Evasion** | Adversarial inputs crafted to mislead the model; prompt injection | Operation |
| **Extraction / confidentiality** | Model theft via repeated legitimate-looking queries or direct exfiltration; model inversion; membership inference; training-data leakage; input/output leakage | Development and operation |
| **Availability** | Denial of model service | Operation |
| **Conventional** | Bypassing model access control, compromised plugins/tools, classic application attacks against AI components | All stages |

A distinctive point: **operational data can become training data.** In systems that learn continuously or are periodically retrained on usage data, corrupted inputs at runtime can poison future model versions — which links operational monitoring to development-time security.

### Relationship to other frameworks

| Framework | Relationship |
|---|---|
| **ISO/IEC 27001 / 27002** | 27090 complements them: 27001 gives the ISMS requirements, 27002 the control catalogue, 27090 the AI-specific threat detail. It does not create new management-system requirements |
| **ISO/IEC 42001** (AI management system) | 42001 governs responsible AI development and use; 27090 supplies the security-threat content an AIMS should address |
| **ISO/IEC 27091** (AI privacy) | Sister document from the same working group on privacy risks in AI/ML across the lifecycle; at FDIS stage |
| **ISO/IEC 5338** (AI lifecycle) | Shared lifecycle model and authorship lineage (Rob van der Veer led 5338 and contributed to 27090/27091) |
| **EU AI Act, Article 15** | Requires accuracy, robustness and cybersecurity for high-risk systems and names data poisoning, model poisoning and adversarial inputs explicitly; 27090 is a natural evidence base, but adoption does not itself establish legal compliance |
| **NIST AI RMF 1.0 / NIST AI 100-2 (Adversarial ML taxonomy)** | US counterparts; NIST's AML taxonomy maps closely onto 27090's threat families |
| **OWASP AI Exchange / Top 10 for LLM Applications** | Practitioner-level control vocabulary; OWASP AI Exchange fed into the ISO drafting process |
| **MITRE ATLAS** | Adversarial tactics/techniques knowledge base useful for mapping 27090 threats to observed attacks |

## Practical implications

- **ISMS owners:** add AI assets (datasets, models, prompts, evaluation harnesses, agent tool credentials) to the asset inventory and risk register; treat 27090 as the threat source for 27005 risk assessment on those assets.
- **AI governance teams:** use the threat catalogue as the security chapter of a model risk assessment or EU AI Act Article 15 evidence file.
- **Procurement / vendor management:** ask model and platform vendors which 27090 threat families they address and how — particularly model-extraction defences and poisoning controls on retraining pipelines.
- **Agentic systems:** 27090 is model-centric; pair it with agent-specific guidance (see [DeepMind's Three Layers](../../analyses/agent-security-three-layers.md) and the [agent-security checklist](../checklists/agent-security-checklist.md)) for tool-use, sandboxing and multi-agent risk, which the standard does not cover in depth.
- **Certification:** nothing to certify against; auditors may nonetheless reference it when assessing 27001 or 42001 scopes that include AI.

## Related publications and commentary

| Source | What it adds | Link |
|---|---|---|
| ISO — *ISO/IEC 27090 explained* (insights article) | ISO's own plain-language summary of scope and rationale | <https://www.iso.org/insights/ISO-27090-explained> |
| ISO — standard page (abstract, status, preview) | Authoritative status and purchase/preview | <https://www.iso.org/standard/56581.html> |
| ISO/IEC FDIS 27091 — AI privacy protection | Companion privacy standard; scope and status | <https://www.iso.org/standard/56582.html> |
| Nemko Digital — *ISO/IEC 27090 published as new AI cybersecurity standard* (30 Oct 2026) | Practitioner summary; regulatory relevance for EU AI Act high-risk systems | <https://digital.nemko.com/news/isoiec-27090-published-as-new-ai-cybersecurity-standard> |
| ISO27001security.com — ISO/IEC 27090 page | Independent ISO27k commentary; threat list; critique that the standard is "pessimistic" and does not treat AI as a defensive asset | <https://www.iso27001security.com/html/27090> |
| Kertos — *ISO 27090 explained: AI security in your ISMS* | Comparison table 27001 / 42001 / 27090 / EU AI Act | <https://www.kertos.io/en/blog/iso-27090> |
| Rob van der Veer (SIG) — ITU workshop slides, *AI security & privacy standards* (2024) | Lifecycle threat map from a lead author of 5338/27090/27091; the clearest public diagram of the threat taxonomy | <https://www.itu.int/en/ITU-T/Workshops-and-Seminars/2024/0219/Documents/Rob%20van%20der%20Veer_V2.pdf> |
| NIST AI 100-2 E2025 — *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations* | US taxonomy that maps onto the 27090 threat families | <https://csrc.nist.gov/pubs/ai/100/2/e2025/final> |
| OWASP AI Exchange | Open control catalogue that contributed to ISO/IEC 27090 drafting | <https://owaspai.org/> |
| MITRE ATLAS | Adversarial threat landscape for AI systems — techniques and real-world case studies | <https://atlas.mitre.org/> |
| ENISA — *Multilayer framework for good cybersecurity practices for AI* (2023) and later AI threat-landscape reports | EU-level framing that 27090 operationalises | <https://www.enisa.europa.eu/> |

### Gaps and open questions

- Agentic and multi-agent threats (tool misuse, sandbox escape, inter-agent propagation) are only partly addressed — see the [OpenAI/Hugging Face case study](../../case-studies/openai-hugging-face-2026.md) for why this matters.
- No treatment of AI as a defensive capability; organisations will need a separate view on AI-enabled security operations.
- Harmonisation status under the EU AI Act: as of November 2026 ISO/IEC 27090 is not itself a harmonised standard; CEN-CENELEC JTC 21 work on Article 15 should be tracked.

## Status notes

Facts above are as of November 2026. Verify stage codes and the 27091 status on the ISO pages before citing; draft-stage descriptions circulated before October 2026 may differ from the published text.
