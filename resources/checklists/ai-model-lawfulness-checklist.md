# AI model lawfulness checklist (GDPR)

**Source:** [EDPB Opinion 28/2024](../../analyses/edpb-ai-models.md). Use for both models you develop and third-party models you deploy.

## A. Anonymity claim (only if you assert the model is anonymous)
- [ ] Extraction-risk assessment on file: direct extraction from parameters **and** probabilistic extraction via queries
- [ ] Assessment considers "all means reasonably likely to be used" by you and by third parties
- [ ] Design measures documented: source selection, minimisation, filtering, pseudonymisation
- [ ] Robustness testing against membership inference / data extraction attacks, with results
- [ ] Conclusion reviewed by someone independent of the development team

## B. Development phase — legitimate-interest assessment
- [ ] Interest articulated: lawful, clear, real and present
- [ ] Necessity: why this data, this volume, this method; less intrusive alternatives considered
- [ ] Balancing: data-subject impact, reasonable expectations (public availability, collection context, web-scraping), vulnerable groups
- [ ] Mitigations in place: technical (pseudonymisation, filters, unlearning capability), transparency (public notice beyond Art. 14 minimum), rights facilitation (pre-training opt-out, easy objection)
- [ ] Alternative lawful basis considered where LI fails (consent, contract, legal obligation)

## C. Deployment phase — separate LIA
- [ ] Deployer's own interest and necessity assessed (not inherited from developer)
- [ ] Output risks assessed: inference, discrimination, re-identification, profiling
- [ ] Human oversight and output controls documented

## D. Third-party models (deployer due diligence)
- [ ] Provenance and lawfulness evidence requested from vendor (training data sources, lawful basis, DPIA)
- [ ] Contractual warranties and audit/information rights on training-data lawfulness
- [ ] Assessment of consequences if the model is later found unlawfully developed (retraining, replacement, deletion)

## E. Governance
- [ ] DPIA completed where processing is likely high-risk
- [ ] Records of processing updated for development and deployment separately
- [ ] Interaction with EU AI Act obligations (GPAI training-data summary, high-risk duties) mapped
