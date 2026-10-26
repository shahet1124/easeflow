# Real-user test kit

AI personas are a fast first pass, but research on simulated users finds they're more successful and more agreeable than real people. Write `easeflow-report/real-user-test.md` so the user can check the prototype with **five real people** in about an hour total. Five participants usually surface most of the serious problems in a flow.

Write it for someone who has never run a usability test. Plain words, no research jargon.

## What to write

```markdown
# Test the new flow with real people

**What you need:** the prototype (`prototype.html`) on the device your customers use, 5 people, about 20 minutes each.

## Who to ask

<Describe 5 people matching this product's buyers, starting with someone like Harold: over 65, not confident with technology. Use people who have never seen the product. Friends, family and existing customers are all fine; colleagues are not.>

## Before you start (say this, word for word)

"Thanks for helping. I'm testing the app, not you, so you can't do anything wrong. Please think out loud as you go. I can't help you once we start, but tell me if you'd give up, and we'll stop there."

## The tasks (read each one out, then stay quiet)

1. "<First run: the core win as a real-life goal, without using any words from the product's screens. For example: 'Imagine you want to see your doctor next Tuesday. Use this to arrange it.'>"
2. "<A second core job, as a real-life goal.>"
3. "<A third core job, or 'coming back': something they'd do a week later.>"
4. "<A finding task: something occasional that now lives under More options or Advanced. For example: 'You've moved house. Change the address on your account.'>"

Keep it to four tasks. If they get stuck on one, move on to the next.

## Watch for (tick when it happens)

| What to watch | Person 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Task 1 finished without help | | | | | |
| Task 2 finished without help | | | | | |
| Task 3 finished without help | | | | | |
| Task 4: found it (where did they look first?) | | | | | |
| <the 2–3 report findings that most need confirming, e.g. "Paused at the 'Choose a plan' screen"> | | | | | |
| Said something was confusing (write what) | | | | | |
| Would they pay for this? (ask at the end: yes / maybe / no) | | | | | |

## Rules while watching

- Don't help, hint or explain. If they ask, say "What would you do if I weren't here?"
- Note where they hesitate for more than a few seconds.
- If they give up, that's a real result. Note the screen.

## After all five

- If **3 or more** got stuck at the same place, fix it before building.
- If only one did, note it, but don't redesign around one person.
- Share what you found with Claude and ask it to update the EaseFlow report and prototype.
```

## Rules for writing the kit

- **Word the task as a real-life goal**, never with the product's own labels. If the screen says "Create booking", the task must not say "booking".
- Pick the findings to confirm from the friction register: the Blockers the redesign fixes, and any spot where the two Harold runs disagreed.
- Match the device to the product type: phone for mobile apps and mobile-first products.
