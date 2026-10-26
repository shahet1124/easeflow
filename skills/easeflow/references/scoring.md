# EaseFlow scoring

Score every persona twice: once on the current product, once on the proposed one. The score shows *how easy* it is. Pass/fail shows *whether they made it*. Report both.

Score **each task separately** (first run, each core job, coming back, recovery, each regular job). A persona's **overall score** is the average of their task scores, and their **overall result** is Pass only if they pass every task on their list.

## Metric definitions

Count these along each task's path. For first run, that's from first contact (landing page, install, invite or first open) to the core win. For other jobs, it's from the home screen to the job's outcome.

| Metric | Counts as one |
|---|---|
| **Step** | A distinct action the user must take: a screen change, a form submit, a required click. Optional actions don't count. |
| **Decision** | A point where the user must choose between options and there's no recommended default. A pre-selected default with "Continue" isn't a decision. |
| **Jargon term** | A word the persona wouldn't use in everyday speech to describe their own goal ("workspace", "instance", "SKU", "ledger", "webhook", "sync", "entity", "provision", "tenant"). Count each distinct term once per screen. |
| **Vague instruction** | An instruction a literal reader could interpret more than one way ("Add your info", "Connect", "Set up"). |
| **Dead end** | A screen where the next action isn't visibly labelled, or an empty state with no call to action. |
| **Unhelpful error** | An error that's technical, blames the user, or doesn't say how to fix it. |
| **Trust gap** | A commitment made blind: payment, a permission grant, sending or deleting without explanation, preview or undo. |
| **Nav load** | Navigation items (sidebar, tabs, top menu, bottom bar) visible on the first real screen after entry. |
| **Clicks from home** | For a feature: the fewest clicks from the home screen to use it. |
| **Findability** | For a feature: whether a blind walker found it without help, and how many places they looked first. |

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

**Pass** (per task) = the persona completes the task **alone** (only the one-time guided onboarding) **within their patience budget**, with no Blocker. Patience budgets in persona files apply to **each task**.

For the guardrail persona (Alex), **Pass** means every Advanced feature was found within 3 clicks from home and works.

## Product verdict

The product **passes EaseFlow** only when all of these are true:

1. Harold passes first run and every core job.
2. The Literal Follower passes first run, every core job and every regular job.
3. Alex passes (every Advanced feature found within 3 clicks).
4. No Blockers remain in the friction register.
5. Coverage is 100%: every feature in the ledger has a home, and none is lost.

Report the verdict as one line: `EaseFlow verdict: PASS` or `EaseFlow verdict: FAIL — <the main reason>`.

## Baseline metrics table

Always include this table for both flows:

| Metric | Current | Proposed |
|---|---|---|
| Steps to core win (first run) | | |
| Average steps per core job | | |
| Decisions before core win | | |
| Jargon terms across core jobs | | |
| Dead ends | | |
| Nav items on first screen | | |
| Trust gaps | | |
| Features found by blind walkers (%) | | |
| Advanced features within 3 clicks (%) | | |
| Features kept (of total) | N/N | N/N |

And a per-job table:

| Job | Tier | Harold (current → proposed) | Literal Follower | Steps (current → proposed) |
|---|---|---|---|---|
