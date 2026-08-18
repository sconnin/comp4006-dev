# CLAUDE.md — Python Course Assignments

## Project

10-unit introductory Python course. Each assignment is a subdirectory: `NN-name/`, or `NNx-name/` where a unit has several (`01a-`, `01b-`). Leading digits give the unit number.

**Units:** 1 Intro / Variables / Boolean Logic · 2 Control Flow · 3 Functions · 4 Lists & Tuples · 5 Strings & Sets · 6 Dictionaries · 7 File I/O & Exceptions · 8 Classes · 9 Recursion · 10 Independent Project

Functions is unit 3, before collections. No function-decomposition prompts before unit 3.

## Rule precedence

A `.md` file inside an assignment subdirectory takes precedence over this file wherever the two contradict. Root rules apply to everything the subdirectory file is silent on.

- When you follow a subdirectory rule that contradicts this file, say so explicitly in your report: name the file, the root rule overridden, and the subdirectory rule applied. Never apply an override silently.
- Precedence resolves contradictions only. A subdirectory file cannot waive a rule it does not address.
- If two files in the same subdirectory contradict each other, stop and ask.

This precedence covers the generation rules in this file. `RUBRICS.md` is course-wide; treat its scoring rules as fixed unless I change that file directly.

## Allowed imports and methods

Every assignment directory contains `allowed.md`. It has two sections:

- **New in this assignment** — imports and methods the instructor introduces here. Instructor-maintained.
- **Effective set** — the cumulative union of every `allowed.md` from unit 01 through this assignment, in directory order. You generate this section on request; never edit "New in this assignment."

The effective set is what graders read. Regenerate it whenever an earlier assignment's `allowed.md` changes, and report which downstream assignments were affected.

Rules for prompt writing:

- Never name an import or method outside the assignment's effective set — not in a prompt, an example, or a sample output.
- If you are unsure whether something is in the effective set, read `allowed.md`. If it is absent there, treat it as disallowed rather than assuming.
- If `allowed.md` is missing from an assignment directory, stop and ask. Do not infer the allowed set from the spec or from the unit number.

## Scope

Apply when I ask for reflective prompts. Do not generate unprompted. **Rubrics are course-wide and already written — see `RUBRICS.md`. Never generate per-assignment rubrics.**

## Procedure

1. Read the assignment spec. If absent, stop and ask.
2. Name the one failure this problem invites — misread spec, wrong type, off-by-one, wrong container, unhandled input. Prompts target that failure.
3. Set the band from the unit number.
4. Draft, run the checklist, rewrite failures.
5. Write `<assignment-dir>/reflection-prompts.md`. Never overwrite; use `-v2` and say so. Report the failure mode from step 2.

## Format

Three `##` sections: Pre-Coding, Post-Coding, Debugging. 3 / 2 / 2 prompts (unit 10: 4 / 3 / 2). Number each; tag beneath as `*Stage N · [regulation type]*`. State the response cap at the top of each section.

**Stages:** 1 Reinterpret the prompt · 2 Find analogous problems · 3 Find solutions · 4 Evaluate a solution · 5 Implement · 6 Evaluate the implementation

**Regulation types** (tag each prompt with exactly one; this list is closed): planning · process monitoring · comprehension monitoring · reflection on cognition · self-explanation

## Response template

Alongside `reflection-prompts.md`, write `<assignment-dir>/reflection-template.md`: the same numbered prompts with a blank answer space beneath each, and the word cap for that section at its head. Students submit this file completed. Graders must be able to map every answer to its prompt number without inference.

## Required content

- **Pre-coding** — one Stage 1 reinterpretation; one predicting exact output for a stated input before coding; from unit 3, one listing intended sub-tasks.
- **Post-coding** — both compare what was built to the plan; one names what changed and how the student noticed.
- **Debugging** — both open "Before you change any code:"; one asks which original assumption the behavior contradicts.

## Quotas

Per assignment: **comprehension monitoring or planning ≥ 4** · **process monitoring ≥ 1** · **self-explanation ≤ 1**. Reflection on cognition is permitted but never required.

Unit 10 (9 prompts): comprehension monitoring or planning ≥ 5, process monitoring ≥ 1, self-explanation ≤ 1.

## Testing scope

Testing is required **only on assignments that ask students to write functions** — unit 3 at the earliest, and only where the spec actually calls for a function. It is not required on units 1–2, nor on any later assignment whose deliverable is a script rather than functions.

Testing in this course uses no imported packages. It means calling a function directly with chosen inputs and checking the returned value against what the student expected.

- Prompts may ask about testing only on function-writing assignments, and only in terms of the assignment's effective allowed set.
- On non-function assignments, ask about *verification* instead — running the program and checking its output — not testing.
- A process-monitoring prompt asking "how did you confirm this worked" is valid on every unit; the expected answer is running-and-checking on units 1–2 and function-level testing from unit 3 where functions are required.

## Bands

- **Units 1–2, concrete:** a variable, line, printed value, condition, input.
- **Units 3–6, structural:** sub-tasks, function boundaries, return values, container choice.
- **Units 7–10, strategic:** approach, alternatives rejected, anticipated failure.

Never presume a construct not yet taught.

## Unit extras

- **1 (Boolean):** enumerate every case, name one nearly missed.
- **7:** list anticipated failure points before any `try`.
- **8:** separate attributes from methods before coding.
- **9:** state base case and reduction step separately; one debugging prompt asks what the recursive call was assumed to return.
- **10:** name a structurally analogous earlier problem and the shared element.

## Limits

Prompt ≤40 words, one question mark, no compound clauses. Responses: pre-coding ≤100 words total, post-coding ≤80 total, debugging ≤40 each — these are hard caps, and graders read only up to the cap. Total reflective time ≤15 minutes. At most one prompt asks for a list. Self-contained: the spec and the student's own code, nothing else. No untaught vocabulary; never say "metacognition" or "decomposition" to students.

## Grading compatibility

Reflective responses will be scored by human TAs and by LLM graders, using the same rubric and evidence-citation rules (`RUBRICS.md`). Prompts must be written so either grader can verify the answer against the code without having solved the problem themselves.

- Every required artifact (sub-task, line, variable, assumption, case) must be something a grader can locate and confirm in the submitted code — not something only the student can judge.
- Do not write prompts whose "correct" answer is a matter of the student's private intent or feeling. If a grader can't check it against the code, it isn't a decomposition prompt.
- Avoid prompts a student could answer plausibly without having solved *this* problem — an AI grader is more easily satisfied by confident, generic language than a human is, so problem-specificity (rule 4 in the checklist) matters more here, not less.

## Checklist — every prompt, all yes

1. Tagged to one stage.
2. Answer requires naming a specific artifact — sub-task, line, type, assumption, input, case.
3. Names a goal, not a method.
4. Unanswerable without this particular problem.
5. Inside the band; no untaught constructs.
6. No solution content — code, pseudocode, skeleton, or the sub-task list itself.
7. Within length and single-question limits.
8. Answerable at the moment it fires.
9. Verifiable by a grader against the code alone, without needing to have solved the problem or know the student's private reasoning.
10. Names no import or method outside this assignment's effective allowed set.

Report a prompt that fails twice rather than rewriting a third time.

## Reference

`.claude/decomposition-research.md` — the evidence behind these rules. Read only when revising them.
