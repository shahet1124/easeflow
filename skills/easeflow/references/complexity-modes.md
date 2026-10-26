# Handling complexity: disclosure and Advanced mode

A big product can stay simple without losing anything, by showing each feature at the right moment. Use the **cheapest level that works** for each feature. Only reach for a separate Advanced mode when the levels below it aren't enough.

## The disclosure ladder

Climb only as far as you need, per feature:

1. **Automate it.** Smart defaults and automation remove the choice entirely, but it can still be changed.
2. **Show it in context.** It appears only where and when it applies.
3. **More options.** A clearly labelled "More options" on the same screen. Always say what's inside ("More options: repeat, reminders, notes").
4. **An Advanced section per area.** Each object or job area has its own "Advanced" section for its rare features.
5. **Role-based views.** Owners and admins see admin areas; everyone else doesn't. Use this when the product already has roles.
6. **A global Advanced mode.** A single switch that adds expert tools across the whole product. Last resort.

Progressive disclosure (Nielsen's "staged disclosure") works because novices see only what they need, but it fails when experts can't find what's hidden, or novices can't get back to a safe state. So: every hidden thing has a visible, labelled way in, and every expanded thing has a way back.

## When to recommend a global Advanced mode

Recommend one **only when all three** are true. Write the evidence for each in the report:

1. **There's a distinct expert audience** that uses the product heavily (daily or all day), for example operators, analysts or agency staff, alongside occasional or non-technical users.
2. **Advanced features are spread across most areas**, so per-area "More options" and Advanced sections would clutter nearly every screen. A rough signal: Advanced-tier features are over about a third of the ledger, or appear in most areas.
3. **Experts need a different layout**, not just more buttons: dense tables, bulk editing, keyboard-driven work, multiple panes, raw data views.

If any of these is false, **don't add a mode**. Use levels 1–5. Most products don't need one.

If the product **already has** a mode, beginner view or similar, evaluate it against the rules below rather than adding another.

## Rules for Advanced mode, if recommended

Research and practice on modes agree on what goes wrong: users forget which mode they're in, and modes that change how familiar controls behave cause errors. So:

- **Simple is the default.** New users, and Harold, never need to switch to complete any core job.
- **Advanced only adds.** It adds tools, columns, panels and shortcuts. It never moves, renames or changes the behaviour of anything that exists in Simple.
- **Same structure, same data.** Both modes share navigation, objects and data. Switching never loses work or changes what's saved.
- **Always visible state.** A clear indicator shows which mode is on, and the switch is in one predictable place (for example, the user menu).
- **Per person, remembered.** Each user's choice is saved. One person switching doesn't change it for others.
- **Named plainly.** "Simple view" and "Advanced view", not "Pro mode" or "Expert++".
- **Reachable without the mode.** Each Advanced feature still has a home (Advanced section or More options) for people who need it once and won't switch modes.

## Roles

If the product has roles, simplify **per role**. Each role sees only the jobs it does. Admin-only features go in an admin area that other roles never see. Walk the core jobs of each role separately.

## Consistency across a big product

In large products, simplicity comes from **learning once and using everywhere**:

- The same pattern for the same kind of task in every area (create, edit, find, delete, export).
- "More options" and "Advanced" always in the same position.
- One name per concept across the whole product, matching the ledger's plain names.
