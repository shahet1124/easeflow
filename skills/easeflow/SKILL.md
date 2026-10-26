---
name: easeflow
description: Audit any finished product (web app, SaaS, mobile app, desktop app, store, marketplace, booking or internal tool), however large, for how easy it is for non-technical, time-poor paying customers, and redesign how it's presented without losing a single feature. Inventories every feature, groups them into user jobs, runs blind, literal-minded persona walkthroughs led by "Harold", a wealthy 70-year-old with low tech comfort, scores each job and persona with pass/fail, then proposes a simple, sellable structure with guided onboarding, progressive disclosure and, only where justified, an Advanced mode. Produces a clickable HTML prototype in the product's own design theme, a complete feature ledger, a report with before/after flow diagrams, a summary showcase page and a real-user test kit, and implements changes only on approval. Use when the user asks to run EaseFlow, simplify a product, its flows, navigation or onboarding, check whether a non-technical customer could use it, run a persona/usability audit, or reduce product complexity.
---

# EaseFlow

**The test:** give the product to Harold, a 70-year-old with plenty of money and little tech comfort, and walk away. If he can do everything he's paying for alone, with only a one-time guided onboarding, the product passes.

Developers build what feels easy to people who know the system. EaseFlow sees the product the way a buyer does: literally, impatiently, with no inside knowledge. It's the PB&J "exact instructions" test applied to software.

**EaseFlow changes how a product is presented and used, never what it can do.** A big product keeps all its power. Every feature gets a home, and Harold only meets each one when he needs it. EaseFlow covers the whole product, not just the first-run flow.

## Method

EaseFlow combines established methods:
- a **complete feature inventory** with a coverage ledger,
- **object-oriented UX** and **top tasks** (the few jobs most people come to do) to restructure navigation,
- **progressive disclosure** to keep advanced features reachable but out of the way,
- **persona-driven cognitive walkthroughs** to test every job,
- mechanical scoring.

Research on AI-simulated users shows they're **too successful and too agreeable**: they find the right path real users miss, praise designs real users question, and invent issues that aren't there. Every rule below that says *blind*, *evidence* or *default to fail* exists to counter that. Don't relax them.

## Ground rules

- **Nothing is lost.** Every feature in the ledger ends with a new home. Removal is only ever a recommendation for the user to decide.
- **Evidence or it didn't happen.** Every feature and friction point cites where it comes from: `file:line`, a route, a component, or a screenshot. Never invent screens, features, or copy the product doesn't have.
- **Insiders map, outsiders walk.** Whoever has read the code knows too much to play Harold. Persona walkthroughs see only what's on screen.
- **Default to fail.** If a persona *might* get stuck and the screen doesn't clearly prevent it, they get stuck.
- **Report first, change code only on approval.**
- **Be honest about coverage.** Say what couldn't be verified, and say plainly that EaseFlow is a fast first pass, not a replacement for watching real people.

## Phase 0: Set up

1. **Identify the product type** from the code. This decides where the journey starts and how the prototype is framed:

   | Type | Usually starts at | Prototype frame |
   |---|---|---|
   | Web app / SaaS | Landing page → sign-up | Browser |
   | Mobile app (React Native, Flutter, Swift, Kotlin) | Install → first open | Phone |
   | Desktop app (Electron, Tauri, native) | Install → first launch | Window |
   | Store / marketplace / booking | Landing or product page → checkout or booking | Browser (phone if mobile-first) |
   | Content / learning / community | Landing → join → first lesson, post or item | Browser or phone |
   | Internal / admin / B2B back-office | Invite email or SSO → first screen | Browser |
   | Companion app for a device or service | Install → pair or connect → first use | Phone |

   If it mixes types, take the one the paying customer meets first.

2. **Identify the core win:** the first meaningful **outcome** a buyer pays for ("first invoice paid", "first appointment booked", "first order placed"). Infer it from the code, README, pricing and marketing copy. Ask the user once only if it's genuinely unclear.

3. **Pick the mode:**
   - **Code + live app:** when the user gives a URL or a dev server/simulator can be started. Map from code, then walk the app and take screenshots.
   - **Code only:** when there's no runnable app or the user asks for it.
   - Ask once if neither is obvious. Otherwise decide and state which mode you chose.

4. **Gauge the size:** count screens/routes and rough feature count. Over about 15 screens or 60 features is a **big system**: split the work by module and use parallel subagents where this file says so.

5. **Create the output folder** `easeflow-report/` at the product's root (with `screenshots/` in live mode).

## Phase 1: Inventory everything (insider)

