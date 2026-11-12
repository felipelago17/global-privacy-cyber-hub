# ISO/SAE TR 8477:2026 — Road vehicles — Cybersecurity verification and validation

`International · Automotive cybersecurity · Technical Report · ISO/SAE 21434 · UNECE R155`

## At a glance

| Attribute | Detail |
|---|---|
| **Full title** | Road vehicles — Cybersecurity verification and validation |
| **Status** | **Under publication** — Edition 1, dated 2026-10, stage 60.00 on the ISO page ("final production steps, up to seven weeks"). Secondary sources (Nov 2026) describe it as already published; confirm stage 60.60 on ISO before citing it as published |
| **Committee** | ISO/TC 22/SC 32 (Electrical and electronic components and general system aspects), working group WG 11 (Cybersecurity); developed jointly with SAE |
| **Type** | Informative **Technical Report** — not a normative standard, not certifiable, no mandatory methods or fixed test checklist |
| **Scope (ISO abstract)** | Considerations on the planning and execution of verification and validation (V&V) of the cybersecurity of items and components of road vehicles, in the context of ISO/SAE 21434 |
| **Primary source** | ISO landing page: <https://www.iso.org/standard/83188.html> |

## What it covers

ISO/SAE 21434:2021 sets high-level V&V requirements but says little about how to plan, scope or evidence them. TR 8477 fills that gap with guidance on *what evidence is needed and how to organise the work*, rather than prescribing techniques. Its core message is that cybersecurity assurance should rest on structured, traceable V&V linked to the threat analysis, requirements and architecture, rather than on an isolated test such as a single penetration test.

### Verification versus validation

| | Verification | Validation |
|---|---|---|
| **Question** | Does the architecture, design or implementation meet the specified cybersecurity requirements? ("Did we build it right?") | Is the item or component sufficiently cybersecure in its intended vehicle and operational context? ("Did we build the right thing against the threats?") |
| **Anchored to** | Cybersecurity requirements and architecture | TARA output, cybersecurity goals and claims, operational environment |
| **Techniques** | Overlap heavily with validation; the claims and the evidence differ |

### Indicative structure

Based on previews and pre-publication descriptions, not the final text — verify against the purchased document.

- **V&V in the cybersecurity context:** relation to the requirements hierarchy and architecture layers; the logical sequence of V&V activities; relation to the TARA; assumptions; handling of reused, out-of-context and COTS components.
- **V&V strategy and planning.**
- **Method groups:** review, analysis, formal methods, code analysis, functional testing, vulnerability scanning, fuzz testing, stress testing, fault injection, penetration testing, cryptographic testing.
- **Examples of method application.**
- **V&V reporting:** traceable evidence covering strategy, plan, environment, scope, results, findings and conclusions.
- **Informative annex** on how V&V differs from a cybersecurity assessment, plus a bibliography.

## Relationship to other frameworks

| Framework | Relationship |
|---|---|
| **ISO/SAE 21434:2021** | TR 8477 is positioned as guidance in the context of 21434; it elaborates the V&V requirements and does not add to them. A second-edition project for 21434 was reportedly registered around Oct 2026 |
| **ISO/SAE PAS 8475** (Cybersecurity Assurance Levels and Targeted Attack Feasibility) | Companion document that scales the rigour of activities, including V&V, by assurance level; CAL concepts first appear in 21434 Annex E. Publication status should be checked |
| **SAE J3322:2025** (Cybersecurity Testing, Verification, and Validation Methods) | Catalogue of detailed methods (~90 pages, May 2025); the TR points to it for technique-level detail |
| **UNECE R155 / R156** | R155 requires a certified cyber security management system and type-approval evidence; V&V results feed that evidence. TR 8477 does not itself establish compliance |
| **ISO 24089 / R156** | Software update engineering counterpart; V&V of update mechanisms is a related scope |
| **ISO/IEC 27090 and the NIST AI profile** | Not automotive-specific; relevant where AI components in the vehicle need security V&V — see the [ISO/IEC 27090 note](iso-27090-ai-security.md) and the [NIST IR 8596 note](nist-ir-8596-cyber-ai-profile.md) |

## Practical implications

- **OEMs and suppliers:** use the report to agree who performs which V&V activity at which interface, and what evidence is handed over. Distributed development is a stated use case.
- **Cybersecurity engineers:** build a traceability chain from TARA threat scenarios to requirements, tests and results, instead of a standalone pen-test report.
- **Assessors and auditors:** the report supports the evidence chain, but a V&V report is not a cybersecurity assessment; the annex draws that line.
- **Reused, out-of-context and COTS components:** state the assumptions explicitly and show how they were validated in the target vehicle context.
- **Privacy link:** vehicle data flows (telematics, location, driver data) fall under GDPR and similar regimes; security V&V evidence can support Article 32 "appropriate technical measures" narratives, but it is not privacy compliance evidence on its own.

## Related publications and commentary

| Source | What it adds | Link |
|---|---|---|
| ISO — standard page | Authoritative status, abstract, committee | <https://www.iso.org/standard/83188.html> |
| Paul Wooderson (HORIBA MIRA), *ISO/SAE 8475 and 8477 update* (Oct 2026, GlobalPlatform event) | Industry overview of the role of TR 8477 and PAS 8475; notes SAE J3322 for method detail | <https://globalplatform.org/wp-content/uploads/2026/10/14_-Wooderson_ISO-SAE-8475-and-8477-update.pdf> |
| SAE International — SAE J3322:2025 | Method catalogue supporting detailed V&V planning | <https://www.sae.org/> |
| Roberts, Marksteiner et al. — *A Global Survey of Standardization and Industry Practices of Automotive Cybersecurity V&V Testing Processes and Tools* (SAE Int. J. CAV, 2023) | Academic background on the V&V gap that TR 8477 addresses | <https://saemobilus.sae.org/content/12-07-02-0013/> |
| Chinese automotive-security commentary (CN-SEC, EET-China, Nov 2026) | Early reading: moves beyond "we did a penetration test"; stresses customer–supplier allocation and auditable evidence | Search by title; not independently verified |

### Gaps and open questions

- No peer-reviewed analysis of the published TR exists yet.
- Page count (reported ~28) and price (reported CHF 159) come from secondary sources, not the ISO page.
- Whether UNECE R155 approval authorities will treat TR 8477-style V&V reporting as expected evidence is untested.

## Status notes

Facts are as of 12 November 2026. The ISO page showed "Under publication" (stage 60.00); some third-party sources say "published". Verify the stage and the final clause structure before citing.
