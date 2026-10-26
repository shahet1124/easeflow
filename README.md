# EaseFlow

**If a 70-year-old who's great with money but not with tech can use your product alone, it's a good product.**

EaseFlow is a Claude Code skill you run on any finished product with a user interface: web apps, SaaS, mobile apps, desktop apps, stores, marketplaces, booking systems and internal tools. It maps how the product really works, walks through it as a set of non-technical buyer personas who follow every screen literally, scores how easy it is, and proposes a simple, sellable flow with a one-time guided onboarding.

Developers build what feels easy to developers. The people who pay usually have money and little time, not tech familiarity. EaseFlow closes that gap.

## What you get

1. **Clickable prototype** (`easeflow-report/prototype.html`): your product in its own design theme (colours, fonts, logo, components), rebuilt around EaseFlow's simplified flow. It runs from the first screen through the guided onboarding to the core win, framed as a browser, phone or desktop window to match your product. It looks like your app, made simple.
2. **Report** (`easeflow-report/report.md`): friction points ranked by severity, a score and pass/fail for each persona, before vs. after, and screen-by-screen changes.
3. **Flow diagrams**: the current flow vs. the proposed flow (Mermaid, inside the report).
4. **Before/after showcase** (`easeflow-report/showcase.html`): a one-page summary of the scores and both flows, linking to the prototype, ready to show clients or your team.
5. **Real-user test kit** (`easeflow-report/real-user-test.md`): a 15-minute script for checking the prototype with five real people.
6. **Optional fixes**: only after you approve, EaseFlow builds what the prototype shows in your codebase.

## How it stays honest

EaseFlow is a persona-driven **cognitive walkthrough**, a long-established method for judging how easy a product is for first-time users. Research on AI-simulated users shows they tend to be too successful and too agreeable, so EaseFlow builds in counterweights:

- **Blind walkers.** Personas run as separate agents that see only what's on screen, never the code or the designer's reasoning.
- **Four questions per step.** Will they want to do it, see the control, understand it, and know it worked? Any "maybe" counts as a "no".
- **Default to fail**, with every finding tied to evidence. Findings without evidence are dropped.
- **Harold runs twice.** If the runs disagree, the worse result counts.
- **Measured accessibility** in live mode: real contrast, zoom and phone-width checks.
- **Blind re-test.** The new flow is judged by fresh agents, not by the one that designed it.
- **Real people last.** The test kit confirms the findings that matter before you build.

## Personas

Two core personas run every time:

- **Harold**, 70, wealthy, low tech comfort. He's the gold standard.
- **The Literal Follower**: does exactly what the screen says, like the dad in the PB&J "exact instructions" video.

Alex, the power-user guardrail, also runs every time. Each run then picks 2–3 personas from the library (`skills/easeflow/personas/`) and generates 1–2 for the product's real buyers. A product **passes** only when Harold and the Literal Follower pass, Alex doesn't fail, and no Blockers remain.

| Persona | Catches |
|---|---|
| Harold, 70 | Overall complexity, jargon, too many choices |
| The Literal Follower | Missing steps, vague labels |
| Priya, CEO | Slow time-to-value |
| Ramesh, shop owner | Unclear return on investment, setup that feels like work |
| Frank, the skeptic | Pricing and trust gaps, no undo |
| Linda, executive assistant | Handoff, sharing, roles |
| Grace, first-time digital user | Scary errors, missing reassurance |
| Ana, non-native English | Idioms, jargon |
| Jay, mobile only | Desktop-only layouts |
| Margaret, low vision | Zoom, contrast |
| Sam, distracted parent | Lost progress |
| Alex, power user | Over-simplification |

## Modes

- **Code only**: maps flows from routes, pages, forms and navigation.
- **Code + live app**: also walks the running app in a browser (local or staging URL) and captures screenshots as evidence. More accurate.

## Install

Link the skill into your personal skills folder, so edits to this repo apply straight away.

Windows (PowerShell):

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\easeflow" -Target "<path to repo>\skills\easeflow"
```

macOS / Linux:

```bash
ln -s "<path to repo>/skills/easeflow" ~/.claude/skills/easeflow
```

Start a new Claude Code session afterwards. Plugin-marketplace install will come with publishing.

## Run

Open any product's folder in Claude Code and say:

- *"Run EaseFlow on this product"*, or `/easeflow`
- *"Run EaseFlow. The app is running at http://localhost:3000"* (live mode)

Results go to `easeflow-report/` inside that product's folder.

## Repo layout

```
.claude-plugin/plugin.json      plugin manifest
skills/easeflow/
  SKILL.md                      the workflow
  personas/                     one file per predefined persona
  references/                   scoring, simplification rules, report template,
                                prototype guide, real-user test kit
  assets/prototype-skeleton.html  base for the themed, clickable prototype
  assets/showcase-template.html   before/after summary page, filled with run data
```

## Origin

The idea came from the "Exact Instructions Challenge" (PB&J) video: instructions only work when every step is stated and no word is vague. EaseFlow applies the same test to software.
