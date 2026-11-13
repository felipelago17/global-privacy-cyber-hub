# Case study — The irreversibility trap in fine-tuning (analytical case, 2026)

`AI governance · Fine-tuning · Erasure and retraining · Vendor dependence · UAE / DIFC · Design controls`

## Summary

This is an analytical case study, not an incident report. It takes the "irreversibility trap" described by Shoshana Rosenberg in *Practical AI Governance* (Kogan Page, 2026, p. 274) and works it through a hypothetical fine-tuning project. The trap has two limbs: sensitive data irreversibly shapes a model (through training, fine-tuning or embedding), and the organisation becomes operationally dependent on that model. Once both are true, the organisation can neither roll the model back nor leave the vendor without stopping operations. The first limb is created when a model is fine-tuned; the second is created by how the model is then used at inference. Keeping the two apart is a design decision that has to be taken before training.

## Scenario (hypothetical)

| Item | Detail |
|---|---|
| Organisation | UAE industrial group with an onshore operating company and a DIFC subsidiary |
| Project | Provider-hosted fine-tune of a closed-weight language model |
| Training data | Maintenance records; employee and customer correspondence; technical manuals from a foreign equipment supplier |
| One year on | Model embedded in maintenance planning and customer service; earlier manual workflows retired; no portable copy of the adapted weights |

## The fine-tuning elements that build the trap

| Element | Why it is hard to reverse | Privacy and cyber consequence |
|---|---|---|
| **Personal data in the training set** | Information reflected in parameters is not a record that can be deleted | Lawful basis and purpose must hold for the training use itself; the model cannot be presumed anonymous (see [EDPB Opinion 28/2024](../analyses/edpb-ai-models.md)); in the DIFC, processing to enable a system's learning is within [Regulation 10](../analyses/difc-regulation-10-lifecycle.md) |
| **Third-party confidential or controlled technical data** | The adapted weights inherit the restrictions as an open question | Confidentiality breach if weights or outputs leak; possible export-control exposure |
| **Rights in the adapted weights** | Set by contract at the outset; hard to renegotiate once dependent | No portable copy means no exit |
| **Inference data reused for training** | Prompts, outputs and user feedback (ratings, corrections) retained and fed back turn an "inference-only" service into development; Christian describes feedback as the signal from which a system infers its objective (pp. 262, 264) | Purpose drift; operational data can poison later versions (see [ISO/IEC 27090](../resources/frameworks/iso-27090-ai-security.md)) |
| **Retired fallbacks** | Staff and processes no longer able to run without the model | Incident response is constrained: the system cannot be switched off when it misbehaves |

## What springs the trap

- An erasure or objection request that can only be honoured by retraining.
- A finding that the training lacked a lawful basis.
- Reclassification of the supplier's data, or a change in export-control rules.
- A provider-side suspension or restriction of access.
- A security incident affecting the weights or the training pipeline.

In each case the required response (stop, retrain, withdraw) collides with operational dependence.

## Controls that keep the two limbs apart

| Control | Practice |
|---|---|
| Ask whether the data needs to enter the parameters | Prefer retrieval over a governed repository for sensitive material. Rosenberg lists embedding as one of the irreversible routes, so vector stores still need deletion and access controls |
| Keep the adaptation separable | Versioned adapters distinct from the base model; dataset manifest; ability to retrain without a given source |
| Minimise before training | Filtering and pseudonymisation at the dataset stage; record the decision |
| Contract for exit first | Rights in adapted weights; escrow or portability where lawful; deletion on termination; no-training commitment for inference data |
| Keep a tested fallback | Manual process or alternative model, exercised, for every process that must continue |
| Name an owner | One accountable person per model; reversibility assessment recorded in the AI inventory and revisited on change |

## Framework mapping

- [AI model lawfulness checklist](../resources/checklists/ai-model-lawfulness-checklist.md): sections A, B and D.
- [Breach liability regimes: UAE, DIFC, ADGM, India](../resources/frameworks/breach-liability-regimes-uae-difc-adgm-india.md): a weight leak may be a notifiable breach if personal data is recoverable.
- [Cybersecurity of sensitive non-personal data](../analyses/sensitive-non-personal-data-security.md): weights as a protected asset.

**Related reading:** [Inference, feedback and irreversibility — reading note](../analyses/inference-feedback-irreversibility-reading-note.md)

## Caveats

- The scenario is invented to illustrate the concept. No real organisation is described.
- The concept is Rosenberg's; the mapping to fine-tuning and inference, and the control list, are this hub's analysis.
- Page reference taken from the print edition.

## Sources

- S. Rosenberg, *Practical AI Governance: Building a Program for Oversight and Strategy* (Kogan Page, 2026), p. 274
- N. Watson and A. Hessami, *Safer Agentic AI: Principles and Responsible Practices* (Kogan Page, 2026), pp. 244 and 246 (inference data reused for training; governance assumptions about static systems)
- B. Christian, *The Alignment Problem* (UK paperback), pp. 262, 264 (learning from human feedback)
- European Data Protection Board, Opinion 28/2024 on AI models (17 Dec 2024)
