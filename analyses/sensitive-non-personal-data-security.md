# Cybersecurity of sensitive non-personal data — trade secrets, OT/process data, CUI, model weights and research data

`Non-personal data · Trade secrets · OT · CUI · Export controls · Model weights · Compute · Reasonable measures`

Prepared for the General Counsel Summit (Dubai, 12 Nov 2026), Session 3. Status as of 12 Nov 2026. Built from two practitioner notes, then checked against public sources; where a claim in the notes did not survive checking, it is corrected below and listed in the verification table.

## Why this belongs in a breach-liability session

Privacy law gives most programmes their notification clocks, regulators and fines, so security effort follows personal data. Attackers follow value. IBM's Cost of a Data Breach Report 2026 puts the global average at USD 4.99 million (up 12%), with intellectual property stolen or compromised in about 32% of breaches and described as the costliest type of breach. IBM also reports that attackers increasingly pressure victims by threatening to expose IP (31%) and that AI-enabled attacks are now about one in four malicious breaches. Verizon's 2026 DBIR (22,000+ confirmed breaches) found vulnerability exploitation overtook credential abuse as the top initial access vector (31%), with ransomware present in 48% of breaches. None of that is specific to personal data. The assets most worth stealing in energy, AI and industrial groups (process recipes, control logic, reservoir and grid models, designs, model weights, research datasets) often carry no personal data, so no privacy regime is triggered and no clock starts.

For a moderator the useful framing is: **the "reasonable security" question is asked under at least five different bodies of law, none of which is the privacy statute.**

## Five legal hooks for non-personal sensitive data

| Hook | What it asks | Source of the duty | Practical consequence |
|---|---|---|---|
| **1. Trade-secret "reasonable measures"** | Owner must take reasonable steps to keep information secret to qualify for protection | DTSA (18 U.S.C. § 1839(3)), UTSA; UAE trade-secret rules (see UAE note) | Weak security can defeat the owner's own claim. Courts treat technical controls as necessary but not sufficient: contracts, access limits and enforcement count too |
| **2. Critical-infrastructure risk management** | Appropriate and proportionate measures protecting confidentiality, integrity and availability of data held on network and information systems | NIS2 Art. 21 (energy is in Annex I); UAE CII Protection Policy (Sept 2025); NERC CIP, TSA directives (US) | Applies to operational data regardless of personal content; management-body accountability under NIS2 Art. 20 |
| **3. Government information safeguarding** | Implement prescribed controls for controlled information | CUI (EO 13556, 32 CFR 2002); NIST SP 800-171 Rev. 3; DFARS 252.204-7012 and CMMC | Contractual flow-down to suppliers; non-compliance can bring False Claims Act exposure |
| **4. Export controls on technical data and AI assets** | Control who can access or receive controlled technology, including by deemed export | EAR, ITAR; BIS controls on advanced chips; model weights (ECCN 4E091, status contested, below) | Security failure can itself be an export event; access architecture matters |
| **5. Contract, insurance and M&A representations** | Warranties of adequate security and no material incidents | JV agreements, SPAs, cyber policies | Where the loss actually lands for most GCs; ties directly to the Marriott/Yahoo diligence lessons |

## What courts actually require for trade-secret "reasonable measures"

- The standard is fact-specific and not absolute. A Fourth Circuit decision of 18 November 2025 reversed a pleading-stage dismissal and said measures need not be "absolute or heroic" (IPWatchdog summary).
- Technical controls alone have not been enough in several cases. A 2025 federal decision held that firewalls and passwords, without enforceable confidentiality commitments, did not establish reasonable safeguards (McGuireWoods). The Second Circuit (2022, *Turret Labs v. CargoSprint*) affirmed dismissal where the owner could not show confidentiality terms with vendors and end users. An Illinois court denied an injunction where the owner took almost no measures (CGW, 2019).
- Plaintiff trade-secret owners lose cases on this element. One review found about 14% of post-DTSA cases were dismissed on the pleadings or summary judgment, often on reasonable efforts (World IP Review, 2020).

Lesson for the panel: document the cybersecurity programme as evidence of reasonableness, and pair it with NDAs, access logs, offboarding and vendor terms. A breach that proves your controls were thin can cost you the legal protection as well as the data.

## Sector lenses

### National security
- **CUI** is the US government's umbrella for unclassified information needing safeguards (categories include Controlled Technical Information, Export Controlled and Critical Infrastructure information). Non-federal systems handling CUI implement NIST SP 800-171 Rev. 3 (final, 14 May 2024); the DoD has not necessarily moved contractors to Rev. 3 yet (check current DFARS/CMMC position).
- **Export-controlled technical data** is frequently CUI and adds nationality and access limits on top of baseline controls.
- **DOJ Data Security Program** (28 CFR Part 202, EO 14117) is a hybrid case: it restricts transfers of bulk US sensitive personal data and government-related data to countries of concern, so it straddles personal and non-personal categories. Not independently re-verified in this pass.

