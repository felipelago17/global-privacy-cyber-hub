# Tools and templates

Open-source tools, templates and automation ideas. Link to external tools rather than vendoring them; keep any scripts small and documented.

## Open-source tools (by job)

| Job | Tool | Link |
|---|---|---|
| PII detection / anonymisation | Microsoft Presidio | <https://github.com/microsoft/presidio> |
| Privacy engineering, data mapping, DSAR, consent | Fides (Ethyca) | <https://github.com/ethyca/fides> |
| Differential privacy | OpenDP; Google DP | <https://github.com/opendp/opendp> · <https://github.com/google/differential-privacy> |
| Federated learning | Flower | <https://github.com/adap/flower> |
| Privacy-preserving ML | OpenMined PySyft | <https://github.com/OpenMined/PySyft> |
| LLM / agent security testing | OWASP resources; Garak; promptfoo | <https://genai.owasp.org/> · <https://github.com/NVIDIA/garak> · <https://github.com/promptfoo/promptfoo> |
| DPIA / PIA tooling | CNIL PIA software | <https://www.cnil.fr/en/privacy-impact-assessment-pia> |
| GRC / compliance automation | see `getprobo/awesome-compliance` | <https://github.com/getprobo/awesome-compliance> |

## Templates (to be added here)

- `dpia-outline.md` — DPIA outline built on the GCP DPIA's five-category data model
- `legitimate-interest-assessment.md` — LIA template following the EDPB three-step test for development and deployment phases
- `agent-security-controls.md` — control list mapped to DeepMind's three layers and OWASP LLM Top 10
- `breach-triage-dpdp.md` — breach classification and notification worksheet for the no-threshold DPDP regime

Checklists derived from the analyses live in [`../checklists/`](../checklists/).

## Automation ideas

See the "Technical connectors" section of [`../../connectors/external-hubs.md`](../../connectors/external-hubs.md).
