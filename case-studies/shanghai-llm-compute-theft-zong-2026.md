# Case study — Shanghai's first large-model computing-power theft case (Zong, Xuhui District Court, 2026)

`China · Generative AI · API abuse · Account farming · Forged e-signature verification · Criminal sentence`

## Summary

On 3 November 2026 PANews, citing The Paper, reported that the Shanghai Xuhui District Court sentenced a man surnamed Zong for illegally obtaining computer information system data. It was described as Shanghai's first case of using AI to forge signatures and steal large-model computing power. Zong found an interface on a large-model aggregation platform that was not open to the public, built his own relay website, and resold AI image and video generation at low prices. To fund this he used AI-written scripts to register accounts in bulk and collect sign-up bonus credits, getting round limits on registrations per IP address and forging the electronic signature check. He called the interface more than 290,000 times and made over 34,000 yuan. The platform reported the matter to police in March 2026.

## Key facts

| Item | Detail |
|---|---|
| Court | Shanghai Xuhui District Court |
| Defendant | A man surnamed Zong |
| Offence | Illegally obtaining computer information system data |
| Sentence | Three years' imprisonment with a three-year reprieve (suspended), and a fine of 40,000 yuan |
| Reported as | Shanghai's first case involving AI-forged signatures and theft of large-model computing power |
| Target | A large-model aggregation platform; an interface not open to the public |
| Method | Own relay website reselling image and video generation; AI-written scripts for bulk account registration to harvest bonus credits; bypass of IP registration limits; forged electronic signature verification |
| Scale | More than 290,000 interface calls; over 34,000 yuan in illicit proceeds |
| Detection | The platform saw more than 4 million accounts registered from a single IP in a short period; it reported to police in March 2026 |

## What went wrong

- **A non-public interface was reachable.** An endpoint not meant for the public could be found and called, and signature verification on it could be forged.
- **Signup incentives were exploitable at scale.** Free credits for new accounts turned account creation into a source of compute.
- **Per-IP limits were not enough.** Registration limits tied to IP address were bypassed. The scale of the abuse, millions of registrations from one IP, was visible to the platform, which did eventually report it.
- **Resale hid the origin.** A relay site let the defendant sell the stolen capacity to other users at low prices, so downstream customers were using services of unclear provenance.

## Why it matters for privacy, cyber and AI governance

- **Compute is an asset to protect.** Large-model capacity has direct monetary value. API keys, signing schemes and bonus credits are targets in the same way as payment or data assets.
- **Cost and abuse monitoring is a security control.** Sudden spikes in registrations, calls or spend from one origin are early indicators. The platform's data shows the abuse was detectable.
- **Relay and aggregator services add supply-chain risk.** Organisations using cheap third-party AI access may be sending prompts, files and personal data through an operator with no authority to provide the service, and may receive no legal or security assurances.
- **AI lowers the cost of fraud at scale.** The defendant used AI to write the registration scripts, which fits the pattern in this hub's other cases of AI making routine abuse cheaper.
- **A suspended sentence still records a criminal conviction** for a first-of-its-kind case, signalling that courts in China are treating this conduct as an offence against computer information systems.

## Controls to take from it

| Control | Practice |
|---|---|
| Authenticate every endpoint | Treat undisclosed interfaces as reachable; require strong server-side authentication |
| Harden signatures | Verify signatures and timestamps server-side, rotate keys, and test for forgery and replay |
| Rate-limit beyond IP | Combine device, account, payment and behavioural signals with IP limits |
| Gate free credits | Add verification, throttles and clawback for promotional credit |
| Monitor anomalies | Alert on bursts of account creation, one-origin concentration and abnormal call volume |
| Report and preserve evidence | Keep logs; decide in advance when to refer to police or regulators |
| Vet resellers | Ask where a cheap AI service gets its capacity and what happens to your data |

## Caveats

- This note rests on a short PANews report that relays The Paper. I have not seen the judgment or The Paper's original story. Details such as the platform's name, the exact legal provisions applied and the date of sentencing are not given in the report.
- The "controls" and the governance points are this hub's reading, not statements from the court or the platform.
- Conversion and monetary figures are in yuan as reported.

## Sources

- PANews (PA一线), 3 November 2026, "Shanghai's First Case of Stealing Large-Model Computing Power Is Sentenced: Man Who Used AI to Forge Signatures for Profit Jailed", citing The Paper. Link supplied by the user via a security-gateway URL: panews.io/articles/01a1a0a9-8e8a-771a-a25a-a61cfb7be5c5
