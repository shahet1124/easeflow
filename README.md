# EaseFlow

**If a 70-year-old who's great with money but not with tech can use your product alone, it's a good product.**

EaseFlow is a Claude Code skill you run on a finished product. It maps how the product really works, walks through it as a set of non-technical buyer personas who follow every screen literally, scores how easy it is, and proposes a simple, sellable flow with a one-time guided onboarding.

Developers build what feels easy to developers. The people who pay usually have money and little time, not tech familiarity. EaseFlow closes that gap.

## What you get

1. **Clickable prototype** (`easeflow-report/prototype.html`): your product in its own design theme (colours, fonts, logo, components), rebuilt around EaseFlow's simplified flow. It runs from sign-up through the guided onboarding to the core win. It looks like your app, made simple.
2. **Report** (`easeflow-report/report.md`): friction points ranked by severity, a score and pass/fail for each persona, before vs. after, and screen-by-screen changes.
3. **Flow diagrams**: the current flow vs. the proposed flow (Mermaid, inside the report).
4. **Before/after showcase** (`easeflow-report/showcase.html`): a one-page summary of the scores and both flows, linking to the prototype, ready to show clients or your team.
5. **Optional fixes**: only after you approve, EaseFlow builds what the prototype shows in your codebase.

## Personas

Two core personas run every time:

- **Harold**, 70, wealthy, low tech comfort. He's the gold standard.
- **The Literal Follower**: does exactly what the screen says, like the dad in the PB&J "exact instructions" video.

Each run also picks 3–4 personas from the library (`skills/easeflow/personas/`) and generates 1–2 for the product's real buyers. A product **passes** only when Harold passes and Alex (the power-user guardrail) doesn't fail.

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
- **Code + live app**: also walks the running app in a browser (local or staging URL) and captures screenshots as evidence.

## Install

As a plugin (from a local clone):

```bash
claude plugin install ./EaseFlow
```

Or copy the skill into your personal skills folder:

```bash
cp -r skills/easeflow ~/.claude/skills/easeflow
```

Then in any project, ask Claude: *"Run EaseFlow on this product"*, or use `/easeflow`.

## Repo layout

```
.claude-plugin/plugin.json      plugin manifest
skills/easeflow/
  SKILL.md                      the workflow
  personas/                     one file per predefined persona
  references/                   scoring, simplification rules, report template, prototype guide
  assets/prototype-skeleton.html  base for the themed, clickable prototype
  assets/showcase-template.html   before/after summary page, filled with run data
```

## Origin

The idea came from the "Exact Instructions Challenge" (PB&J) video: instructions only work when every step is stated and no word is vague. EaseFlow applies the same test to software.
