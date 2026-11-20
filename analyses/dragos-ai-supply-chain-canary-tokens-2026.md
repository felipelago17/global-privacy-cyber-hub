# Dragos (HD Moore): canary tokens show prompts leaking through the AI supply chain (Nov 2026)

`AI inference data · Zero Data Retention · Routers and resellers · Canary tokens · Provider breaches · Cross-border data flow · Source: Dragos research blog`

Status as of 20 Nov 2026. The page is based on a tool-generated summary of the Dragos blog post, not a direct reading, so wording, figures and nuance may differ from the original. It is one vendor's own research, single-sourced, and none of the findings has been independently verified or confirmed by the providers involved. The providers and the AI lab involved are not named in the summary.

## The source

HD Moore, Chief Research Officer at Dragos, "Three breaches, endless leaks: Your AI supply chain needs canaries", published 19 Nov 2026: <https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens>. The post ends with a Dragos product pitch.

## Thesis

Prompts and responses often leave the customer's control and are retained, resold or accessed by parties the customer never chose. Privacy settings such as Zero Data Retention (ZDR) frequently do not hold, and routers and marketplaces add hidden hops that can see everything.

## Method (as summarised)

- About 2 million prompts sent from July to November 2026, each seeded with unique canary URLs and credentials that no legitimate system should use.
- Tooling began with Thinkst Canarytokens, then a purpose-built seeding service producing per-prompt hostnames, URLs and credentials, with listeners for DNS, web, git, SSH, database, mail and legacy protocols. AWS keys belonged to empty, fully logged accounts.
- Each hit is attributed to the exact prompt, model, router and privacy setting. Route tracing used image-URL fetches and deliberately malformed requests whose nested error "envelopes" were matched to a signature database, mapping about 2,000 routes. Some routes sent data to companies not on the advertised path, and one seller added about 1,000 hidden tokens per prompt.

## Findings (as summarised)

1. **Provider compromises.** Attackers stole data from at least three hosting providers, the earliest in mid-July, and none of the providers knew until notified. The largest involved a couple of hundred AWS keys, each sent once in late October, some captured before a model ran, which suggests theft at the provider's front door. Two involved requests marked ZDR, which the author says a privacy flag cannot protect against once an attacker is inside. The attackers tested keys within hours, listed S3 buckets, searched Secrets Manager and Parameter Store, tried to enable Bedrock models and add IAM users, in tens of thousands of AWS API calls. One actor hit two providers from a single rented server, and on 1 Nov used an LLM-driven pentest framework (ARTEX) to check that stolen keys were still live.
2. **Marketplace resellers.** No exploit was needed: sellers listed popular models cheaply, switched on request logging and waited. Sellers appeared to be individuals on home connections; leaks followed the seller, not the marketplace. One French-based actor used passwords from prompts to try manual SSH root logins. One router secretly forwarded some traffic to a marketplace and said it stopped when notified.
3. **Privacy settings and retention ignored.** A Chinese AI lab fetched secret URLs from over half of its prompts (Jul–Oct), including about two-thirds of requests flagged "no data collection" or ZDR, typically two to three days after each request. US hosting providers reselling the lab's models triggered the same scraper, so prompts reached the lab despite customers choosing US providers for data residency. A git client on another cloud tried to clone private repositories named in prompts. A major US provider kept crawling a URL more than two months after one search-endpoint call. In the "Feishu incident", a secret link appeared in a Feishu chat 24 days after a prompt to a US provider with ZDR enabled, and was opened within two minutes from six devices in Beijing and Shanghai. The disclosure to the provider contained only the first eight characters of the link, so the person sharing it was reading a stored copy of the full prompt.

## Disclosure and response

The first provider's incident was undisclosed publicly as of the post, with stolen data driving login attempts into late October. One provider from the late-October breaches published a preliminary security notice. Dragos began notifying providers in early November, is working with about a dozen, and says stolen keys and URLs were still being accessed months later.

## Recommendations in the post

1. Self-host where feasible, only for the most sensitive work (the post prices hardware from about US$6,950 to US$570,000 or more).
2. Go directly to a first-tier provider to reduce the parties with access, noting agreements or breaches can still expose data.
3. Use routers carefully: choose upstream providers yourself, verify privacy settings govern routing, and avoid reseller marketplaces, which may rely on stolen keys.
4. Seed your own canaries: place fake credentials in the context agents and pipelines send, and treat any use as an incident.
5. Enable secret filtering where offered, knowing it misses sensitive data not shaped like API keys.

Key caveat: a privacy flag binds only the first hop, and AI agents send whatever they can read, including credentials.

## Why a privacy and cyber hub should care

- **Contractual promises versus technical reality.** ZDR and "no training" commitments cover a provider's own handling, not routers, resellers or a breach. DPIAs and vendor due diligence for AI services should map the full path, not the first hop. This echoes the [irreversibility trap](../case-studies/irreversibility-trap-fine-tuning.md) point on data that cannot be pulled back.
- **Transfers and residency.** The reported flow of prompts from US-hosted resellers back to a Chinese lab is the type of onward transfer that GDPR transfer analysis and data-residency commitments assume will not happen. If prompts contain personal data, a breach or unlawful onward transfer could carry notification duties.
- **Secrets in prompts.** Agents and coding assistants send credentials as context. That ties to the [Uber/Fireworks AI vendor breach](../case-studies/uber-fireworks-ai-vendor-breach-2026.md) where stolen vendor credentials were reportedly the entry point.
- **Detection control.** Canaries give a low-cost way to test whether data has been misused, but seeding canaries in real client or personal data raises its own questions, and the research appears to have used synthetic content.

## Gaps and cautions

- Summary only, one vendor's research, no independent corroboration, providers and the lab unnamed, and sample method not reproducible from what I saw.
- I could not check the figures (2 million prompts, 2,000 routes, "over half" and "two-thirds") or the attribution of any scraping or login attempts.
- Not legal or security advice.
