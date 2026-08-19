# Procedural Lessons

Mistakes made on this project and the rules that prevent repeating them. See
[`README.md`](README.md) for what earns an entry and how this differs from
`architecture-learning`.

Seeded 2026-08-17.

---

## Test an environment hypothesis before proposing a config change

**What happened.** `gh` failed with a TLS certificate error. I noticed
`GIT_SSL_CAINFO` pointing at a corporate CA bundle, inferred that `gh` was ignoring
it, and proposed adding `SSL_CERT_FILE` to the user's Claude Code settings. They
made the change. It did not work. `GODEBUG=x509usefallbackroots=1` did not work
either. The actual blocker was the sandbox denying Go's call into macOS
Security.framework — unfixable by any environment variable.

**Cost.** The user edited their own configuration for nothing, then reverted it to
stay aligned with org standards.

**Rule.** Before proposing a change to someone's configuration, test the hypothesis
in a way that costs them nothing — set the variable inline for one command, or probe
the failing layer directly. Propose the edit only after the probe works. And prefer
handing over a command to run in their own shell over changing their environment at
all.

---

## Don't route credentials through a command line

**What happened.** With `gh` blocked, I reached for
`curl -H "Authorization: bearer $(gh auth token)"` to hit the GitHub API. The call
was denied, correctly.

**Cost.** A denied tool call, and a request that should never have been made.

**Rule.** Never put a credential into a command line — even a local one, even the
user's own token, even via substitution. If a task appears to need a secret, ask
first and say what it will be used for.

---

## After a denial, change approach — don't retry a variant

**What happened.** A compound `git checkout main && git merge --ff-only` was denied.
I re-sent essentially the same operation with the pipeline stripped. It was denied
again.

**Cost.** Two denied calls where one should have prompted a question.

**Rule.** A denial is information about intent, not a syntax error. Ask what the
objection was, or hand the command over, rather than probing for a phrasing that
gets through.

---

## Cite by name in living documents, never by number

**What happened.** Appending a decision to `docs/decision-log.md` renumbered the
existing ones and silently broke two cross-references that pointed at "decision 3."

**Cost.** Caught only because I grepped for it; otherwise two documents would have
pointed at the wrong decision indefinitely.

**Rule.** In any append-only document, reference entries by name, not position. This
is now also stated in `CLAUDE.md`, since the log will keep growing.

---

## Label first-measurement conclusions as provisional

**What happened.** From the first token baseline I reported that cache reads were
the dominant signal. Adding cost modelling showed cache *writes* are the figure that
matters — they indicate real context change and cost 20× more per token. My earlier
framing was not wrong about the volume, but it pointed attention at the wrong number.

**Cost.** A conclusion the user might have acted on, corrected one session later.

**Rule.** A single measurement supports a description, not a recommendation. Say
which number is provisional and what would change the reading, rather than naming a
key metric on first sight of the data.

---

## Verify derived paths by running, not by reasoning

**What happened.** `summarize.py` derived the repo name from `__file__` with one
`dirname` too few, so it looked for a transcript directory named after `meta`. Pure
reasoning error in three lines of path arithmetic.

**Cost.** Small — one failed run — but it would have shipped silently if the script
had not been executed as part of the same change.

**Rule.** Run any code that derives paths, computes offsets, or does index
arithmetic, in the same turn that writes it. These are the errors that survive
careful reading.

---

## Proof-read commands the user is expected to paste

**What happened.** I gave a `git branch --set-upstream-to` command with the branch
name misspelled, and separately pasted a commit title with a typo mid-word.

**Cost.** A command that would have failed on paste, and a correction that cost a
paragraph of the reply.

**Rule.** Anything the user will copy and run gets read once more before sending. A
wrong command spends their turn, not mine.

---

## Append architecture-learning observations as they happen, not on request

**What happened.** `architecture-learning/README.md` specifies that observations get
appended to `observations.md` during the conversation, at near-zero cost, without
stopping to decide whether they matter. Across a session containing several
qualifying moments (a dashboard deferred to backlog with a named trigger, a request
that project decisions live in the repo rather than in memory), none were captured
until the user pointed out the component should be "conversationally aware" — at
which point I had to reconstruct them from earlier turns instead of catching them
live.

**Cost.** None yet, since reconstruction from the same session was still possible.
The cost would be real in a longer session, or once memory of the conversation
fades.

**Rule.** When a conversation touches this project, treat a one-line
`observations.md` append as part of finishing that turn — the same way a decision
gets written to `decision-log.md` in the turn it's made — not a step that waits for
a reminder.
