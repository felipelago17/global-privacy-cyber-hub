# SAMA quantum readiness circular: cryptographic inventory and risk assessment (Aug 2026)

`Saudi Arabia · SAMA · Quantum risk · Post-quantum cryptography · Financial sector · Cryptographic inventory · Source: consultancy paraphrase and trade press`

Status as of 22 Nov 2026. I have not read SAMA's circular. The page rests on (1) a tool-generated summary of a consultancy's campaign page that paraphrases it, and (2) search excerpts from trade and law-firm sites. The consultancy page is promotional and says the circular, on the SAMA Rulebook, is the authority. Check the circular text before relying on any requirement or date.

## The source

The page at <https://quantum-readiness.ahad-me.com/> belongs to AHAD, a consulting firm, and is not SAMA's publication. It describes SAMA Circular 482021280 on quantum readiness, issued 27 Aug 2026. Trade-press excerpts (PostQuantum.com, Quantum Zeitgeist) give the same issue date and the 31 Dec 2026 inventory deadline, and PostQuantum.com says SAMA issued it under its powers in the Saudi Central Bank Law. An Okaz excerpt (Arabic) says SAMA required institutions to take four measures, which matches the four requirements below.

## Who it covers

Per the AHAD summary: banks, finance companies, payment services companies, credit information companies and licensed finance-support entities. It says insurers are not on the distribution list, advises checking the list in unclear cases, and names SAMA's Executive Department of Operational Resilience Control as the contact.

## Requirements and deadlines (as paraphrased)

| # | Requirement | Deadline |
|---|---|---|
| 1 | **Classify cryptographic assets:** identify and classify all of them; map the data, systems and services each protects; classify by sensitivity and migration priority; assess resilience of priority assets; record constraints, challenges and third-party dependencies | 31 Dec 2026 (end Q4 2026) |
| 2 | **Enterprise quantum risk assessment**, inside the existing enterprise risk process, covering at least operational, legal, regulatory and strategic risk; name the skills and staffing needed; produce action plans, not only findings | 31 Mar 2027 (end Q1 2027) |
| 3 | **Resilience plans** for every priority asset, using quantum-resistant cryptography or a suitable alternative where it is not available | No date given |
| 4 | **Governance and reporting:** monitor quantum risk periodically; report to the Information Security Supervisory Committee and, where one exists, the board Risk Committee; send challenges and recommendations to the board or equivalent | Continuing |

The AHAD page notes the inventory deadline falls before the risk assessment even though the circular lists the assessment first. A LinkedIn practitioner summary reads the plan as risk-based migration rather than a big-bang replacement, which is that author's interpretation.

## Algorithms and reporting

- Per the AHAD page, SAMA names no specific algorithms. It says the National Cybersecurity Authority (NCA) sets algorithm choices in Saudi Arabia, and that the international reference set is NIST's (ML-KEM, ML-DSA, SLH-DSA). One trade-press excerpt mentions a draft listing ML-KEM and ML-DSA, and I could not tell from the excerpt which document it means, so treat that point as unresolved.
- No submission to SAMA is required and no format is prescribed. Reporting is internal, so evidence must satisfy the institution's own governance.

## External dates the AHAD page cites (unverified)

NIST IR 8547 (112-bit RSA and elliptic curve deprecated after 2030, quantum-vulnerable public-key cryptography disallowed after 2035), an EU roadmap (critical infrastructure by 2030), UK NCSC (priority migrations by 2031) and the G7 Cyber Expert Group (critical systems 2030–2032). The page says these are standards timelines that do not depend on predicting when a quantum computer arrives. I have not verified them.

## Context from search excerpts

- PostQuantum.com argues the 31 Dec inventory deadline is tight for banks starting from zero and says SAMA's circular follows a Jan 2025 Bank of Israel directive. These are the author's views and claims.
- Quantum Zeitgeist describes SAMA as mirroring a coordinated global push and calls inventory the most critical first step; the first hurdle many face is simply knowing what cryptography they hold.
- The BIS paper "Quantum-readiness for the financial system: a roadmap" (BIS Paper 158, July 2025) also stresses starting now, with awareness and cryptographic inventory as foundations.
- A Deloitte note describes Swiss FINMA Guidance 05/2026 with a mid-2027 deadline, pointing to a wider regulatory trend (not read in full).

## Why a privacy and cyber hub should care

- **Harvest now, decrypt later.** Data encrypted today with quantum-vulnerable public-key methods and kept for years is the exposure that drives inventory and migration. Long-retention personal and financial data is the obvious example, which links this to retention and minimisation work.
- **Cryptographic inventory as a control.** An inventory tied to the data and systems each asset protects is also useful for incident response, transfer mapping and vendor due diligence. See the [Dragos canary-token analysis](dragos-ai-supply-chain-canary-tokens-2026.md) for a case where credentials and secrets leaked through third parties.
- **Third-party dependency.** The circular reportedly asks institutions to record third-party dependencies, which ties into supplier risk.
- **Governance model.** Risk-committee and board reporting mirrors what many cyber and privacy programmes already do. For another Saudi regulatory item, see the [SDAIA Responsible AI policy page](saudi-sdaia-responsible-ai-policy-clifford-chance-2026.md).

## Gaps and cautions

- Not read from the circular; a consultancy paraphrase and secondary excerpts. Scope, dates and the "no algorithms named" statement need confirming against the Rulebook text.
- The AHAD page promotes its own services and self-assessment tool.
- Whether the circular applies to a given institution depends on its licence and the distribution list.
- Not legal or regulatory advice.
