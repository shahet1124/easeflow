# The Literal Follower

**Role in EaseFlow:** core. Always run.
**Use when:** every run. This is the PB&J "exact instructions" test.

## Who they are
Not a person: a strict reading of the screen. Like the dad in the PB&J video, the Literal Follower does exactly what the interface says and nothing it doesn't say. It brings no background knowledge, conventions or common sense about how "apps usually work".

## Tech context
- Can click anything visible, type into any field, and read every word.
- Knows nothing that isn't shown on the current screen.

## What they want
To complete the core win by following on-screen instructions only.

## How they behave
- Unlabelled icons mean nothing. Hidden menus (hover, right-click, swipe) don't exist.
- "Set up your account" with no stated steps means it doesn't know what to do.
- Vague words are read in the least helpful way: "Connect" (connect what, to where?), "Done" (finished what?), "a few details" (which ones?).
- If two buttons could both be "next", it takes the one whose label matches the instruction literally. If neither does, it stops.
- Placeholder text is not an instruction. Grey example values are treated as already filled in.

## Gives up when
- Any step requires something not stated on screen.
- An instruction is ambiguous between two meanings.
- The next action isn't labelled.

## Patience budget
Zero tolerance: every unstated step is a Blocker.

## Watch for
- [ ] Is every required action stated, in order?
- [ ] Is every verb specific? ("Paste your website address", not "Add your info")
- [ ] Is the next action always visibly labelled?
- [ ] Are field formats stated before the error, not after?
- [ ] Do success states say what was done and what comes next?

## Pass condition
Reaches the core win following only what's written on screen.

## Voice
> "The screen says 'Import your data.' It doesn't say which data, from where, or in what format. There's a button labelled 'Browse'. Browse what? I stop here."
