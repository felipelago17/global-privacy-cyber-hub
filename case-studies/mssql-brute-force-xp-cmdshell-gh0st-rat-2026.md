# Internet-exposed SQL Servers hijacked with brute force, xp_cmdshell, a miner and Gh0st RAT (FortiGuard Labs)

`Database security · Credential brute force · xp_cmdshell · Gh0st RAT · Cryptomining · Source: FortiGuard Labs via GBHackers, 13 Nov 2026`

Status as of 14 Nov 2026. Technical findings are FortiGuard Labs' as relayed by GBHackers; I did not read the FortiGuard report. The campaign was active in early October 2026.

## Summary

Attackers scan for Microsoft SQL Server instances exposed on TCP port 1433, guess credentials, switch on `xp_cmdshell` with a T-SQL script to run operating-system commands, and install a Monero miner and a Gh0st remote access trojan variant. The activity looks opportunistic rather than targeted: no victim counts or sectors were given.

## Reported attack chain

| Stage | Detail |
|---|---|
| Discovery | A packed Go binary using the Naabu port scanner pulls a target range from a remote server, expands it to a hard-coded /16 block and probes port 1433 |
| Access | Brute force with usernames such as `sa` and `admin` against a password list of more than 2,700 entries, with up to 500 threads |
| Execution | After a successful login, a T-SQL script enables `xp_cmdshell`, giving command execution on the host through the database |
| Payloads | A Monero miner disguised as a Microsoft Edge updater; a Gh0st RAT variant disguised as `winlogon.exe` with 30+ commands (keylogging, file transfer, download-and-execute, registry and service control, event-log clearing) and theft of QQ data; a downloader that fetches more files from an FTP server |
| Persistence | Scheduled tasks imitating Edge Update (every 30 minutes and daily), a task named `Microsoft_UPDATES`, a Run key, a Windows service and a Startup-folder copy |
| Evasion | Renamed payloads (for example `Google.exe`, `dwm.exe`); the RAT checks for 78 security-product process names, including Microsoft Defender and 360 Total Security |

## What is claimed, not established

- Attribution: no actor is named. The article suggests a Chinese-language malware lineage, based on QQ data theft and other features, which is an inference.
- The article's "espionage-style access and monetisation" description is its interpretation.
- The RAT's command servers were offline during analysis, so the RAT was examined statically only.

## Why it matters for privacy and cyber teams

1. **A database login is a path to the operating system.** With `xp_cmdshell` enabled, weak SQL credentials become full host compromise, and the database often holds personal and regulated data.
2. **Basic exposure still drives incidents.** Port 1433 reachable from the internet, a default `sa` account and no lockout policy are the preconditions. They are cheap to find and fix.
3. **Miner plus RAT means more than lost CPU.** A RAT with keylogging and file transfer turns a "nuisance" miner alert into a possible data breach, so triage should assume the worse case until the host is investigated.
4. **Unexpected configuration change is the alarm.** Treat any server where `xp_cmdshell` was enabled without a change record as compromised, and review event-log clearing as an anti-forensic signal.
5. **Evidence for regulators.** Under GDPR Art. 32, NIS2 Art. 21 and similar duties, "reasonable security" will be tested against exactly these basics: exposure, credentials, hardening and monitoring. See the [Marriott/Starwood](cyber-risk-in-m-and-a-marriott-yahoo.md) page on inherited systems for the legacy-server angle.

## Recommended controls (from the article)

- Do not expose port 1433 to the internet.
- Rename or disable `sa`; enforce long, unique passwords and account lockout.
- Keep `xp_cmdshell` disabled and alert if it is enabled.
- Hunt for Edge-update tasks pointing to unusual paths such as `C:\Users\Public` or `E:`, and for the file names, tasks and domains in the FortiGuard report.

## Sources

- GBHackers, Mayura Kathir, "Hackers Hijack Microsoft SQL Servers Using T-SQL Commands to Install Gh0st RAT and Crypto Miners" (13 Nov 2026): <https://gbhackers.com/microsoft-sql-servers-hijacked/>
- The article attributes the technical analysis to FortiGuard Labs; the original report was not accessed. Indicators of compromise are in that report and are not reproduced here.
