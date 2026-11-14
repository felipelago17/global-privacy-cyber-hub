# Case study — Explainable AI for disease classification: 105 studies, none clinically ready (Memon et al., 2026)

`Healthcare · Explainable AI · Clinical decision support · EU AI Act · GDPR · Validation and reproducibility`

## Summary

A systematic review in *BMC Medical Informatics and Decision Making* (2026) looked at 5,005 machine-learning disease-classification studies published between January 2019 and December 2025. Of those, 105 used explainable AI (XAI). The authors scored the 105 against a 13-item checklist built on the CLIX-M framework and the XAI 2.0 manifesto. No study met all 13 items. Explanations were rarely tested, rarely checked with clinicians and rarely validated outside the development setting. For a privacy, cyber or compliance team this is a case about evidence: "explainable" is often claimed in clinical AI, and the review shows how seldom the claim is tested.

This is a literature review, not an incident. It sits in this hub because the gap it measures is the same one regulators and auditors will ask about: can the organisation show that a system's explanations are accurate, stable and usable by the person who has to rely on them?

## Key facts

| Item | Detail |
|---|---|
| Paper | Memon, S. A., Ebrahimi, A., Shaikh, M. & Wiil, U. K. (2026). *Explainable AI-based techniques for disease classification: a systematic review and future work.* BMC Med Inform Decis Mak 26:455. DOI 10.1186/s12911-026-03750-4. Open access (CC BY-NC-ND 4.0) |
| Method | Systematic review following Kitchenham and Charters; four databases; studies from 2019 to 2025 |
| Scope | 5,005 ML/DL disease-classification studies screened; 105 used XAI |
| What was in the 105 | 49 datasets or data sources, 131 models across 12 architecture families, 27 distinct XAI techniques |
| Dominant approach | Gradient-based heatmaps for imaging models (Grad-CAM and variants) were the most common family, in 78 studies |
| Study design | About 80% retrospective |
| Explanation evaluated | 9 of 105 studies (8.5%) measured whether their explanations were accurate or useful |
| Clinical validation | Fewer than 25% reported any; the most common form was experts judging whether a heatmap matched the disease. Two studies ran reader or usability studies and one tested a tool as a decision aid |
| Source code | About 10% shared code |
| Readiness checklist | Mean score 9.07 of 13 (about 70%); no study met all 13 items. Lowest: stating the intended clinical user and use, testing explanation robustness, human-centred evaluation, and discussing risks and misuse |
| Funding | Horizon Europe (WISDOM project); University of Southern Denmark open-access funding |

## What the review found

- **Performance is not the problem.** Many imaging studies report accuracy and AUC above 95%. The review treats that as evidence about the model, not about whether a clinician can rely on its explanation.
- **Explanations are shown, not tested.** Heatmaps are the default output. Few studies check them against expert annotations, perturbation tests or clinician feedback.
- **Weak validation settings.** Single-centre, public and retrospective datasets dominate. Several studies report AUC of 0.97 to 1.00 internally, while two studies with external validation saw AUC fall to 0.69–0.76; the authors raise leakage and overfitting concerns where accuracy is very high.
- **Poor reproducibility.** With about one study in ten sharing code, independent checking is rarely possible.
- **Risk language is missing.** The most-missed checklist theme was stating the risks and limits of the explanation itself.

## Why it matters for privacy, cyber and compliance programmes

- **Transparency duties need evidence.** Where an AI system supports a clinical decision, the duty to give meaningful information about how it reaches outputs (GDPR Articles 13–15 and 22 where they apply; AI Act transparency and human-oversight requirements for high-risk systems) is only as good as the explanation the system produces. An explanation nobody has tested is a weak basis for either.
- **False confidence is a harm.** The authors note that post-hoc explanations can be unstable or misleading. A control that reassures without being checked can be worse than none, because it changes how much a clinician checks the output.
- **Health data raises the stakes.** The datasets are health data, usually special-category data under the GDPR. Single-site, narrow-demographic training sets are also a bias and accuracy risk that surfaces in deployment, not in the paper's headline metric.
- **Reproducibility is a security and assurance issue.** Without code and documented pre-processing, a deployer or auditor cannot re-run the claims, review the supply chain or reproduce a failure.
- **Procurement.** A vendor statement that a tool is "explainable" or "validated" should be met with the same questions the review asks: explained to whom, tested how, validated where, with what failure modes disclosed.

## Framework mapping

This is the hub's mapping of the review's findings; it is not drawn from the paper and is not legal advice.

| Finding | Hub lens |
|---|---|
| No explanation testing | AI governance: documented testing of transparency measures; see [medical-AI Act safeguards](../analyses/medical-ai-act-safeguards.md) |
| Internal vs external performance | Accuracy and robustness expectations for high-risk AI; post-deployment monitoring |
| No intended-user statement | Purpose specification and DPIA scoping; human-oversight design |
| Missing risk disclosure | DPIA and AI risk register content; user instructions |
| Little shared code | Third-party and supply-chain due diligence; auditability |

## Controls to take from it

| Control | Practice |
|---|---|
| Ask for explanation evidence | Request tests of explanation faithfulness and stability, not only model accuracy |
| Require external validation | Ask for results on data from sites and scanners that were not used in development |
| Involve the clinical user | Record that intended users reviewed explanations, and what they changed |
| Name the user and use | State who relies on the output and for what decision before approval |
| Disclose limits | Put known explanation failure modes into the DPIA and the user documentation |
| Check reproducibility | Prefer vendors and research that share code and pre-processing steps, or accept an independent re-run |
| Monitor after go-live | Track explanation drift and clinician override rates, not just accuracy |

## Caveats

- The review's checklist is the authors' own, adapted from CLIX-M. The authors say the score reflects reported evidence of readiness, not proof that a system is ready for clinical use.
- Quality assessment used a single reviewer with predetermined criteria; no inter-rater agreement was computed. Only English-language studies from four databases were included.
- The paper's counts of external validation differ by place: the abstract gives 21.0%, Table 8 lists 14 studies with external validation, and Table 9 lists four external-cohort studies among 22 across all clinical-validation types (also about 21%). Check the table before citing a figure for external validation specifically.
- The legal references in this note are general pointers. Check the Regulation text and your own legal advice for how GDPR and the AI Act apply to a specific system.
- The paper is licensed CC BY-NC-ND; this note paraphrases findings and does not reproduce its text or tables.

## Sources

- Memon, S. A., Ebrahimi, A., Shaikh, M. & Wiil, U. K. (2026). Explainable AI-based techniques for disease classification: a systematic review and future work. *BMC Medical Informatics and Decision Making*, 26:455. <https://doi.org/10.1186/s12911-026-03750-4>
- LinkedIn summary post of the paper (Nov 2026), used to find the paper; all figures above were checked against the paper itself.
