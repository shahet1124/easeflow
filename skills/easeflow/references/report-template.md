# Report template

Write `easeflow-report/report.md` with exactly these sections, in this order. Keep it readable by a non-technical founder: lead with the verdict and the changes, and put the evidence below.

```markdown
# EaseFlow report: <Product name>

**Date:** <YYYY-MM-DD> · **Mode:** <Code only | Code + live app> · **Core win:** <one line>

**EaseFlow verdict:** <PASS | FAIL — main reason> (current) → <PASS | FAIL> (proposed)

**See it:** [Clickable prototype of the new flow](prototype.html) · [Before/after summary](showcase.html)

## In one minute

- Harold's score: <before> → <after> (<band> → <band>)
- <One sentence: the single biggest problem today.>
- <One sentence: the single biggest change proposed.>
- Steps to core win: <before> → <after>

## Persona scorecard

| Persona | Current score | Current result | Proposed score | Proposed result |
|---|---|---|---|---|
| Harold | 34 (Hard) | ❌ Fail, quit at step 3 | 88 (Effortless) | ✅ Pass |
| ... | | | | |

Why these personas: <one line each for library and generated picks>

## Top changes

Numbered, highest impact first. Max 10. Each one:

1. **<Change in plain words>.** Fixes: <friction IDs>. Rules: <R#>. Helps: <personas>.

## Current flow

<Mermaid flowchart of the current path, sign-up to core win. Mark the steps where personas quit with a ⛔ in the node label.>

## Proposed flow

<Mermaid flowchart of the proposed path. Mark the onboarding steps.>

### Guided onboarding (shown once)

| Step | Screen heading | Body copy | Primary button | Skip? |
|---|---|---|---|---|

### Where every feature went

| Feature / setting | Before | After | Reason |
|---|---|---|---|
| <name> | Sidebar | Advanced → Campaign settings | R5 |

## Metrics

<Baseline metrics table from scoring.md.>

## Friction register

| ID | Severity | Where | What happens | Personas | Evidence | Fix |
|---|---|---|---|---|---|---|
| F1 | Blocker | Sign-up → Create workspace | "Workspace" is undefined; Harold stops | Harold, Ana, Literal | `src/app/onboarding/page.tsx:42` | Top change #1 |

## Persona walkthroughs

### Harold: current flow
<Step by step: short in-character think-aloud, ⛔ where they quit.>

### Harold: proposed flow
<...>

<Repeat for each persona. In each section, list any rounds of the re-test loop (Round 1 → fix → Round 2).>

## Needs your decision

<Product decisions EaseFlow can't make: pricing, removing features, data policy. "None" if empty.>

## Coverage and limits

<What was checked and how (code paths, screenshots). What couldn't be verified (e.g. "code only; mobile layout not rendered"). Where the prototype's theme came from, any neutral defaults used because a value wasn't found, and any accessibility adjustments to brand colours or sizes.>
```

## Mermaid conventions

- Use `flowchart TD`.
- Node IDs `S1`, `S2`, …; labels are screen names in quotes.
- Current flow: style blocker nodes with `classDef blocker fill:#fde2e2,stroke:#c0392b`.
- Proposed flow: style onboarding nodes with `classDef onboard fill:#e3f2e8,stroke:#2e7d4f`.
