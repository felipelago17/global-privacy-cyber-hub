# EDPB Opinion 28/2024 on certain data protection aspects of AI models (17 December 2024)

`EU · GDPR · AI governance · Anonymisation · Legitimate interest`

## Source

- **Title:** Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models
- **Author:** European Data Protection Board (EDPB), adopted at the request of the Irish DPC under GDPR Article 64(2)
- **Date:** 17 December 2024
- **Link:** see [`resources/papers/links.md`](../resources/papers/links.md)

## Summary

The Opinion answers four questions: when an AI model trained on personal data can be considered anonymous; how legitimate interest can be used as a lawful basis in the **development** phase; how it can be used in the **deployment** phase; and what the consequences are if a model was developed with unlawfully processed personal data.

## Key findings

### 1. AI models are not automatically anonymous

- A model trained on personal data **cannot be assumed anonymous**. Anonymity must be assessed **case by case** by the supervisory authority.
- The test is whether personal data can be extracted from the model — either **directly** (e.g. from parameters) or **probabilistically** (e.g. via queries / membership inference) — taking into account **"all the means reasonably likely to be used"** by the controller or a third party.
- Controllers should document: the design choices (source selection, minimisation, filtering, pseudonymisation), robustness against extraction attacks, and the test results that support an anonymity claim.

### 2. Legitimate interest — the three-step test

The EDPB restates the test and applies it to AI:

| Step | Development phase | Deployment phase |
|---|---|---|
| **(a) Legitimate interest pursued** | Must be lawful, clearly articulated, real and present (e.g. developing a conversational assistant; fraud detection) | Same; the interest of the deployer may differ from the developer's |
| **(b) Necessity** | Is processing the data necessary to achieve the interest? Could less data or less intrusive means suffice? | Same test on the deployment processing |
| **(c) Balancing** | Data subjects' interests, fundamental rights, and **reasonable expectations** (was the data publicly available? what was the context of collection? is web-scraping involved?) | Impact of model outputs on individuals; risks of inference, discrimination, re-identification |

- **Reasonable expectations** are central: data scraped from the web may fall outside what individuals expect, especially where the collection context differs from the use.
- **Mitigating measures** can tip the balance: technical measures (pseudonymisation, output filters, unlearning), transparency measures (public notices beyond the Article 14 minimum), and measures facilitating rights (opt-out before training, easy objection).

### 3. Consequences of unlawful development

Three scenarios:

1. Same controller develops and deploys with unlawfully processed data — the deployment lawfulness is affected; authorities may order deletion, retraining or other corrective measures.
2. Different controller deploys — the deployer must assess the model's lawfulness as part of its own accountability.
3. The model has been **genuinely anonymised** after unlawful development — GDPR may no longer apply to the model itself, but the authority can still act on the original processing.

## Practical implications

- Do not claim a model is anonymous without an **extraction-risk assessment** on file.
- Build a **documented LIA** for both development and deployment; the EDPB expects the two phases to be assessed separately.
- Deployers of third-party models should request **provenance and lawfulness evidence** from vendors; "we didn't train it" is not a defence.
- Opt-out mechanisms before training and public-facing transparency notices are now expected elements of the balancing test, not optional extras.

## Open questions / critique

- The Opinion offers principles rather than bright-line thresholds for anonymity; practical robustness benchmarks are left to controllers and authorities.
- Interaction with the EU AI Act's GPAI obligations (training-data summaries, copyright policy) is only implicit; a combined compliance map is still needed.

## Source notes

Summary prepared from the EDPB Opinion as published. The three-scenario structure in section 3 follows the Opinion's own framing.
