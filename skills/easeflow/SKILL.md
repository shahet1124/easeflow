---
name: easeflow
description: Audit a finished product (SaaS, web app, tool) for how easy it is for non-technical, time-poor paying customers. Maps the real flow from code (and optionally the live app), walks it as literal-minded buyer personas led by "Harold", a wealthy 70-year-old with low tech comfort, scores each persona with pass/fail, then proposes a simple, sellable flow with one-time guided onboarding. Produces a clickable HTML prototype of the new flow in the product's own design theme, a report with before/after flow diagrams, and a summary showcase page, and implements fixes only on approval. Use when the user asks to run EaseFlow, simplify a product's flow or onboarding, check whether a non-technical customer could use the product, run a persona/usability audit, or reduce product complexity.
---

# EaseFlow

**The test:** give the product to Harold, a 70-year-old with plenty of money and little tech comfort, and walk away. If he can reach the thing he's paying for alone, with only a one-time guided onboarding, the product passes.

Developers build what feels easy to people who know the system. EaseFlow sees the product the way a buyer does: literally, impatiently, with no inside knowledge. It's the PB&J "exact instructions" test applied to software. Every missing step gets skipped, and every vague word gets misread.

## Ground rules

- **Evidence or it didn't happen.** Every friction point cites where it comes from: `file:line`, a route, a component, or a screenshot. Never invent screens, features, or copy the product doesn't have.
- **Read literally.** Personas know only what's on the screen. If a label says "Workspace", Harold doesn't know what a workspace is. If no button says what to do next, he doesn't do it.
- **Simplify, don't amputate.** Hide or defer advanced features; don't delete capability users pay for. Alex (the power-user guardrail) must still find them.
- **Report first, change code only on approval.** Don't edit the product's code until the user approves the proposed flow.
- **Be honest about coverage.** In code-only mode, say what couldn't be verified without running the app.

## Phase 0: Set up

1. **Identify the product and its core win.** The core win is the one outcome a buyer pays for: "first campaign sent", "first invoice paid", "first report delivered". Infer it from the code, README and marketing copy. If it's genuinely unclear, ask the user once. Everything is measured as *time and effort to the core win*.
2. **Pick the mode:**
   - **Code + live app:** when the user gives a URL or a dev server can be started (check `.claude/launch.json`, `package.json` scripts, etc.). Map from code, then walk the app in the browser and take screenshots.
   - **Code only:** when there's no runnable app or the user asks for it.
   - Ask once if neither is obvious. Otherwise decide and state which mode you chose.
3. **Create the output folder** `easeflow-report/` at the product's root (with `screenshots/` in live mode).

## Phase 1: Map the current flow

Trace the path a new paying customer takes: **first visit → sign-up → first screen after login → setup → core win → coming back the next day**.

From code, find: routes/pages, navigation (sidebar, tabs, menus), forms and required fields, empty states, onboarding (if any), error messages, and settings the user must touch before the core win. In live mode, walk the same path in the browser and screenshot each screen.

Record, for each step: screen name, what the user must do, required inputs, choices offered, visible terms, and the evidence location.

Then compute the **baseline metrics** (definitions in `references/scoring.md`):
- steps to core win
- decisions before core win
- navigation items visible on first login
- jargon terms shown before core win
- dead ends (screens with no obvious next action)

Draw the current flow as a Mermaid flowchart.

**Capture the design theme** too. The prototype in Phase 6 must look like *their* product, not like EaseFlow. Follow the "Capture the theme" section of `references/prototype-guide.md` and save the result as `easeflow-report/theme.json`.

## Phase 2: Choose personas

Persona files live in `personas/`. Read each one you use in full.

- **Always run the core two:** `harold.md` and `literal-follower.md`.
- **Always run the guardrail:** `alex-power-user.md`.
- **Pick 2–3 from the library** that fit this product's buyers and context (for example, Priya for B2B tools sold to executives, Jay if customers will likely use phones, Frank if there's a payment or data-sharing step).
- **Generate 1–2 product-specific personas** for the product's real buyers, using the same structure as the library files (see `personas/_template.md`). Name them, and base them on evidence (the product's market, copy and pricing), not stereotypes.

