# LAG Köln: works councils cannot get permanent access to time-tracking data by company-wide agreement (Jan 2026)

`Germany · Employment data · Works councils · Health data (Art. 9 GDPR) · Section 26 BDSG · Access controls · Source: Ogletree Deakins (Emily Hannemann)`

Status as of 22 Nov 2026. This page is based on the full text of Ogletree's article, supplied as a paste, with the Heuking summary from search excerpts as a cross-check on the facts. The pasted text matches the title of the JD Supra link you sent, but I could not open that page, and the paste does not show a publication date. I have not read the judgment. Statements about the reasoning are Ogletree's account of the court's reasoning.

## The decision

Regional Labor Court of Cologne (LAG Köln), 9 Jan 2026, Ref. 9 TaBV 22/25. Held: a general works council cannot, on its own authority, grant local works councils permanent electronic access to personal data in a time-tracking system through a company-wide works agreement. The decisive factors were data protection requirements and the general works council's limited competence.

## Facts

- The employer concluded a company-wide works agreement with its general works council on the HR system "LOGA", which records working hours, time accounts and reasons for absence, among other things. Local works councils had electronic read-only access for monitoring.
- A data protection incident triggered the dispute: a local works council had employees' sick days in an unencrypted spreadsheet on an internal drive. The employer revoked all local works councils' access. Heuking's summary adds that the data protection officer had demanded the revocation and that the agreement dated from 2018; I have not confirmed those points beyond that summary.
- The general works council demanded restoration or, alternatively, limited access without certain absence reasons (illness, rehabilitation stays, maternity leave).

## Reasoning (as reported)

1. **Competence.** Time-tracking that records conduct or performance is subject to co-determination under Section 87(1) No. 6 BetrVG, and the general works council handled that for a company-wide system. But local works councils' access to working-time data falls under their own monitoring and information rights in Section 80 BetrVG, exercisable at establishment level. A company-wide rule would need delegation under Section 50(2) BetrVG, and there was none. The court left open whether an employer can generally give local councils their own access rights in a company-wide agreement.
2. **Obligations as well as rights.** Read-only access would also create data protection obligations for the local councils, which had not agreed to take them on.
3. **Data protection.** Even read-only access is processing under the GDPR. Absence reasons such as rehabilitation stays or maternity leave allow conclusions about health, so they are health data, bringing Art. 9 GDPR and Section 26(3) BDSG into play.
4. **Necessity.** Permanent monitoring access with no specific reason was not necessary. Section 80(2) BetrVG gives works councils the information and documents they need for their tasks, not permanent online access to a whole database. Case-by-case requests let the employer check what data is actually needed; unlimited access would largely remove that check.
5. **No basis in the agreement.** The works agreement did not justify processing the specially protected data, which was not necessary in the employment context, and employees had not consented.
6. **Alternative request.** Rejected: the agreement did not provide for a view hiding absence reasons, building it would need programming, and Section 80 BetrVG does not require an employer to create new documents or technically modify a system.

## Outlook (Ogletree)

Works councils may still receive working-time data, but the court distinguished information needed for a specific case from permanent, comprehensive system access. Section 87(1) No. 6 BetrVG alone does not let a general works council regulate local councils' access to personal data for monitoring. Ogletree suggests reviewing access concepts for HR and time-tracking systems regularly, using role-based, purpose-limited, data-minimising access.

## Why a privacy and cyber hub should care

- **Access to HR systems is a data protection question.** Standing read access for any internal body, including employee representatives, needs a necessity analysis and attention to special-category data.
- **The incident shaped the outcome.** An unencrypted spreadsheet of sick days led to the access dispute. This is a reminder that downstream handling by recipients is part of the controller's risk.
- **Collective agreements are not a free pass.** This is consistent with earlier German and CJEU reasoning that works agreements cannot justify processing the GDPR does not permit; the search excerpts discuss that line (the CJEU's Dec 2024 C-65/23 ruling and related German rulings), but I have not read them.
- For other employment-related data protection material in this hub see the [EDPB 2027 enforcement action on automated recruitment](edpb-cef-2027-automated-recruitment-art22.md).

## Gaps and cautions

- Reasoning is Ogletree's account; the LAG Köln judgment itself was not read, and the pasted article has no stated date.
- The court left open some questions (for example, whether company-wide agreements can ever give local councils their own access rights). It was an appeal on a specific agreement, so I would not generalise beyond that.
- German-law specifics (BetrVG sections) may not translate to other jurisdictions.
- Not legal advice.