### Energy and OT
- NIS2 lists energy (electricity, oil, gas, hydrogen, district heating and cooling) as a sector of high criticality and Art. 21 sets all-hazards risk measures including cryptography, access control, supply-chain security and vulnerability handling.
- **Correction to the source notes:** the "trade-secret exfiltration is a significant incident" criterion comes from Commission Implementing Regulation (EU) 2024/2690, which applies to specified digital-infrastructure and ICT service providers (DNS, cloud, data centres, managed service providers and similar), not to energy operators. Energy entities rely on the general significant-incident test in NIS2 Art. 23(3) as transposed nationally. Best practice is still to write trade-secret exfiltration into your own incident criteria.
- NIST has released the initial public draft of SP 800-82 Rev. 4 (Guide to OT Security), listed on NIST's 2026 news page under 30 September 2026. NERC CIP-015 (internal network security monitoring) is cited in the notes and was not independently re-verified.
- Technical literature in the notes points to a real design tension: security operations centres need rich process telemetry, yet that telemetry can reveal recipes and timing. Proposed answers are anonymisation or non-invertible masking before data leaves the plant zone, and zone-and-conduit segmentation (IEC 62443, Purdue model).

### Medical and research data
- HIPAA stops applying to properly de-identified data (Safe Harbor or Expert Determination), yet the dataset may still be commercially precious and re-identifiable by AI linkage or genomics. Trade-secret law and contracts then do the protective work; a leak may trigger no notification duty at all.
- Synthetic or perturbed data eases sharing but does not remove the need to protect the original research assets.

### Computing power and model weights
- **RAND's playbook** (Nevo et al., 21 Nov 2024) defines five security levels, SL1 to SL5, mapped to attacker capability, and identifies 38 attack vectors. Recommended basics include centralising weights in access-controlled, monitored systems, reducing the number of people with access, and hardening model interfaces. A later RAND report extends the framework to algorithmic insights, which cannot be centralised the same way. The SL5 Task Force notes that current frontier practice does not reach SL5.
- IBM's 2026 report now measures AI-specific loss: more than 20% of organisations reported a breach targeting AI models or applications, and IBM lists a model-inversion attack cost as a distinct figure.
- NIST SP 800-234 (HPC security overlay on SP 800-53) is cited in the notes as a draft; not independently verified here.
- **Export-control status needs care.** The January 2025 AI Diffusion Rule created ECCN 4E091 for certain closed-weight models trained with more than 10^26 operations. In May 2025 BIS announced it would not enforce the rule and began rescission. Sources then diverge: Baker McKenzie described 4E091 as effectively removed, while Miller Chevalier's mid-2026 review says the rule had not yet been formally rescinded in the CFR, and a 2026 National Law Review piece says 4E091 and the model-weights foreign direct product rule remain on the books. Safe statement for the panel: *controls on model weights were announced, are not being enforced, and the formal legal position should be checked before relying on either answer.*

## UAE and regional angles

- **UAE Critical Information Infrastructure Protection Policy**, issued by the Cyber Security Council (17 Sept 2025), sets baseline security and resilience for CII; the National Cyber Accreditation Programme rollout in 2026 will restrict unaccredited providers for CII (Chambers 2026).
- **Dubai Law No. 15 of 2024** (Dubai Electronic Security Centre) covers information security, information systems and critical infrastructure for Dubai government and classified critical entities.
- **Trade secrets:** Chambers' *Doing Business in 2026* cites Federal Decree-Law No. 26 of 2020 on trade secrets, with possible criminal liability under the Cybercrime Law (FDL 34/2021) where electronic systems are used. I could not confirm that instrument number against the official portal; check it before citing.
- **National Encryption Policy** was announced by the UAE Cybersecurity Council with an executive regulation; relevant to NIS2-style encryption expectations. Details not reviewed.
- Mainland PDPL, DIFC and ADGM regimes remain personal-data regimes; see the [breach liability note](../resources/frameworks/breach-liability-regimes-uae-difc-adgm-india.md).

## Control themes that recur across all regimes

Data classification that covers non-personal assets; least privilege and strong authentication; encryption at rest and in transit; segmentation (IT/OT zones, HPC enclaves); exfiltration monitoring and DLP tuned to non-PII patterns; vendor and supply-chain access control; documented risk management; and incident criteria that name trade-secret and operational-data exfiltration. Where regimes conflict, build to the strictest applicable one and keep availability and safety first in OT.

## Questions for the panel (Session 3)

1. If a breach exposes no personal data, who in your organisation decides whether it is reportable, and on what test?
2. Would your current security record survive a "reasonable measures" challenge in a trade-secret case against a departing employee or supplier?
3. In an M&A or JV data room, how do you diligence security of the target's non-personal crown jewels (process data, models, designs)?
4. Where do SOC, cloud and AI-vendor flows cross OT or R&D zones, and who approves them?
5. For model weights and training data, which security level are you aiming for, and who can show evidence?

## Verification of claims taken from the source notes