Follow `references/feature-coverage.md` steps 1–4:

1. **Feature inventory:** every screen, action, setting, object, role, integration, notification and billing feature, in `feature-ledger.md`. Big systems: one subagent per module, then merge.
2. **Completeness check:** reconcile routes, endpoints, settings and nav items against the ledger. Don't continue with unexplained gaps.
3. **Objects:** the 3–8 nouns users think in, and how they relate.
4. **Jobs and tiers:** group every feature into user jobs, and tier each job **Core**, **Regular** or **Advanced**, with the evidence for each tier. If the product has roles, list each role's jobs.

Then map the current experience for:
- **First run:** first contact → entry → first real screen → any setup → core win.
- **Every core job**, end to end, for each role that does it.
- **Coming back:** the next day, a week later, with data in the product.
- **Recovery:** fixing a mistake, undoing, finding something you made earlier, getting help.
- **Regular and advanced jobs:** where each one lives today and how many clicks it takes to get there.

Write a **screen inventory** for the walkers, `easeflow-report/screens.md`: for every screen involved, **only what a user would see**: headings, visible text, labels, buttons, placeholder text, icons (described as they look, e.g. "gear icon, no label"), what's pre-filled, and what each control visibly leads to. In live mode, reference the screenshot. **No code, no component names, no developer intent, no explanations of jargon.**

Compute the **baseline metrics** (`references/scoring.md`). Draw a current **navigation map** (all areas) and a Mermaid flowchart for first run and each core job.

**Capture the design theme** too, following "Capture the theme" in `references/prototype-guide.md`, and save `easeflow-report/theme.json`.

## Phase 2: Choose personas and tasks

Persona files live in `personas/`.

- **Always run:** `harold.md`, `literal-follower.md`, and the guardrail `alex-power-user.md`.
- **Pick 2–3 from the library** that fit this product's buyers and context.
- **Generate 1–2 product-specific personas** from evidence, using `personas/_template.md`.

Give each persona a **task list** written as real-life goals, never using the product's own labels:

| Persona | Tasks |
|---|---|
| Harold | First run, then every core job, coming back, and recovery |
| Literal Follower | First run, every core job, and every regular job |
| Alex | Find and use every Advanced feature (from the ledger), plus bulk and expert work |
| Library and generated personas | First run plus the core jobs that fit them; their own checks (e.g. Jay on a phone, Frank at every commitment) |

For each role in the product, walk that role's core jobs with at least Harold and the Literal Follower.

State which personas you picked and why, in one line each.

## Phase 3: Walk the current product (outsider, blind)

**Run each persona as a separate subagent** (Agent tool) when available. Big systems: split a persona's task list across several subagents, one per area. Give each subagent only:
- the persona file,
- its tasks (as real-life goals),
- `screens.md` (and screenshots in live mode),
- the walkthrough instructions below.

Don't give it the code, the ledger, the flow map, or anything that explains what the product's terms mean. If subagents aren't available, do the walkthrough yourself using only `screens.md`, and treat anything you know from the code as unknown.

**Walkthrough instructions** (for each step of each task, in character, literally):

