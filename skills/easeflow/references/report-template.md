# Report template

Write `easeflow-report/report.md` with exactly these sections, in this order. Keep it readable by a non-technical founder: lead with the verdict and the changes, and put the evidence below. For big products, keep the main sections short and push detail into the per-job and per-persona sections at the end.

```markdown
# EaseFlow report: <Product name>

**Date:** <YYYY-MM-DD> · **Mode:** <Code only | Code + live app> · **Type:** <product type> · **Core win:** <one line>

**EaseFlow verdict:** <PASS | FAIL — main reason> (current) → <PASS | FAIL> (proposed)

**See it:** [Clickable prototype](prototype.html) · [Before/after summary](showcase.html) · [Feature ledger](feature-ledger.md)

## In one minute

- Harold, across first run and core jobs: <before> → <after> (<band> → <band>)
- Features: <N> found, <N> kept. <X> visible, <Y> in context or more options, <Z> advanced, <A> admin, <M> merged, <D> need your decision.
- Advanced mode: <Recommended | Not needed> — <one-sentence reason>
- <One sentence: the single biggest problem today.>
- <One sentence: the single biggest change proposed.>

## Persona scorecard

| Persona | Current score | Current result | Proposed score | Proposed result |
|---|---|---|---|---|
| Harold | 34 (Hard) | ❌ Fail: quit first run at step 3; failed 2 of 4 core jobs | 88 (Effortless) | ✅ Pass |
| ... | | | | |

Why these personas: <one line each for library and generated picks>

## Jobs scorecard

<Per-job table from scoring.md, core jobs first, then regular.>

## Top changes

Numbered, highest impact first. Max 10. Each one:

1. **<Change in plain words>.** Fixes: <friction IDs>. Rules: <R#>. Helps: <personas>.

## New structure

### Navigation, before and after

<Two indented trees (or Mermaid `flowchart LR`): current navigation with every area, then proposed navigation. Proposed top level shows at most 5 items for the main role.>

### Core objects and jobs

| Object | Core jobs | Regular jobs | Advanced |
|---|---|---|---|

### Advanced mode decision

<Recommended or not. For each of the three tests in complexity-modes.md, one line of evidence. If recommended: what Advanced view adds, where the switch is.>

### Roles

<Per role: which jobs they see, and where admin-only features live. "Single role" if none.>

## First run

<Mermaid flowchart of the current first run, then the proposed one. Mark ⛔ where personas quit and the onboarding steps.>

### Guided onboarding (shown once)

| Step | Screen heading | Body copy | Primary button | Skip? |
|---|---|---|---|---|

## Core jobs

<For each core job: one line of what it is, current vs. proposed steps, and a Mermaid flowchart of the proposed path. Mark ⛔ where personas quit on the current path.>

## Where every feature went

<Summary counts by disclosure level, then the features that moved most (top-level or sidebar items that moved, merged features, and every "Needs your decision" item). The complete table is in feature-ledger.md.>

## Metrics

<Baseline metrics table from scoring.md.>

## Friction register

| ID | Severity | Job | Where | Failed question | What happens | Personas | Evidence | Fix |
|---|---|---|---|---|---|---|---|---|
| F1 | Blocker | First run | Sign-up → Create workspace | Connect | "Workspace" is undefined; Harold stops | Harold, Ana, Literal | `src/app/onboarding/page.tsx:42` | Top change #1 |

Failed question is one of the four walkthrough questions: Goal, Notice, Connect, Feedback.

## Persona walkthroughs

### Harold: current
<Per task: short in-character think-aloud, step by step, ⛔ where they quit.>

### Harold: proposed
<...>

<Repeat for each persona. Alex's section lists each Advanced feature: found or not, clicks, where he looked first. List any rounds of the re-test loop (Round 1 → fix → Round 2).>

## Next: test with real people

<Two sentences: EaseFlow's personas are a fast first pass and tend to be more successful than real users. Point to real-user-test.md and list the 2–3 findings that most need confirming.>

## Needs your decision

<Product decisions EaseFlow can't make: features suggested for removal, pricing, data policy, whether to adopt Advanced mode. "None" if empty.>

## Coverage and limits

<Feature inventory completeness check: counts reconciled and any explained gaps. What was checked and how (code paths, screenshots). What couldn't be verified. Whether walkthroughs ran as blind subagents or in a single context. Where the two Harold runs disagreed, and which result was kept. Which accessibility checks were measured and which were judged. Where the prototype's theme came from, any neutral defaults used, and any accessibility adjustments to brand colours or sizes.>
```

## Mermaid conventions

- Use `flowchart TD` for flows and `flowchart LR` for navigation trees.
- Node IDs `S1`, `S2`, …; labels are screen names in quotes.
- Current flows: style blocker nodes with `classDef blocker fill:#fde2e2,stroke:#c0392b`.
- Proposed flows: style onboarding nodes with `classDef onboard fill:#e3f2e8,stroke:#2e7d4f`.
