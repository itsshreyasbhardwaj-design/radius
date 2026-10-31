# Security Policy

## Reporting a vulnerability

Please report security issues **privately**, not in a public issue.

Use GitHub's private vulnerability reporting on this repository:
**Security → Report a vulnerability**. That channel is monitored and keeps the
report confidential until a fix is available.

If private reporting is unavailable, email the maintainer address on the
GitHub profile for this account and put `SECURITY` in the subject.

Please include:

- what the issue is and roughly how severe you think it is
- the steps or request needed to reproduce it
- the affected version, commit, or deployed URL
- anything you already know about impact

**Please do not** open a public issue, a pull request containing an exploit, or
a public discussion thread for an unfixed vulnerability.

## What to expect

- An acknowledgement within **7 days**.
- An assessment, and either a fix or a clear explanation of why something is
  not considered a vulnerability, within **30 days** where that is achievable.
- Credit in the release notes if you would like it. Please say so.

This project is maintained by one person alongside other work. Response times
are best-effort, stated honestly rather than optimistically.

## Supported versions

Only the default branch receives security fixes. There are no long-lived
maintenance branches.

## Scope

In scope: this repository's own source code, its build and release workflows,
and its dependency manifests.

Out of scope: vulnerabilities in third-party dependencies that already have a
public advisory — Dependabot alerts and security updates are enabled on this
repository and will raise those automatically. Report those upstream.

Test fixtures that deliberately contain insecure code or placeholder
credentials are not vulnerabilities. Where a directory is named `fixtures/`
and documented as a deliberately vulnerable sample, findings inside it are
expected and are used to test this project's own scanners.
