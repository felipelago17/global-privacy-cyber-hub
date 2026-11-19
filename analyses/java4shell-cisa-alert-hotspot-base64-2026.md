# Java4Shell: CISA urges patching of the HotSpot Base64 flaw (Nov 2026)

`Vulnerability · Java / OpenJDK · Remote code execution · Patch management · Source: trade press (The Hacker News)`

Status as of 19 Nov 2026. The primary source is CISA's alert "Critical Java Vulnerability Requires Immediate Patching", released 17 Nov 2026: <https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching>. I read its full text, as pasted by the author because my own fetch of the page failed. The CVSS score, product list, Keycloak conditions and test results are not in the CISA alert; they come from a trade-press article, Ravie Lakshmanan, "CISA Urges Immediate Patching of Java4Shell Flaw That Could Allow Remote Code Execution", The Hacker News, 18 Nov 2026: <https://thehackernews.com/2026/11/cisa-urges-immediate-patching-of.html>. The vendor source is Oracle's Critical Security Patch Update (CSPU) advisory for November 2026, Rev 1, 17 Nov 2026: <https://www.oracle.com/security-alerts/cspunov2026.html>. I read the advisory text as pasted by the author and did not open the URL myself. I did not read the Keycloak advisory or the Blackpoint Cyber research.

## What CISA's alert says (primary)

- **Flaw.** CISA urges immediate patching of Oracle Java vulnerability CVE-2026-114938, a critical memory-corruption flaw nicknamed "Java4Shell" in the Base64 decoder of the x86-64 HotSpot JVM, part of the JDK. Specially crafted Base64 input could crash the JVM and allow unauthenticated remote code execution.
- **Actions.**
  1. Identify affected Java installations, including JDKs and runtimes bundled with third-party applications or included in container images and appliances. CISA notes they may not appear as separate entries in software inventories.
  2. Apply Java and vendor patches as soon as available, prioritising internet-facing systems.
  3. If patching is not immediately feasible, use compensating controls: restrict and validate Base64 input at the application boundary, enforce input-size limits, limit unauthenticated access.
  4. Review Oracle's security advisory ("Critical Security Patch Update, November 2026") for affected products and versions.
  5. Monitor for suspicious activity, including rogue runtimes, unexpected JVM crashes and suspicious Java processes.
- **What the alert does not say.** It gives no CVSS score, no list of affected third-party products, no Known Exploited Vulnerabilities listing, no deadline and no exploitation status.

## What Oracle's advisory says (vendor, primary)

- **Release.** The November 2026 CSPU (Rev 1, 17 Nov 2026) contains 655 new security patches across the listed product families. Oracle says patches are released on the third Tuesday of each month; the next dates it lists are 15 Dec 2026 (CSPU), 19 Jan 2027 (CPU), 16 Feb 2027 and 16 Mar 2027 (CSPU).
- **Java SE.** 11 new Java SE patches, all described as remotely exploitable without authentication. CVE-2026-114938 has the highest base score of the eleven, 8.1 (CVSS 3.1; network vector, attack complexity high, no privileges, no user interaction, scope unchanged, high confidentiality, integrity and availability impact).
- **Affected products as Oracle lists them for this CVE.** Oracle Java SE, Oracle GraalVM for JDK and Oracle GraalVM Enterprise Edition; component listed as "Compiler", protocol "Multiple". Versions listed: Java SE 8u511b33-perf, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3 and 27.0.1.0.3; GraalVM for JDK 17.0.21.0.3 and 21.0.13.0.3; GraalVM Enterprise Edition 21.3.20.0.3. Java 11 and the non-"perf" 8u511b33 build are not listed for this CVE, although they appear for other CVEs in the same update. How Oracle's version strings map to patched and unpatched builds should be read from its patch availability documents, which I did not see.
- **Exploitation condition (Note 1).** Per Oracle, this vulnerability can only be exploited by supplying data to APIs in the affected component without using untrusted Java Web Start applications or applets, for example through a web service. That fits CISA's description of server-side exposure through crafted input.
- **Credit.** Reported to Oracle by Albert Yang and by Quang Luong of Calif.io.
- **Naming difference.** Oracle's risk matrix labels the component "Compiler", while CISA and the press describe the Base64 decoder of the x86-64 HotSpot JVM. Oracle's matrix uses generic component names, so this may be a labelling difference; I have not resolved it.
- **Related.** Oracle says it issued earlier Security Alerts in October 2026 for CVE-2026-91403, CVE-2026-114820, CVE-2026-109618 and CVE-2026-109619, and that customers should apply those too.
- **Support.** Patches are provided only for versions under Premier or Extended Support; Oracle recommends upgrading unsupported versions. It also points to Java Management Service for finding vulnerable Java installations.
- **No exploitation statement.** The advisory text I have does not say whether the flaw is being exploited.

