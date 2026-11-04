# Cloud DPIA checklist

**Source:** [GCP DPIA summary](../../analyses/gcp-dpia-summary.md) (Dutch government / Privacy Company, June 2026). Adapt the transfer section to your jurisdiction.

## 1. Scope and data model
- [ ] Services in scope listed by name and version (IaaS/PaaS/SaaS components)
- [ ] Personal data classified into **Content, Account, Diagnostic/Telemetry, Support, Website**
- [ ] Data flows documented per category, including provider-side logging and telemetry

## 2. Roles
- [ ] Provider's role (processor / controller / joint controller) established **per data category**
- [ ] Any provider "controller" claim for diagnostic or account data challenged and justified in writing
- [ ] DPA / data-processing terms reviewed against GDPR Art. 28 (or local equivalent)

## 3. Residency and transfers
- [ ] Region selection and data-location controls configured and evidenced
- [ ] Transfer mechanism identified (adequacy/DPF, SCCs/IDTA, other) with fallback documented
- [ ] Transfer Impact Assessment completed; see [transfer-risk-reassessment](README.md)
- [ ] Support-access and remote-access paths from outside the region assessed

## 4. Security and confidentiality
- [ ] Encryption at rest and in transit confirmed; **customer-managed keys** evaluated or enabled
- [ ] **Confidential computing** options evaluated for sensitive Content data
- [ ] Admin access governance: MFA, least privilege, access logging, periodic review

## 5. Retention and telemetry
- [ ] Log and telemetry retention periods set to the minimum needed
- [ ] Optional telemetry disabled where not required
- [ ] Provider retention/deletion commitments for each data category documented

## 6. Rights and transparency
- [ ] Process for data-subject requests covering data held in the platform
- [ ] Privacy notice updated for cloud processing and any sub-processors

## 7. Residual risk
- [ ] Each identified risk paired with a mitigating measure and owner (provider or customer)
- [ ] Residual risk rated; any high residual risk escalated (prior consultation where required)
- [ ] Review date set (and trigger events: new service, provider terms change, legal change)
