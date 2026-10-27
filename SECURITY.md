# Security policy

## What EaseFlow does on your machine

EaseFlow is a set of instructions for Claude Code. It has no server and collects no data. When you run it, Claude may:

- read your product's source code,
- start your app's dev server and open it in a browser (live mode),
- write report files to `easeflow-report/` inside your project,
- edit your code, **but only after you approve the proposal**.

The HTML templates load no third-party scripts. A generated prototype may load your product's own font from Google Fonts if your product uses one.

## Things to keep in mind

- **Don't commit `easeflow-report/` to a public repo** unless you're happy to share it. Reports describe your product's screens and features, and include file paths and screenshots.
- **Live mode uses your running app.** Point it at a local or staging environment with test data, not production with real customer data.
- **Review changes before approving.** Treat EaseFlow's code changes like any other pull request.

## Supported versions

Security fixes go into the latest release.

## Reporting a vulnerability

If you find a security problem, for example a template that could run untrusted content, or an instruction that could lead Claude to expose secrets or modify code without approval:

1. **Don't open a public issue.**
2. Use GitHub's **private vulnerability reporting** on this repository: the **Security** tab, then **Report a vulnerability**.
3. Include what you found, how to reproduce it, and what impact you think it has.

You'll get an acknowledgement within 7 days. We'll keep you updated while we work on a fix, and credit you in the release notes if you'd like.
