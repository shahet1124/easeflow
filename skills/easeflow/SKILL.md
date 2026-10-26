---
name: easeflow
description: Audit any finished product (web app, SaaS, mobile app, desktop app, store, marketplace, booking or internal tool) for how easy it is for non-technical, time-poor paying customers. Maps the real flow from code (and optionally the live app), runs blind, literal-minded persona walkthroughs led by "Harold", a wealthy 70-year-old with low tech comfort, scores each persona with pass/fail, then proposes a simple, sellable flow with one-time guided onboarding. Produces a clickable HTML prototype of the new flow in the product's own design theme, a report with before/after flow diagrams, a summary showcase page and a real-user test kit, and implements fixes only on approval. Use when the user asks to run EaseFlow, simplify a product's flow or onboarding, check whether a non-technical customer could use the product, run a persona/usability audit, or reduce product complexity.
---

# EaseFlow

**The test:** give the product to Harold, a 70-year-old with plenty of money and little tech comfort, and walk away. If he can reach the thing he's paying for alone, with only a one-time guided onboarding, the product passes.

Developers build what feels easy to people who know the system. EaseFlow sees the product the way a buyer does: literally, impatiently, with no inside knowledge. It's the PB&J "exact instructions" test applied to software. Every missing step gets skipped, and every vague word gets misread.

EaseFlow works on any product with a user interface. Nothing in it assumes a particular industry.

## Method

EaseFlow is a **persona-driven cognitive walkthrough** (the established inspection method for first-time-user learnability) with mechanical scoring and a built-in redesign. Research on AI-simulated users shows they're **too successful and too agreeable**: they find the right path real users miss, praise designs real users question, and invent issues that aren't there. Every rule below that says *blind*, *evidence* or *default to fail* exists to counter that. Don't relax them.

## Ground rules

- **Evidence or it didn't happen.** Every friction point cites where it comes from: `file:line`, a route, a component, or a screenshot. Never invent screens, features, or copy the product doesn't have.
- **Insiders map, outsiders walk.** Whoever has read the code knows too much to play Harold. Persona walkthroughs see only what's on screen (see Phase 3).
- **Default to fail.** If a persona *might* get stuck and the screen doesn't clearly prevent it, they get stuck. Real users wander and give up more than simulations predict.
- **Simplify, don't amputate.** Hide or defer advanced features; don't delete capability users pay for. Alex (the power-user guardrail) must still find them.
- **Report first, change code only on approval.** Don't edit the product's code until the user approves the proposed flow.
- **Be honest about coverage.** Say what couldn't be verified, and say plainly that EaseFlow is a fast first pass, not a replacement for watching real people (Phase 7 gives the user a kit for that).

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

2. **Identify the core win.** The core win is the first meaningful **outcome** a buyer pays for, not an action inside the product: "first invoice paid", "first appointment booked", "first lesson finished", "first order placed", "first report delivered", "first payment received", "first device reading shown". Infer it from the code, README, pricing and marketing copy. If it's genuinely unclear, ask the user once. Everything is measured as *time and effort to the core win*.

3. **Pick the mode:**
   - **Code + live app:** when the user gives a URL or a dev server/simulator can be started (check `.claude/launch.json`, `package.json` scripts, etc.). Map from code, then walk the app in the browser and take screenshots.
   - **Code only:** when there's no runnable app or the user asks for it.
   - Ask once if neither is obvious. Otherwise decide and state which mode you chose.

4. **Create the output folder** `easeflow-report/` at the product's root (with `screenshots/` in live mode).

## Phase 1: Map the current flow (insider)

Trace the path a new paying customer takes: **first contact → account or entry → first real screen → any setup → core win → coming back the next day**.

From code, find: routes/screens, navigation (sidebar, tabs, menus, bottom bars), forms and required fields, permission prompts, payment steps, empty states, onboarding (if any), error messages, and settings the user must touch before the core win. In live mode, walk the same path and screenshot each screen.

Write two things:

1. **Flow map** (for you): each step's screen, what the user must do, and the evidence location.
2. **Screen inventory** (for the walkers): `easeflow-report/screens.md`. For each screen, **only what a user would see**: headings, visible text, labels, buttons, placeholder text, icons (described as they look, e.g. "gear icon, no label"), what's pre-filled, and what happens on each control (described as a visible result, e.g. "goes to a screen titled 'Workspace setup'"). In live mode, reference the screenshot. **No code, no component names, no developer intent, no explanations of jargon.**

Compute the **baseline metrics** (definitions in `references/scoring.md`) and draw the current flow as a Mermaid flowchart.

**Capture the design theme** too. The prototype must look like *their* product, not like EaseFlow. Follow "Capture the theme" in `references/prototype-guide.md` and save `easeflow-report/theme.json`.

## Phase 2: Choose personas

Persona files live in `personas/`.

- **Always run the core two:** `harold.md` and `literal-follower.md`.
- **Always run the guardrail:** `alex-power-user.md`.
- **Pick 2–3 from the library** that fit this product's buyers and context (for example, Priya for products sold to executives, Jay for mobile-first products, Frank if there's a payment, permission or data-sharing step, Linda if buyers delegate setup).
- **Generate 1–2 product-specific personas** for the product's real buyers, using `personas/_template.md`. Base them on evidence (the product's market, copy, pricing), not stereotypes, and give each one concrete "Gives up when" triggers.

State which personas you picked and why, in one line each.

## Phase 3: Walk the current flow (outsider, blind)

**Run each persona as a separate subagent** (Agent tool) when available. Give it only:
- the persona file,
- `screens.md` (and screenshots in live mode),
- the core win in plain words,
- the walkthrough instructions below.

