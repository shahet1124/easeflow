# EaseFlow scoring

Score every persona twice: once on the current flow, once on the proposed flow. The score shows *how easy* the flow is. Pass/fail shows *whether they made it*. Report both.

## Metric definitions

Count these along the path from sign-up to the core win.

| Metric | Counts as one |
|---|---|
| **Step** | A distinct action the user must take: a screen change, a form submit, a required click. Optional actions don't count. |
| **Decision** | A point where the user must choose between options and there's no recommended default. A pre-selected default with "Continue" isn't a decision. |
| **Jargon term** | A word the persona wouldn't use in everyday speech to describe their own goal ("workspace", "sequence", "ICP", "webhook", "sync", "entity"). Count each distinct term once per screen. |
| **Vague instruction** | An instruction a literal reader could interpret more than one way ("Add your info", "Connect", "Set up"). |
| **Dead end** | A screen where the next action isn't visibly labelled, or an empty state with no call to action. |
| **Unhelpful error** | An error that's technical, blames the user, or doesn't say how to fix it. |
| **Trust gap** | A commitment made blind: payment, a permission grant, sending or deleting without explanation, preview or undo. |
| **Nav load** | Navigation items (sidebar, tabs, top menu) visible on the first screen after sign-up. |

## Persona score (0–100)

Start at 100 and subtract:

| Component | Max | Deduction |
|---|---|---|
| **Time to value** | 25 | −5 per step beyond the persona's patience budget |
| **Decision load** | 20 | −4 per decision before the core win, beyond the first |
| **Language** | 15 | −3 per jargon term or vague instruction the persona meets |
| **Dead ends & errors** | 15 | −5 per dead end or unhelpful error |
| **Trust & reassurance** | 10 | −5 per trust gap, or missing confirmation of success |
| **Independence** | 15 | −15 if the persona needs outside help at any point |

- Each component can't go below 0. Its deduction is capped at its Max.
- **Blocker cap:** if the persona hits any Blocker, the score is capped at **40**.
- Apply the persona's own "Watch for" checklist when deciding what counts. Margaret's contrast issue is a dead end for her, but may be nothing for Alex.

## Bands

| Score | Band | Meaning |
|---|---|---|
| 85–100 | **Effortless** | Harold would recommend it to a friend |
| 70–84 | **Easy** | Works, with small bumps |
| 50–69 | **Effortful** | Gets there, but it feels like work |
| 0–49 | **Hard** | Most buyers like this persona won't make it |

## Pass / fail per persona

**Pass** = the persona reaches the core win **alone** (only the one-time guided onboarding) **within their patience budget**, with no Blocker.

For the guardrail persona (Alex), use **Pass** or **Fail** based on their own pass condition: every capability they need is still reachable.

## Product verdict

The product **passes EaseFlow** only when all of these are true:

1. Harold passes.
2. The Literal Follower passes.
3. Alex does not fail.
4. No Blockers remain in the friction register.

Report the verdict as one line: `EaseFlow verdict: PASS` or `EaseFlow verdict: FAIL — <the main reason>`.

## Baseline metrics table

Always include this table for both flows:

| Metric | Current | Proposed |
|---|---|---|
| Steps to core win | | |
| Decisions before core win | | |
| Jargon terms before core win | | |
| Dead ends | | |
| Nav items on first screen | | |
| Trust gaps | | |
