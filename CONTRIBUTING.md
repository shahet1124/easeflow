# Contributing to EaseFlow

Thanks for helping make software easier for the people who pay for it. This guide explains what we're looking for, how to make a change, and the rules every contribution follows.

By taking part, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to help

| You want to… | Do this |
|---|---|
| Report something EaseFlow got wrong on a real product | Open a **Run report** issue |
| Report a broken template, script or instruction | Open a **Bug report** issue |
| Suggest a new persona | Open a **Persona proposal** issue first, then a PR |
| Suggest a new rule, metric or workflow change | Open a **Feature request** issue first, then a PR |
| Fix a typo or unclear wording | Open a PR directly |

For anything bigger than a wording fix, **open an issue first** so we can agree on the approach before you spend time on it.

## What makes a good contribution

EaseFlow is a set of instructions that Claude follows. Every word changes how it behaves on someone's product. So the bar is clarity, evidence and consistency, not volume.

**Good contributions:**
- fix a real failure seen on a real product run (say what happened),
- make an instruction more literal and less open to interpretation,
- add a persona that catches a kind of problem none of the existing ones catch,
- strengthen the safeguards against AI walkthroughs being too optimistic,
- improve the templates' accessibility, robustness or design.

**Contributions we'll usually decline:**
- personas that overlap heavily with existing ones,
- rules without a source or a real failure behind them,
- anything that lets EaseFlow drop features, edit code without approval, or skip the blind walkthroughs,
- industry-specific logic in the core skill (EaseFlow must work on any product),
- new runtime dependencies (the templates must stay single-file, no build step).

## The rules

These protect the skill's core promises. A PR that breaks one won't be merged.

1. **Nothing is lost.** EaseFlow changes how features are presented, never removes them. Any change must keep the feature ledger and the coverage gate intact.
2. **Code changes only on approval.** The skill never edits a product's code before the user approves the proposal.
3. **Outsiders walk blind.** Persona walkthroughs see only what's on screen. Don't give walkers access to code, reasoning or the ledger.
4. **Evidence or it didn't happen.** Every finding must cite a file, route or screenshot.
5. **Product-agnostic.** Examples should vary across industries. Don't tune the core skill for one product type.
6. **Plain words.** EaseFlow tells others to avoid jargon, so its own files must too. Short sentences, literal verbs, and no idioms.
7. **One concept, one name.** Reuse existing terms (core win, job, tier, disclosure level, friction point, Blocker/Major/Minor). Don't introduce synonyms.
8. **Cite research.** If a change is based on a study, method or guideline, link it in the PR.

## Project layout

```
.claude-plugin/
  plugin.json                 plugin manifest
  marketplace.json            lets people install the plugin straight from this repo
skills/easeflow/
  SKILL.md                    the workflow Claude follows (phases 0–8)
  personas/                   one file per persona, plus _template.md
  references/                 detailed method files the workflow points to
  assets/                     HTML templates (prototype skeleton, showcase)
scripts/validate.py           checks the repo's structure and consistency
.github/                      issue templates, PR template, CI
```

## Making a change

1. **Fork** the repo and create a branch: `git checkout -b persona/rural-user` or `fix/scoring-typo`.
2. **Install your fork locally** so Claude uses your version (see [Install for development](#install-for-development)).
3. **Make the change.** Keep it focused: one persona, one rule, or one fix per PR.
4. **Run the validator:**
   ```bash
   python scripts/validate.py
   ```
5. **Test it on a real product** if the change affects behaviour (see [Testing a change](#testing-a-change)).
6. **Update `CHANGELOG.md`** under `Unreleased`.
7. **Open a pull request** and fill in the template.

### Install for development

Point your personal skills folder at your clone, so edits apply straight away.

Windows (PowerShell):

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\easeflow" -Target "<your clone>\skills\easeflow"
```

macOS / Linux:

```bash
ln -s "<your clone>/skills/easeflow" ~/.claude/skills/easeflow
```

If you already installed the published plugin, disable it while developing so the two versions don't compete.

### Testing a change

Changes to `SKILL.md`, personas, scoring or rules change Claude's behaviour, so test them:

1. Pick a real product you can run, ideally one you know well. Small open-source apps work well.
2. Run EaseFlow on it before and after your change.
3. In the PR, describe what changed in the output: for example, "Harold now gets stuck at X, which matches what we saw with a real user", or "the ledger now catches the export settings it missed before".

Don't commit `easeflow-report/` folders or anything from the products you tested on.

## Adding a persona

1. Open a **Persona proposal** issue: who they are, what kind of problem they catch, and why no existing persona catches it. Link research if you have it.
2. Once agreed, copy `skills/easeflow/personas/_template.md` to `skills/easeflow/personas/<firstname>-<trait>.md`.
3. Fill in every section. **"Gives up when"** and **"Patience budget"** must be concrete and checkable: "two screens in a row without a labelled next step", not "gets confused easily".
4. Add the persona to the table in `README.md` and to the library guidance in `SKILL.md` Phase 2 if it needs a "use when" hint.
5. Run `python scripts/validate.py`.

Personas describe people with respect. Base them on research and real observation, never on stereotypes or jokes.

## Changing rules, scoring or the workflow

- **Simplification rules** are numbered (R1, R2, …). Add new rules at the end of their section with the next free number. Never renumber, because reports cite rule numbers.
- **Scoring** changes affect every run's comparability. Explain why the old weighting was wrong, with an example.
- **Workflow phases** in `SKILL.md`: keep each phase's instructions literal and ordered. If you add a step, say exactly what it produces and where it's saved.
- **Templates** (`assets/`): keep them single-file, dependency-free, accessible (contrast, focus, 44px targets, works at 375px wide) and with light and dark themes. Check them in a browser before opening the PR.

## Style guide

- Write in plain, direct English. Second person ("you") when instructing Claude.
- Use sentence case for headings.
- Prefer tables and numbered steps over long paragraphs.
- Bold only the key term or decision in a sentence.
- File names are lowercase with hyphens.

## Commit messages

Use a short, imperative subject line (under 72 characters), then a blank line and a body if needed:

```
Add Rosa, a rural user on slow connections

Catches pages that need a fast connection to work.
```

## Reviews and releases

- A maintainer reviews every PR. Expect questions. They're about keeping the skill consistent, not about you.
- CI must pass.
- Releases follow [Semantic Versioning](https://semver.org): **major** for changes that alter how runs are scored or what they produce, **minor** for new personas, rules or features, **patch** for fixes and wording.
- Maintainers update `version` in `.claude-plugin/plugin.json`, move `Unreleased` items in `CHANGELOG.md` under the new version, and tag the release.

## Questions

Open a [Discussion](../../discussions) or an issue. There are no silly questions here. That's rather the point of this project.
