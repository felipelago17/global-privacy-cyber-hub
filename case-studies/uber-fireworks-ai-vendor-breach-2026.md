# Uber drivers' licence data stolen in a breach at AI vendor Fireworks AI

`Third-party / AI vendor risk · Stolen credentials · Driver's licence data · US state breach notification · Status: notifications under way`

Status as of 14 Nov 2026. Details come from press coverage of Uber's notices and state filings; I did not see the notice itself.

## Summary

Uber is notifying drivers in the United States that personal information, including driver's licence details, was stolen in an October 2026 breach at Fireworks AI, a third-party AI cloud provider that held Uber records. Uber was told on 9 Oct that hackers had stolen the vendor's internal credentials and used them to reach Uber's data. The notification letter is dated 10 Nov 2026. This is Uber's second known breach of 2026.

## Timeline

| Date (2026) | Event |
|---|---|
| 9 Oct | Fireworks AI tells Uber an unauthorised party stole its internal credentials and used them to access Uber's data |
| 13 Oct | Uber's investigation confirms the attacker accessed Uber data, including personal information of the people now notified; Uber had already cut its data connections with the vendor |
| 10 Nov | Date of Uber's notification letter, about a month after the first alert |
| 13 Nov | TechCrunch reports the breach from state attorney-general filings |

## What is reported

- **Who:** Uber confirmed Fireworks AI as the vendor to TechCrunch. Uber's own systems were reportedly not breached; the access came through the vendor.
- **Data:** personal information and driver's licence details of drivers. The notices seen do not show rider accounts exposed.
- **Numbers:** filings reviewed by TechCrunch show 7,870 people across three states (South Carolina 3,430, Massachusetts 2,567, Rhode Island 1,873). Uber has not disclosed a nationwide total, which is likely higher because notices went to other states, including California.
- **Attacker:** no known group has claimed the attack.
- **Response:** Uber says it found no misuse of the data when the letters went out and offers free credit monitoring and fraud assistance through Cyberscout, with 90 days from the letter date to enrol.
- **Unclear:** whether the separate Fireworks AI incident disclosed in October, which reportedly involved customer billing data and some private AI datasets, also exposed Uber data. Notion has said the same vendor was behind an exposure of AI chat transcripts affecting under 1% of its customer workspaces.

## Why it matters

1. **Vendor-held data is still your breach.** The company that collects driver documents carries the notification duty and the reputational cost even when the intrusion happens at a processor.
2. **A month between alert and letters.** Uber had confirmed access by 13 Oct and the letters are dated 10 Nov. US state laws set different deadlines, and some regulators will ask how the gap was justified. Document the timeline and the reasoning for each notice decision.
3. **Credentials were the way in.** Stolen vendor credentials gave access to a customer's data; the controls that matter are credential hygiene at vendors, tenant isolation, access logging and the ability to revoke connections quickly, which Uber reportedly did.
4. **Government ID data raises the stakes.** Driver's licence numbers are a high-value identity-fraud input, so the quality of monitoring offers and the speed of notice matter more than for basic contact data.
5. **AI vendors concentrate data.** Providers that host models and customer datasets for many clients become single points of exposure, as seen in the same vendor's other customers. This echoes the [Anthropic/Claude Korea PIPC case](anthropic-claude-korea-pipc-investigation-2026.md) and [Maersk's inherited system](maersk-legacy-system-whitearmor-extortion-2026.md).
6. **Prior history shapes scrutiny.** Uber's 2016 breach and its former security chief's obstruction conviction are covered in [United States v. Sullivan](uber-sullivan-ciso-obstruction.md); repeat incidents tend to draw closer regulator attention.

## Open questions

- How many drivers were affected in total, and in which countries?
- What exactly did Fireworks AI hold for Uber, why, and under what retention and security terms?
- Did the vendor's other, separate breach touch Uber data?
- Will state attorneys general or other regulators open inquiries?

## Sources

- TechCrunch, "Uber confirms hackers stole thousands of drivers' license information in data breach" (13 Nov 2026): <https://techcrunch.com/2026/11/13/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/>
- GBHackers, "Uber Hacked: Hackers Steal Drivers' License Personal Data" (14 Nov 2026): <https://gbhackers.com/uber-hacked-hackers-steal-drivers-license-personal-data/>
- Gizmodo (13 Nov 2026): <https://gizmodo.com/hackers-stole-thousands-of-uber-drivers-data-through-an-ai-startup-2000839947>
- SC Media brief (13 Nov 2026): <https://www.scworld.com/brief/uber-drivers-impacted-by-data-breach-at-third-party-provider>
- Cybersecurity News (14 Nov 2026): <https://cybersecuritynews.com/uber-confirms-data-breach/>
- Uber Form 10-Q (30 Sep 2026), risk-factor history of the 2016 and 2022 incidents: <https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000041/uber-20260930.htm>