| Claim in notes | Result |
|---|---|
| IBM 2026: global average USD 4.99m, +12%; IP in about 32% of breaches; AI-enabled attacks +56% | **Confirmed** (IBM, FM Magazine, eSecurity Planet) |
| IP is the costliest data type | **Confirmed** (FM Magazine). The "USD 196 per record" figure and the "March 2025 to February 2026" period were **not found**; omit unless checked against the report |
| Verizon DBIR 2026: exploitation top vector at 31%, ransomware in 48% | **Confirmed** by most sources; one outlet reported 36%, so use 31% |
| NIS2 Annex I covers energy; Art. 21 measures | Consistent with the Directive; primary text not re-fetched here |
| Trade-secret exfiltration is a "significant incident" under NIS2 implementing rules | **Corrected**: applies to CIR 2024/2690 digital providers, not energy entities |
| BIS controls on model weights apply (ECCN 4E091) | **Contested**: non-enforcement since May 2025; formal rescission status disputed by sources |
| NIST SP 800-171 Rev. 3 final | **Confirmed** (14 May 2024) |
| NIST SP 800-82 Rev. 4 draft | **Confirmed** as initial public draft (NIST 2026 news) |
| RAND SL1-SL5 | **Confirmed** (RAND, Nov 2024) |
| DTSA reasonable-measures case law | **Confirmed** at the level of the cases cited above |
| NERC CIP-015, DOJ DSP (28 CFR 202), SP 800-234, SP 1800-28/29, HIPAA de-identification, DFARS/CMMC details | **Not re-verified** in this pass |

## Sources

- IBM, Cost of a Data Breach Report 2026: https://www.ibm.com/reports/data-breach and press release https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled,-costing-companies-6-million-on-average
- FM Magazine on the IBM report: https://www.fm-magazine.com/news/2026/aug/data-breach-costs-climb-as-ai-powered-attacks-surge/
- Verizon 2026 DBIR coverage: https://www.scworld.com/news/verizon-dbir-2026-vulnerability-exploits-top-initial-access-as-patching-coverage-falls ; https://dbugs.ptsecurity.com/news/verizon-dbir-2026-exploitation-of-vulnerabilities-becomes-the-leading-initial-access-vector-20260526
- Commission Implementing Regulation (EU) 2024/2690: https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj/eng ; Hunton summary https://www.hunton.com/privacy-and-cybersecurity-law-blog/implementing-regulation-developing-nis2-rules-for-certain-digital-service-providers-enters-into-force
- NIST SP 800-171 Rev. 3: https://csrc.nist.gov/news/2024/updated-security-requirements-for-protecting-cui ; NIST 2026 news (SP 800-82r4 draft): https://csrc.nist.gov/News/2026
- BIS AI Diffusion Rule: Akin https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/bis-rescinds-ai-diffusion-rule-and-issues-new-guidance ; Miller Chevalier https://www.millerchevalier.com/index%2Ephp/publication/bis-export-controls-2025-year-review-and-2026-mid-year-update ; National Law Review https://natlawreview.com/article/choosing-between-us-and-chinese-ai-models-export-control-risks-both-sides
- RAND, Securing AI Model Weights: https://www.rand.org/pubs/research_briefs/RBA2849-1.html ; algorithmic insights report https://www.rand.org/content/dam/rand/pubs/research_reports/RRA4600/RRA4685-1/RAND_RRA4685-1.pdf ; SL5 Task Force https://securityandtechnology.org/sl5/
- Trade-secret reasonable measures: IPWatchdog https://ipwatchdog.com/2025/12/02/fourth-circuit-clarifies-reasonable-efforts-standard-dtsa-trade-secret-protection/ ; McGuireWoods https://www.mcguirewoods.com/client-resources/alerts/2025/6/passwords-arent-enough-the-critical-role-of-ndas-in-trade-secret-protection/ ; Crowell (Second Circuit) https://www.crowell.com/a/web/aAsAxiax3xMzJMT7vj6mMv/4Ttkb9/second_circuit_rejects_dtsa_claim_due_to_weak_software_licensing_agreement.pdf ; Taft (CGW) https://www.taftlaw.com/news-events/law-bulletins/best-practices-for-the-safeguarding-of-company-trade-secrets/
- UAE: CII Protection Policy https://uaelegislation.gov.ae/en/policy/details/critical-information-infrastructure-protection-policy ; Chambers Cybersecurity 2026 https://gpg-pdf.chambers.com/cybersecurity-2026/438/ ; Chambers Doing Business 2026 https://gpg-pdf.chambers.com/Doing-Business-In-2026/1060/ ; Dubai Law 15/2024 https://dlp.dubai.gov.ae/Legislation%20Reference/2024/Law%20No.%20%2815%29%20of%202024%20Concerning%20the%20Dubai%20Electronic%20Security%20Centre.html ; National Encryption Policy https://www.wam.ae/en/article/15w563h-uae-announces-approval-national-encryption-policy
