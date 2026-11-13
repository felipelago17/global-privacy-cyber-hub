# Case study — DOJ actions against North Korean crypto theft: FaceStealer and the Binance theft (12 Nov 2026)

`DPRK · Deepfakes · Social engineering · Supply chain · Virtual assets · Asset freezes · Developing`

Status as of 13 Nov 2026, based on the US Department of Justice press release of 12 Nov 2026 (No. 26-1356). The release describes ongoing actions; no indictments, defendants, forfeiture complaints, sanctions designations or statutes are named in it.

## Summary

The Justice Department announced coordinated actions against North Korean cryptocurrency theft on two fronts. First, it disrupted cloud infrastructure used in a campaign called **FaceStealer**, which the department says stole more than USD 400 million over about 18 months. Second, it reported progress on tracing and securing assets from a theft of more than USD 6 billion in virtual assets from Binance around 29 October 2026, which the FBI attributes to North Korean military actors it calls "TraderTraitor".

## Key facts

| Item | Detail |
|---|---|
| Announced | 12 Nov 2026, DOJ Office of Public Affairs (release 26-1356) |
| FaceStealer losses | More than USD 400 million in cryptocurrency over about 18 months |
| FaceStealer action | CDCA disrupted cloud-based infrastructure; under a federal warrant the FBI seized more than 900 webcam videos of victims |
| Aliases named | Sapphire Sleet, UNC1069, Dangerous Password, CryptoCore, APT38, BlueNoroff, Stardust Chollima |
| Binance theft | On or about 29 Oct 2026; more than USD 6 billion in virtual assets; attributed by the FBI to "TraderTraitor" |
| Recovery so far | More than USD 2.7 billion frozen through government and private-sector efforts; court authorisation to seize or restrain more than USD 1.2 billion |
| Laundering | Continues through crypto bridges, mixers and exchanges |
| FBI alert | Cyber alert issued the week before with the Secret Service and IRS-CI, urging virtual asset service providers to block transactions with or derived from the laundering addresses |
| Public resources | FBI report IC3 CSA 2026/261112 and fbi.gov/facestealer |

## How FaceStealer works (per DOJ)

1. Attackers send video-meeting invitations from accounts they previously compromised.
2. They record the target's webcam and play pre-recorded videos of earlier victims or trusted contacts, and use AI-generated deepfakes of well-known crypto and Web3 figures.
3. They claim a technical fault, such as the target being inaudible, and send a "fix" that installs malware.
4. Theft can follow months, or more than a year, after the first compromise.
5. They mine victims' contact lists, social media and messaging apps to reach more people.

Targets include people in the crypto and Web3 industries and developers or maintainers of open-source software, apparently to reach software repository accounts and enable supply-chain attacks.

## Why it matters for privacy, cyber and AI governance

- **Identity and trust are the attack surface.** Deepfaked colleagues and prior-victim recordings defeat "recognise the person on the call" as a control. It sits alongside the [AI-agent identity attacks](ai-agent-identity-attacks-entra-artex-2026.md) case.
- **Dwell time can be very long.** A compromise may only monetise a year later, which affects incident scoping, breach notification timing and what "no evidence of misuse" can responsibly claim.
- **Open-source maintainers are a route to downstream supply-chain compromise**, raising vendor and software-dependency risk for any organisation.
- **Response is a multi-party effort.** Freezes of USD 2.7 billion came from government and private-sector action, and the FBI alert asks service providers to block flagged addresses, which is a compliance and sanctions-screening question for exchanges and banks.
- **Questions for legal and compliance teams:** are staff trained to verify identity out-of-band before installing anything during a meeting? Can you scope compromises that predate theft by a year? Are blockchain-address blocking and screening duties documented?

## Sources

- US Department of Justice, 12 Nov 2026: https://www.justice.gov/opa/pr/justice-department-announces-actions-disrupt-north-koreas-massive-theft-cryptocurrency
- FBI FaceStealer resource page, as referenced by DOJ: fbi.gov/facestealer