## What the trade-press article adds (secondary)

- **Score and mechanism.** CVSS 8.1 per the article, which describes an out-of-bounds write in the Base64 decoder of the x86-64 HotSpot JVM (part of the JDK) that can cause denial of service or, under certain conditions, remote code execution. CISA is quoted as saying specially crafted Base64 input could crash the JVM and allow unauthenticated remote code execution.
- **Status.** Oracle and OpenJDK have released patches. No in-the-wild exploitation at publication. No threat actor named.
- **Products said to be exposed (from the outlet's earlier reporting).** Unauthenticated code execution under default settings on Keycloak, Atlassian Jira, Atlassian Confluence, JFrog Artifactory, Jenkins and PingFederate; code execution with a login on Apache Kafka Broker, Apache Solr, Elasticsearch, Gerrit and Spinnaker.
- **Keycloak guidance (18 Nov update).** Possible exposure needs all of: an unpatched OpenJDK build from 17.0.6 onward (including unpatched 21 and 25); a host or VM exposing the `avx512vbmi` CPU feature to Java; and a running JVM with Base64 intrinsics enabled and not limited to AVX2 through `-XX:UseAVX=2`. Container tags 26.8.2-1 and 26.8.2-2 bundle an affected OpenJDK 21.0.13 build, but tags alone do not decide exploitability; standalone ZIP or TAR.GZ distributions can also be affected. Keycloak provides a host-level command to check the CPU feature, and temporary mitigations until patched images ship.
- **Blackpoint Cyber testing.** On a local Spring Boot application with Spring Security, about 28,000 unauthenticated requests carrying a malformed Base64 authentication value crashed the JVM after roughly 20 seconds; testing also showed corruption of nearby Java objects and changes to live application data, sometimes with no immediate crash.

## Why a privacy and cyber hub should care

- **Integrity, not only availability.** Corrupted live application data without a crash is a data-integrity and incident-detection problem, which matters for personal-data breach assessment as well as uptime.
- **Hidden runtimes.** The advice to inventory bundled JDKs in appliances and container images is the same software-bill-of-materials and supplier-visibility problem behind the [Optimizely case](../case-studies/optimizely-third-party-script-compromise-178-sites-2026.md) and [NIS2 supplier security](nis2-supplier-security-contract-negotiation-computing-2026.md).
- **Identity infrastructure.** Keycloak, PingFederate and similar products sit in front of authentication, so a flaw triggered by a malformed authentication value affects the control point many privacy programmes depend on.
- **Conditional exposure.** Exploitability turns on CPU features and JVM flags, so a blanket "affected or not" answer from a version scan will be wrong in both directions; hardware and runtime settings need checking.
- For prioritisation sources, see the [reference sites list](../training-labs/cyber-reference-sites-20.md) (CISA, NVD, EPSS).

## Gaps and cautions

- The CVSS score is now confirmed by Oracle's risk matrix. The non-Oracle product list, Keycloak conditions and Blackpoint test results still rest on the trade-press article alone.
- Oracle's version strings carry a ".0.3" suffix that I could not map to specific builds; use Oracle's patch availability documents.
- The product list is described as coming from earlier reporting, not from vendors, and I did not verify any vendor's own statement beyond Keycloak's as relayed.
- "No exploitation" was true at publication and may have changed.
- Not legal or patching advice; confirm versions against the vendor advisories.
