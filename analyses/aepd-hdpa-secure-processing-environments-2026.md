# AEPD and HDPA: Secure Processing Environments from the data protection perspective (Nov 2026)

`Secure processing environments · DGA · EHDS · GDPR · Cloud and sovereignty · Privacy-enhancing technologies · Source: DPA guidance`

Status as of 18 Nov 2026. This page summarises one 44-page PDF titled *Secure Processing Environments from the Data Protection Perspective*, dated November 2026, prepared jointly by the Spanish Data Protection Authority (AEPD, Technological Innovation Division) and the Hellenic Data Protection Authority (HDPA, Research and Studies Dept.). Named reviewers come from Eurostat, the Italian Garante, Spain's Ministry for Digital Transformation and the UK ICO. I read the full text of the copy supplied to me. I did not check whether it is published on the AEPD or HDPA websites, and the document itself calls itself "initial guidance" that is not an exhaustive statement of requirements. It is not an EDPB opinion and I would not treat it as binding.

## What it says in one paragraph

A secure processing environment (SPE) lets the body that provides it control and supervise every processing action, so that legal compliance and digital sovereignty do not depend on promises from the data user. The authorities stress that an SPE is a bundle of legal, organisational and technical measures, not a product; that it does not displace the GDPR; and that the provider must keep real (de facto) control, not just contractual control, including when a cloud or other third party runs the infrastructure.

## Legal anchors

- **Data Governance Act (Reg. 2022/868).** Art. 2(20) defines an SPE. Art. 5(3)(b) and (c) allow public bodies to require re-use of protected data remotely inside an SPE they provide or control, or on secure premises. The document reads SPEs as the way to move from "sharing" to "access" (art. 2(10) versus 2(13)).
- **European Health Data Space (Reg. 2025/327).** Art. 73 requires secondary use of health data to happen only inside an SPE run under a Health Data Access Body (HDAB), with no download of personal data, access limited to permit holders, auditable logs kept at least a year, and only checked, anonymous outputs leaving. Art. 74 allocates roles: the HDAB is controller for its own tasks and processor for the data user, who is controller; the trusted data holder acts as processor for the user.
- **Data Act (Reg. 2023/2854).** Art. 4(6) confidentiality measures for trade secrets are described as alluding to SPE-style safeguards, though the Act does not name SPEs.
- **GDPR** applies in full, including accountability (art. 5(2)), data protection by design, and a DPIA under art. 35, which the document says is generally required because SPEs typically serve high-risk processing.

## Points most relevant to compliance work

1. **Control must be effective, not nominal.** A third party running an SPE does not automatically become a processor, and the HDAB's responsibilities cannot be moved to it by contract alone. Where a provider can access or process data independently, especially if subject to non-EEA law, the safeguards must be more robust than those asked of a data user.
2. **Certification is not enough.** Third-party security certification alone does not meet DGA and EHDS requirements; continuous monitoring, audit capability and technical enforcement are needed. Art. 73(3) EHDS requires regular audits with corrective measures.
3. **Vendor lock-in and concentration.** Two complementary safeguards: keep SPE components substitutable across providers, and spread critical functions so no single third party holds technical control of the whole SPE. The text cites a 2026 Dutch authorities' paper (ACM, AFM, AP, DNB, RDI) for the lock-in point.
4. **Cloud caution.** The document expects cloud to be attractive but says choosing a cloud provider instead of a public body or research institute needs careful justification. It flags gatekeeper bargaining power and information asymmetry, and lists provider characteristics to weigh in the risk analysis: exposure to non-EU law and intelligence services, international transfers, access to keys and authentication data, high privileges, dominant market position, continuity and the difficulty of investigating breaches.
5. **International transfers** under GDPR Chapter V must be addressed where third-country providers or access are involved.
6. **Precautionary principle by design and the Five Safes** (safe projects, people, settings, data, outputs, after Ritchie 2017) are offered as the planning frame, combined with a risk method and DPIA.
7. **Roles under the DGA are not fixed.** The EHDS role map is a guide, but outside health each SPE needs its own assessment of controller, joint controller and processor roles, documented, including who handles breaches and data subject requests.

## Measures (Section III.A)

Nine control families: governance and accountability; data management; identity management and access control; physical security; network and communications security; system and application security; audit, logging and monitoring; incident response, recovery and resilience; management of third parties. The closing reflections add zero-trust architecture, continuous verification, and a DPO or data protection adviser in the governance framework, with DPIAs integrated into design and operation.

## Data protection engineering (Section III.B)

- **SPEs versus TEEs.** A trusted execution environment can be a building block but is not itself an SPE: TEE internals are often closed and vendor-specific, remote attestation may be opaque, side-channel attacks exist, and TEEs focus on security rather than the other data protection principles.
- **Techniques covered:** homomorphic encryption, secure multi-party computation, polymorphic encryption and pseudonymisation, oblivious pseudonymisation, differential privacy, federated learning. None is called a panacea; suitability must be assessed in context.
- **Section III.C** maps threats to measures.

## Use case (Section IV)

A research consortium wants a linear regression of allostatic load (a stress biomarker) on age, sex, ZIP code and socioeconomic status, using data from hospitals, registries and statistical offices through an HDAB-run SPE. The document analyses linkage risks and shows a six-step homomorphic-encryption workflow (agreement and setup, key management, sending encrypted data to the HDAB, secure computation, sharing results, analysis and reporting) in which neither the SPE provider nor the researchers see the original data.

## Why a privacy and cyber hub should care

- It is the clearest statement I have seen from two DPAs that **contractual assurance plus certification is not control**, which bears on any cloud-hosted sensitive-data environment, not only health. Compare [cloud centrality](cloud-centrality-menace-technollama-2026.md), [NIS2 supplier security](nis2-supplier-security-contract-negotiation-computing-2026.md) and [EU–US AI sovereignty](eu-us-ai-sovereignty-contest-kennedys-2026.md).
- The substitutability and anti-concentration points are practical exit-plan and architecture requirements for vendor reviews.
- The "what is legally prohibited should also be technically prevented" idea matches the AI-agent controls in [agent security three layers](agent-security-three-layers.md).
- Its treatment of SPEs for sensitive data connects to [sensitive non-personal data security](sensitive-non-personal-data-security.md) and to confidential-inference approaches that rely on TEEs.

## Gaps and cautions

- Guidance from two national authorities, described as initial and non-exhaustive; no enforcement force of its own.
- I did not verify the cited articles against EUR-Lex, or the 2026 references it cites (the Commission's COM(2026) 503 and the Dutch authorities' paper), or the TEHDAS2 specifications it mentions. Citations here are the document's own.
- I did not confirm where the document is published or whether a final version differs from the copy I read.
- This page paraphrases and does not reproduce the text; read the PDF for exact wording.