State which personas you picked and why, in one line each.

## Phase 3: Walk the current flow as each persona

For each persona, walk the flow from Phase 1 step by step, **in character and literally**:

- At each step, write a short think-aloud in the persona's voice (one or two sentences): what they see, what they think it means, what they do.
- Apply their **"Gives up when"** rules. When one triggers, they stop. Record where and why.
- Log each problem as a friction point with a severity:
  - **Blocker:** the persona quits or can't continue without outside help.
  - **Major:** the persona guesses, goes the wrong way, or loses meaningful time.
  - **Minor:** slows them down or makes them uneasy, but they continue.

Score each persona using `references/scoring.md` and decide **pass/fail**: did they reach the core win alone, within their patience budget?

Merge all friction points into one **friction register**, de-duplicated and ranked by severity and then by how many personas hit them.

## Phase 4: Design the simple flow

Apply `references/simplification-rules.md`. The target shape is the ChatGPT model: **one obvious first action**, value right away, everything else revealed when needed.

Produce:
1. **The proposed flow:** the shortest path to the core win, step by step, with exact on-screen copy (headings, button labels, helper text) in plain language.
2. **A one-time guided onboarding:** 3–5 steps maximum. It should do real setup work (not a feature tour), use smart defaults, and always be skippable and resumable.
3. **What moves where:** every feature or setting from the current flow ends up as *kept in flow*, *moved to later/contextual*, *moved to Advanced*, or *recommend removing (with reason)*. Nothing silently disappears.
4. The proposed flow as a Mermaid flowchart.

## Phase 5: Re-test until it passes

Walk the **proposed** flow with every persona again, the same way as Phase 3. Re-score.

- **Pass bar:** Harold passes, the Literal Follower passes, Alex does not fail, and no Blockers remain.
- If the bar isn't met, fix the specific step that broke and re-test. This is the PB&J loop. Maximum 3 rounds. Record what changed each round.
- If it still fails after 3 rounds, say so plainly and explain what's blocking it (often a product decision only the user can make).

## Phase 6: Deliver

Write to `easeflow-report/`:

1. **`prototype.html`: the main deliverable.** A clickable, standalone prototype of the **proposed** flow, styled in the product's own theme (`theme.json`). It goes from sign-up through the guided onboarding to the core win, with the exact copy from Phase 4. It should feel like the customer's own product, already simplified. Build it following `references/prototype-guide.md`.
2. **`report.md`:** follow `references/report-template.md` exactly.
3. **`showcase.html`:** the before/after summary page. Copy `assets/showcase-template.html` and replace only the JSON inside `<script id="easeflow-data">` with this run's data (the schema is documented in the template). Set `prototypeUrl` to `"prototype.html"`. Don't change the template's markup or styles. Escape `</` inside JSON strings as `<\/`.
4. **`flow-data.json`:** the same JSON, for reuse.

Open `prototype.html` in a browser and click through the whole flow before handing it over (see the checklist in the guide). If an Artifact tool is available and the user wants to share the result, offer to publish the prototype and the showcase. Otherwise point to the files.

Then give the user a short summary: before → after score for Harold, pass/fail per persona, the top 3 changes, and a pointer to the prototype. Ask whether to implement. The prototype is the spec: Phase 7 builds what it shows.

## Phase 7: Implement (only on approval)

When the user approves (all of it or selected changes):
- Implement in the product's own stack and conventions. Match existing components, styling and copy tone.
- Order: onboarding and first screen first (biggest impact), then copy/jargon fixes, then navigation restructuring.
- Keep advanced features reachable (Advanced section, settings, or contextual entry points).
- Store onboarding progress so it resumes, and never shows again once completed or skipped.
- After implementing, re-run Phase 5 against the real changes (live mode if possible) and update the report's scores.