1. Ask the four cognitive-walkthrough questions, in the persona's terms:
   - **Goal:** will this persona *want* to do what this step needs? (Do they even know it's needed?)
   - **Notice:** will they *see* the control that does it?
   - **Connect:** will they *understand* that this control does what they want, from its label alone?
   - **Feedback:** after acting, will they *know* it worked and what comes next?
2. A step only passes if the screen evidence clearly answers **yes to all four**. Any "maybe" is a "no".
3. Write a short think-aloud in the persona's voice (one or two sentences).
4. Apply the persona's **"Gives up when"** rules. When one triggers, they stop that task. Record where and why. Don't rescue them.
5. Log each friction point with: the task, step, failed question, severity, and evidence.
   - **Blocker:** the persona quits or can't continue without outside help.
   - **Major:** the persona guesses, goes the wrong way, or loses meaningful time.
   - **Minor:** slows them down or makes them uneasy, but they continue.

For **findability tasks** (Alex, and regular jobs), record whether they found it, where they looked first, and how many clicks it took.

**Run Harold's first run and core jobs twice, independently.** If the runs disagree, take the **worse** result and note it.

**Measured checks beat imagined ones.** In live mode, check contrast with `getComputedStyle`, 375px width, 200% zoom and tap target sizes for real.

## Phase 4: Verify findings and score

- **Drop** any friction point with no evidence.
- **Merge** duplicates across personas and tasks.
- **Check** every Blocker against the code: confirm the problem is real, and that the persona's reading is reasonable for someone with their background.

Score each persona **per job** and overall, using `references/scoring.md`, and decide pass/fail. Build one **friction register**, ranked by severity, then by tier (core first), then by how many personas hit it.

## Phase 5: Redesign the whole product

Apply `references/simplification-rules.md` and `references/complexity-modes.md`. Work from the outside in:

1. **Structure:** new navigation built from the core objects and core jobs (at most 5 top-level items for the main role). Every regular job sits with the object or job it belongs to. Draw the new navigation map.
2. **Disclosure:** place every feature on the ladder in `complexity-modes.md` (automatic, visible, in context, more options, per-area Advanced, admin). Decide whether a **global Advanced mode** is justified using its three tests, and write the evidence. Usually it isn't.
3. **Home screen:** the everyday starting point, with one obvious next action and the core jobs one click away (the ChatGPT model).
4. **Core jobs:** the shortest path for each, with exact on-screen copy in plain language.
5. **First run:** a one-time guided onboarding of 3–5 steps maximum that does real setup work, uses smart defaults, and is always skippable and resumable. If no setup is needed, it can be a single welcome step, or none.
6. **Consistency:** one pattern per kind of task across all areas, and one plain name per concept.
7. **Complete the feature ledger** (`feature-coverage.md` step 5) and pass the **coverage gate** (step 6): 100% of features placed, none lost.
8. Write `screens-proposed.md` in the same visible-only format as Phase 1, and Mermaid flowcharts for the new first run and each core job.

## Phase 6: Build the prototype and re-test blind

1. **Build `prototype.html`** following `references/prototype-guide.md`. It must have the new navigation with every area, full clickable flows for first run and every core job, a screen for every area showing where its regular and advanced features now live, and the Advanced mode switch if one was recommended.
2. **Re-test with fresh subagents** that never saw your reasoning, the ledger, the friction register or the old product. Give them the persona file, the same task lists, and the prototype (in the browser if they can use it, otherwise `screens-proposed.md`). Run the same walkthrough as Phase 3. You designed this, so you can't grade it yourself.
3. **Pass bar:**
   - Harold passes first run and **every core job** (both runs).
   - The Literal Follower passes first run, every core job and every regular job.
   - Alex finds **every** Advanced feature within 3 clicks and doesn't fail.
   - No Blockers remain.
   - The coverage gate passes: 100% of features placed, none lost.
4. If the bar isn't met, fix the specific step or placement that broke, update the prototype, and re-test with fresh walkers. Maximum 3 rounds. Record what changed each round.
5. If it still fails after 3 rounds, say so plainly and explain what's blocking it (often a product decision only the user can make).

## Phase 7: Deliver

Write to `easeflow-report/`:

1. **`prototype.html`:** the main deliverable, checked with the guide's checklist.
2. **`feature-ledger.md`:** every feature, old location → new location, disclosure level and reason, with coverage numbers at the top.
3. **`report.md`:** follow `references/report-template.md` exactly.
4. **`showcase.html`:** the before/after summary page. Copy `assets/showcase-template.html` and replace only the JSON inside `<script id="easeflow-data">` with this run's data (the schema is in the template). Set `prototypeUrl` to `"prototype.html"`. Don't change the template's markup or styles. Escape `</` inside JSON strings as `<\/`.
5. **`flow-data.json`:** the same JSON, for reuse.
6. **`real-user-test.md`:** following `references/real-user-test.md`.

If an Artifact tool is available and the user wants to share the result, offer to publish the prototype and the showcase. Otherwise point to the files.

Then give the user a short summary: Harold's before → after scores across core jobs, pass/fail per persona, coverage ("all N features kept; X visible, Y in context, Z advanced"), whether an Advanced mode was recommended and why, the top 3 changes, and a pointer to the prototype. Recommend running the real-user test before building. Ask whether to implement. The prototype and ledger are the spec.

## Phase 8: Implement (only on approval)

When the user approves (all of it or selected changes):
- Implement in the product's own stack and conventions. Match existing components, styling and copy tone.
- Order: navigation and home screen, then core jobs, then first-run onboarding, then copy and jargon fixes, then moving regular and advanced features to their new homes, then Advanced mode (if approved).
- Use the feature ledger as a checklist. Tick each feature as it's moved, and confirm it still works.
- Store onboarding progress so it resumes, and never shows it again once completed or skipped. Store the Advanced mode choice per user.
- After implementing, re-run Phase 6's blind re-test against the real changes (live mode if possible), re-check the coverage gate, and update the report.
