# Inference, feedback and irreversibility — reading note on four books (2021–2026)

`AI governance · Inference vs fine-tuning · Profiling · Feedback as training data · Vendor dependence`

## Source

| Book | Pages used |
|---|---|
| Brian Christian, *The Alignment Problem: How Can Artificial Intelligence Learn Human Values?* (UK paperback; publisher and year to be confirmed from the copyright page) | 261–265, 271, 274 |
| Nell Watson and Ali Hessami, *Safer Agentic AI: Principles and Responsible Practices* (Kogan Page, 2026) | 243–244, 246, 248–249 |
| Shoshana Rosenberg, *Practical AI Governance: Building a Program for Oversight and Strategy* (Kogan Page, 2026) | 274 |
| Nigel Toon, *How AI Thinks* (Torva, 2024) | 35–38 |

- **Type:** Reading note from print editions. Page numbers are from the copies read; paraphrased throughout.

## Summary

Read together, the four books make one point that privacy and security programmes tend to miss: "inference" is not a passive, stateless event. It produces new information about people, it generates feedback that can train the next model, and the organisation that relies on it can become unable to switch it off. The line between using a model and changing one has to be drawn by contract and configuration, because the technology does not draw it.

## Key points

### 1. Inference creates personal data
- Christian (p. 274) notes that assistants serve two masters, the nominal owner and the organisation that built them, and that they draw inferences about people that those people may not want drawn.
- **Privacy reading:** preference models and behavioural inferences are new personal data created at runtime. Purpose limitation and profiling rules apply even when no model weights change.

### 2. Feedback is a training signal
- Christian (pp. 262, 264) describes research in which a system infers what people want from their ratings of, or choices between, samples of its behaviour, then improves towards that inferred goal.
- Watson and Hessami (p. 244) note that reasoning systems can generate data during inference that is then used to train the model further.
- **Privacy reading:** thumbs-up/down, corrections and reasoning traces are training data. A "no training on customer data" term needs to say whether it covers them.

### 3. The boundary moves
- Watson and Hessami (p. 246) identify separate scaling dynamics for training, fine-tuning and test-time compute, and warn that governance built on static, predictable systems may be flawed.
- **Programme reading:** an "inference-only" entry in an AI inventory is a statement about a configuration on a date. It needs a change-control trigger.

### 4. Oversight works better when continuous
- Christian (p. 271) recounts that failures in learning from human feedback tended to disappear when feedback was interleaved through training, and (p. 265) that a known ground truth lets developers check how well a learned objective matches the intended one.
- **Assurance reading:** evaluate continuously, and test against verifiable answers where they exist.

### 5. Irreversibility plus dependence
- Rosenberg (p. 274) defines the irreversibility trap. See the hub's [case study](../case-studies/irreversibility-trap-fine-tuning.md).

### 6. Why outputs are probable, not certain
- Toon (pp. 36–38) explains the shift from deductive expert systems to inductive learning. Inductive systems give probable answers, which is the structural reason verification controls are needed; see [Mata v. Avianca](../case-studies/mata-avianca-aba-512-ai-citations.md).

## Implications for compliance programmes

| Area | Action |
|---|---|
| DPIA | Treat inferred preferences and profiles as outputs to be assessed, not only the prompts going in |
| Contracts | Define "training" to include feedback signals, reasoning traces and evaluation data |
| Inventory | Record learning behaviour and review it on every provider or configuration change |
| Security | Operational data can become training data; monitor for poisoning through feedback channels (see [ISO/IEC 27090](../resources/frameworks/iso-27090-ai-security.md)) |
| Resilience | Test fallbacks before dependence forms |

## Caveats

- Books for a general or practitioner readership; they explain concepts and are not legal authority.
- The Christian edition's publisher and year were not visible in the copy photographed.

**Related:** [EDPB Opinion 28/2024 on AI models](edpb-ai-models.md) · [DIFC Regulation 10](difc-regulation-10-lifecycle.md)

*Reading note prepared 13 November 2026. Not legal advice.*
