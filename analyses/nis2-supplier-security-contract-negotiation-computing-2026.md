# "NIS2 turns supplier security into a contract negotiation" (Computing, 11 Nov 2026)

`EU · NIS2 · Supply chain security · Contracts · Third-party risk · Access lifecycle`

## Source

- **Title:** NIS2 turns supplier security into a contract negotiation
- **Publisher:** Computing (UK), opinion
- **Author:** Joe Petit, MD of Bora
- **Date:** 11 November 2026 (5-minute read)
- **Quoted experts:** Dr Yiannis Pavlosoglou (Deputy Governor, Greek National Cybersecurity Authority); Ioannis Ntokos (IT governance, risk and compliance expert, formerly FedEx, PwC and Randstad)
- **Link:** <https://www.computing.co.uk/opinion/2026/nis2-turns-supplier-security-into-a-contract-negotiation>

## Summary

The article argues that supply-chain security under NIS2 is mainly decided in the commercial contract, not by technical controls alone. A buyer cannot dictate how a supplier runs its business, but it can set the conditions under which that supplier gets access to the buyer's systems. Article 21(2)(d) puts responsibility on the buyer: if a supplier's compromised credentials let an attacker in, the buyer still owns the risk. That raises the weight of the terms agreed before access is granted.

## Key points

1. **Buyer responsibility.** The risk stays with the buyer even when the failure started at the supplier.
2. **Contract terms to settle first.** Whether the supplier must notify the buyer of a breach, how fast and in what circumstances; audit authority, including who pays and what evidence the supplier must provide; and who counts as a supplier at all, since that decides which relationships need identities and access created.
3. **The contract is a control.** Pavlosoglou describes it as one of the strongest controls for supply-chain risk. He recounts a negotiation that took ten months, because agreement on indemnification, liability and softer performance indicators had to come before the supplier's security-investment return could be pursued.
4. **NIS2 gives security teams leverage.** It is a reason to take key supplier agreements back to legal, especially for suppliers with access to critical systems or confidential data. Requirements may sit in indemnity and cyber-insurance clauses, where small wording changes alter who must do what.
5. **A signed questionnaire is not proof.** Questionnaires show what a vendor claims. Audit rights let the buyer verify controls where the risk warrants it.
6. **Look past the direct vendor.** Suppliers rely on their own contractors, so access and security requirements may need to reach further down the chain.
7. **Procurement baseline.** The article points to ENISA's guidance on cybersecurity requirements for ICT products and services as a starting point for what to ask suppliers to meet.
8. **The contract ending should end the access.** Credentials should not outlive the work. Ntokos has seen suppliers keep access after the hiring company had forgotten the relationship and advises vendor offboarding and lifecycle management. Supplier access should be time-limited from the start, rotated or revoked at the end, and logged so activity is attributable. Contract dates and access-system dates must agree.
9. **Maturity varies.** Some vendors already have controls and evidence; others meet formal security requirements for the first time. Slow clauses often decide whether the supplier must tell you about a breach, whether you can check its controls, and what happens to its access afterwards.

## Why it matters

- It turns the NIS2 supply-chain duty into a procurement checklist that legal, security and IT can share.
- The access-lifecycle point is the easiest to fail: paperwork ends on Friday and the account still works on Monday. It is also testable by audit.
- It complements the [ESAs frontier-AI statement](esa-statement-frontier-ai-ict-risks-2026.md), which asks financial entities to map dependencies and extend security requirements to vendors and open-source components, and the [Luxembourg NIS2 ILR reporting note](nis2-luxembourg-ilr-security-measures-reporting-2027.md) on national implementation.

## Clause checklist

This list is the hub's reading of the article's points, not the author's.

| Clause or control | Purpose |
|---|---|
| Definition of supplier and in-scope relationships | Decides which relationships need identities and access |
| Incident notification trigger, deadline and circumstances | Lets the buyer meet its own reporting duties |
| Audit rights, cost allocation and evidence required | Turns self-declared controls into verified ones |
| Indemnity, liability and insurance wording | Fixes who bears what if the supplier fails |
| Flow-down to sub-suppliers | Extends obligations down the chain |
| Time-limited, logged, attributable access | Keeps supplier activity bounded and traceable |
| Offboarding: rotate or revoke credentials at end | Ties contract end to access end |
| Procurement baseline (for example ENISA guidance) | Gives a common reference for requirements |

## Caveats

- This is an opinion piece. The reading of Article 21(2)(d) is the author's; check the Directive and national transposition for the exact duty.
- The article also cites a Passwork report on NIS2 access management, which I have not seen.
- The ten-month negotiation is an anecdote from one interviewee, not a benchmark.
- Quotes are paraphrased; see the original for the experts' wording.