Don't give it the code, the flow map, your own opinions, or anything that explains what the product's terms mean. If subagents aren't available, do the walkthrough yourself using only `screens.md`, and treat anything you know from the code as unknown.

**Walkthrough instructions** (for each step, in character, literally):

1. Ask the four cognitive-walkthrough questions, in the persona's terms:
   - **Goal:** will this persona *want* to do what this step needs? (Do they even know it's needed?)
   - **Notice:** will they *see* the control that does it?
   - **Connect:** will they *understand* that this control does what they want, from its label alone?
   - **Feedback:** after acting, will they *know* it worked and what comes next?
2. A step only passes if the screen evidence clearly answers **yes to all four**. Any "no" is a friction point. Any "maybe" is a "no".
3. Write a short think-aloud in the persona's voice (one or two sentences).
4. Apply the persona's **"Gives up when"** rules. When one triggers, they stop. Record where and why. Don't rescue them.
5. Log each friction point with: the step, which question failed, severity, and the evidence (screen/screenshot).
   - **Blocker:** the persona quits or can't continue without outside help.
   - **Major:** the persona guesses, goes the wrong way, or loses meaningful time.
   - **Minor:** slows them down or makes them uneasy, but they continue.

**Run Harold twice, independently** (two subagents). If the two runs disagree about whether he passes or where he quits, take the **worse** result and note the disagreement.

**Measured checks beat imagined ones.** In live mode, check Margaret's and Jay's concerns for real: compute text contrast with `getComputedStyle`, resize to 375px and check for horizontal scroll, check at 200% zoom, measure tap target sizes. Use those results instead of a guess.

## Phase 4: Verify findings and score

Before scoring, filter the friction points (AI walkers over-report as well as under-report):

- **Drop** any point with no evidence on the screen inventory or screenshot.
- **Merge** duplicates across personas.
- **Check** every Blocker against the flow map: confirm the problem is real (for example, the "missing" button really doesn't exist), and that the persona's reading is reasonable for someone with their background.

Score each persona using `references/scoring.md` and decide **pass/fail**. Build one **friction register**, ranked by severity and then by how many personas hit each point.

## Phase 5: Design the simple flow

Apply `references/simplification-rules.md`. The target shape is the ChatGPT model: **one obvious first action**, value right away, everything else revealed when needed.

Produce:
1. **The proposed flow:** the shortest path to the core win, step by step, with exact on-screen copy (headings, button labels, helper text) in plain language.
2. **A one-time guided onboarding:** 3–5 steps maximum. It should do real setup work (not a feature tour), use smart defaults, and always be skippable and resumable. If the product needs no setup before the core win, the onboarding can be a single welcome step, or none.
3. **What moves where:** every feature or setting from the current flow ends up as *kept in flow*, *moved to later/contextual*, *moved to Advanced*, or *recommend removing (with reason)*. Nothing silently disappears.
4. The proposed flow as a Mermaid flowchart.
5. A **proposed screen inventory** (`screens-proposed.md`) in the same visible-only format as Phase 1.

## Phase 6: Build the prototype and re-test blind

1. **Build `prototype.html`** following `references/prototype-guide.md`: the proposed flow, clickable, in the product's own theme.
2. **Re-test with fresh subagents** that never saw your reasoning, the friction register or the old flow. Give them the persona file and the prototype (in the browser if they can use it, otherwise `screens-proposed.md`). Run the same walkthrough as Phase 3. You designed this flow, so you can't grade it yourself.
3. **Pass bar:** Harold passes (both runs), the Literal Follower passes, Alex does not fail, and no Blockers remain.
4. If the bar isn't met, fix the specific step that broke, update the prototype, and re-test with fresh walkers. This is the PB&J loop. Maximum 3 rounds. Record what changed each round.
5. If it still fails after 3 rounds, say so plainly and explain what's blocking it (often a product decision only the user can make).

## Phase 7: Deliver

Write to `easeflow-report/`:

1. **`prototype.html`:** the main deliverable, checked with the guide's checklist.
2. **`report.md`:** follow `references/report-template.md` exactly.
3. **`showcase.html`:** the before/after summary page. Copy `assets/showcase-template.html` and replace only the JSON inside `<script id="easeflow-data">` with this run's data (the schema is documented in the template). Set `prototypeUrl` to `"prototype.html"`. Don't change the template's markup or styles. Escape `</` inside JSON strings as `<\/`.
4. **`flow-data.json`:** the same JSON, for reuse.
5. **`real-user-test.md`:** a short kit for testing the prototype with real people, following `references/real-user-test.md`. EaseFlow's personas find likely problems fast; five real people confirm which ones matter.

If an Artifact tool is available and the user wants to share the result, offer to publish the prototype and the showcase. Otherwise point to the files.

Then give the user a short summary: before → after score for Harold, pass/fail per persona, the top 3 changes, and a pointer to the prototype. Recommend running the real-user test before building. Ask whether to implement. The prototype is the spec: Phase 8 builds what it shows.

## Phase 8: Implement (only on approval)

When the user approves (all of it or selected changes):
- Implement in the product's own stack and conventions. Match existing components, styling and copy tone.
- Order: onboarding and first screen first (biggest impact), then copy/jargon fixes, then navigation restructuring.
- Keep advanced features reachable (Advanced section, settings, or contextual entry points).
- Store onboarding progress so it resumes, and never shows again once completed or skipped.
- After implementing, re-run Phase 6's blind re-test against the real changes (live mode if possible) and update the report's scores.
