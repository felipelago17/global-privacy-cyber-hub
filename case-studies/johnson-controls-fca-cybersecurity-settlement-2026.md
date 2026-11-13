# Case study — Johnson Controls: USD 5m False Claims Act settlement over contract cybersecurity (Nov 2026)

`United States · False Claims Act · NIST SP 800-171 · Government contractors · Whistleblowers · Supply chain`

## Summary

On 13 November 2026 the US Department of Justice announced that Johnson Controls, Inc. and two subsidiaries agreed to pay USD 5 million to resolve allegations that they violated the False Claims Act by failing to meet cybersecurity requirements in federal contracts. There was no reported breach. The alleged failure was one of compliance: the company is said not to have known enough about, or had enough control over, its own information systems to restrict access to protected government information, and not to have kept the security documentation its contracts required. The claims are allegations only and there has been no determination of liability.

## Key facts

| Item | Detail |
|---|---|
| Announcement | DOJ Office of Public Affairs, 13 November 2026 (Civil Division, No. 26-1360) |
| Parties | Johnson Controls, Inc. (Milwaukee, Wisconsin); Johnson Controls Fire Protection LP; Johnson Controls Security Solutions LLC |
| Amount | USD 5 million |
| Legal basis | False Claims Act |
| Period | January 2018 to August 2025 |
| Contracts | Contracts and subcontracts with NASA and the Departments of Defense, Energy and Justice for building products and services, including HVAC services |
| Whistleblowers | Two qui tam actions resolved. Relator Kelly Vance, a former employee, receives USD 850,000. The release does not state a share for the second relator, David Thomas |
| Cases | *United States ex rel. Kelly Vance v. Johnson Controls, Inc.*, No. 1:24-cv-2500 (N.D. Ga.); *United States ex rel. David Thomas v. Johnson Controls Int'l PLC*, No. 1:26-cv-448 (D.D.C.) |
| Status | Allegations only; no determination of liability |

## What was alleged

- **Access control.** The company failed to control access to protected information because it lacked sufficient information about, and control over, its information systems.
- **System Security Plan.** For contracts requiring compliance with NIST SP 800-171, including Defense Department contracts, it did not maintain a System Security Plan that met the contractual requirements.
- **Plan of action and milestones.** It did not adequately document, fully develop or fully implement a plan to correct deficiencies and reduce vulnerabilities.

## Why it matters for privacy, cyber and compliance programmes

- **Liability without an incident.** The exposure arose from the gap between what the contracts required and what was in place, not from data loss. Security attestations made to a customer are legal representations.
- **Documentation is the control.** Two of the three allegations concern documents: the System Security Plan and the remediation plan. An undocumented or stale plan is treated as a failure in its own right.
- **Asset inventory comes first.** The access-control allegation turns on not knowing the company's own systems well enough. Access control cannot be evidenced without a current inventory.
- **Insiders are the detection mechanism.** Both actions were brought by whistleblowers, one a former employee. Internal reporting channels and non-retaliation are part of cyber risk management.
- **Non-IT suppliers are in scope.** The contractor supplies building systems and HVAC services. Cybersecurity clauses follow the information, whatever the supplier's line of business, and they flow down to subcontracts.
- **Long look-back.** The period runs for more than seven years, so legacy contracts and acquired businesses carry the same exposure.

## Controls to take from it

| Control | Practice |
|---|---|
| Contract register | List every contract with a security clause, the standard it cites and the attestation given |
| System inventory | Keep a current map of systems that hold or process customer-protected information |
| System Security Plan | Maintain it per the cited standard; review on change and at least annually |
| Remediation plan | Document deficiencies with owners and dates; track to closure |
| Attestation sign-off | Named executive confirms the basis for each security representation before it is made |
| Speak-up | Route security concerns to compliance; record the response |
| Flow-down | Check subcontractor clauses and evidence |

## Framework mapping

- NIST SP 800-171 (protecting controlled unclassified information in non-federal systems): access control, security planning, plans of action.
- Compare [SEC v. SolarWinds and its CISO](solarwinds-sec-ciso.md): statements about security posture as a source of liability.
- Compare [EFS blood-plasma freezers](efs-coolworld-refrigeration-2026.md): building-systems contractors as a security dependency.

## Caveats

- Single source: the DOJ press release. The settlement agreement and the complaints were not read.
- The release does not say whether cooperation credit was given, and does not mention the Civil Cyber-Fraud Initiative by name.
- The settlement resolves allegations; the company has not been found liable.

## Sources

- US Department of Justice, Office of Public Affairs, press release of 13 November 2026 — <https://www.justice.gov/opa/pr/hvac-supplier-johnson-controls-inc-and-two-subsidiaries-agree-pay-5-million-settle>
