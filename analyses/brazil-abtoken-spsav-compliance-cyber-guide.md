# Brazil — ABToken Regulatory Compliance Guide: Compliance and Cybersecurity Requirements for Virtual-Asset Service Providers (June 2026)

`Brazil · Virtual assets / tokenisation · Banco Central do Brasil · Cybersecurity · AML/CFT · Banking secrecy`

## Source

- **Title:** *ABToken Explica — Guia de Conformidade Regulatória: Requisitos de Compliance e Cibersegurança* (Regulatory Compliance Guide: Compliance and Cybersecurity Requirements)
- **Author / publisher:** Associação Brasileira das Empresas Tokenizadoras (ABToken), June 2026; 50 pp., Portuguese
- **Type:** Industry-association technical guide to the new Banco Central do Brasil (BCB) regime for *Sociedades Prestadoras de Serviços de Ativos Virtuais* (SPSAVs — virtual-asset service providers); informative, not legal advice
- **Link:** ABToken publications page (<https://abtoken.org.br/>); the PDF is not committed to this repository

## Summary

The guide walks tokenisation companies through the regulatory framework that brought Brazilian VASPs inside the National Financial System (SFN). The anchor is the package of **BCB Resolutions 519, 520 and 521 of 10 November 2025** (in force 2 February 2026), which implement Law 14.478/2022 (the crypto-assets legal framework) and make SPSAVs BCB-authorised institutions. The guide's framing: SPSAVs stop being peripheral and become financial-infrastructure entities, with entry and permanence requirements — authorisation, minimum capital, independent technical certification — in which "the quality of internal controls will be the main competitive differentiator".

Two features make it relevant to a privacy-and-cyber hub: the cybersecurity chapter imports the **BCB Resolution 85/2021** bank-grade cyber regime wholesale into the crypto sector, and the **banking-secrecy** extension (CMN Resolution 5.280/2026) changes the legal character of customer data held by VASPs.

## The regulatory package

| Instrument | Published | In force | Scope |
|---|---|---|---|
| BCB Res. 520/2025 | 10 Nov 2025 | 2 Feb 2026 | Constitution, operation and governance of SPSAVs — the central text |
| BCB Res. 519/2025 | 10 Nov 2025 | 2 Feb 2026 | Authorisation process and minimum capital |
| BCB Res. 521/2025 | 10 Nov 2025 | 2 Feb 2026 (certain FX provisions from 4 May 2026) | FX operations with virtual assets; international-capital rules |
| BCB Res. 552/2026 | 10 Nov 2025 | Immediate | Extends governance and cybersecurity rules (incl. Res. 85/2021, 65/2021, 93/2021, 28/2020) to SPSAVs |
| CMN Res. 5.280/2026 | 26 Feb 2026 | 1 Mar 2026 | Subjects SPSAVs to banking secrecy (Complementary Law 105) |
| BCB Normative Instructions 701, 704, 720, 739/2026 | 2026 | — | Independent technical certification; authorisation documents; endpoint monitoring; assurance of AML/CFT, fraud and sanctions controls |

## Chapter 1 — Compliance and governance (selected requirements)

- **Segregation** of client assets from the institution's own (Res. 520 Art. 12 and related), with documented, auditable processes.
- **Travel Rule** implementation under Res. 520 with IN 701/2026 — originator/beneficiary information exchanged in real time.
- **Self-custody wallet identification (KYT)** — Res. 552/2026 amends Res. 65/2021 so that transactions involving wallets outside the institution's environment require board-approved procedures and enhanced monitoring; mixers and obfuscation techniques are flagged.
- **AML/CFT (PLD/FT)** — Res. 520 Arts. 43–45; a dedicated internal-controls adherence structure (Res. 93/2021 as amended); record-keeping minimum **5 years**; monthly reporting to COAF.
- **Ombudsman channel** — responses within 10 business days; a monthly customer-relationship threshold of R$ 35,000 referenced for simplified relationships.
- **Operational prohibitions** — no credit extension or bank-like risk-taking; any referenced asset must be backed as represented.
- **Third-party and outsourcing management** (Res. 520 Arts. 32–36), business continuity, and transparency / disclosure policies.
- **IN 739/2026** — raises the maturity bar by requiring **assurance of AML/CFT, fraud and international-sanctions controls** as part of authorisation (initially for SPSAVs already operating); updates IN 704/2026's document list.
- **Banking secrecy** — CMN Res. 5.280/2026 Art. 1 equates SPSAVs to institutions bound by LC 105: customer data becomes secrecy-protected information with the corresponding disclosure regime, criminal exposure and information-sharing constraints — layered on top of the LGPD.

## Chapter 2 — Cybersecurity and technological resilience

The guide's premise is that in DLT environments cybersecurity *is* the asset: a lost private key or a fraudulent transaction is usually irreversible, so BCB imposed bank-grade standards.

| Requirement | Basis | Content |
|---|---|---|
| Cybersecurity policy and cloud governance | Res. 552/2026 extending **Res. 85/2021**; Res. 520 Art. 48 | Formal policy across the organisation; encryption at rest and in transit; cloud contracts must guarantee BCB supervisory access and compliance with Brazilian law; cybersecurity cannot be traded for operational agility |
| Independent technical certification | **IN 701/2026** Arts. 1–2 | A conclusive opinion from a qualified independent firm on infrastructure robustness and **private-key custody security** before operations start — an entry filter |
| Private-key management and cryptographic redundancy | Res. 520 Art. 48(VI); IN 701 | No single point of failure — multisig or MPC; disaster-recovery plans with key-compromise scenarios and automated migration |
| Multi-factor authentication | Policy-based | Mandatory for administrative access, critical environments, infrastructure consoles and transfers above internal thresholds |
| Penetration testing and vulnerability assessment | Res. 520 Art. 48(IV) | Periodic assessments, pentests proportionate to size/complexity; results classified and remediated |
| Endpoint and anomalous-event monitoring | Res. 520 Art. 48(II); **IN 720/2026** | Detection on all endpoints incl. development and production; code changes monitored and approved; data access only via secure APIs (no screen scraping or shared credentials) |
| API and integration security | Res. 520 | Authentication, encryption, access management, event monitoring proportionate to risk profile |
| Logs, audit and time synchronisation | Policy-based | Tamper-protected logs, access segregation, secure storage |
| Incident handling and rapid response | Cyber policy | Identification, classification, containment, treatment and recovery for critical systems and data |
| Hardening | Section 2.11 | Baseline configuration hardening |

## Chapter 3 — Accounting, tax and reporting; Chapter 4 — Strategic outlook

Chapter 3 covers COSIF accounting, tax and the monthly/periodic reporting layouts; Chapter 4 positions the regime as a maturity filter in which authorised, certified SPSAVs gain access to banking rails and institutional counterparties while unauthorised operators are pushed out.

## Why it matters for this hub

1. **Cyber regime by reference.** Brazil did not write a crypto-specific cyber rule; it extended the banking one (Res. 85/2021) and added crypto-specific items (key custody certification, KYT for self-custody). This is the same technique as the EU's DORA-plus-MiCA layering and a useful comparator for GCC virtual-asset regulators (VARA, ADGM FSRA, CBUAE).
2. **Pre-operation third-party certification of key custody** (IN 701/2026) is unusual and worth tracking as a model — it converts a security architecture question into a licensing precondition.
3. **Banking secrecy over crypto customer data** changes the privacy analysis: LC 105 secrecy is a distinct legal regime from LGPD personal-data protection, with its own disclosure gateways and criminal sanctions. Privacy programmes for Brazilian VASPs now run two registers.
4. **Sanctions assurance at authorisation** (IN 739/2026) is a rare example of a central bank requiring assured international-sanctions controls as a licensing input — relevant to the sanctions-screening work in the companion Sanctions-and-Export-Controls repository.

## Caveats

- Industry-association guide, not the regulator's text; article references should be checked against the BCB resolutions and normative instructions before reliance.
- Several normative instructions (701, 704, 720, 739/2026) were issued during 2026 and may have been amended since June 2026.
- Portuguese source; translations here are the hub's own.

**Related:** [Binance hack (Oct 2026)](../case-studies/binance-2026-hack.md) · [Frameworks index](../resources/frameworks/README.md) · [Global compliance maturity checklist](../resources/checklists/global-compliance-maturity.md)

*Reading note prepared 9 November 2026. Not legal advice.*
