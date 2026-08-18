# RUBRICS — Applied to Every Assignment

Course-wide. Do not regenerate per assignment. Where a criterion varies by unit, the variation is listed inside it.

## Grading Protocol — applies identically whether the grader is human or an LLM

These rules exist because an AI grader can be misled in ways a careful human isn't — most importantly, it can reward language that *sounds* specific without checking whether the named thing actually exists in the code. Every rule below closes one such gap.

1. **Open the code before scoring the reflection.** Never score Accuracy, Plan-to-outcome linkage, or Diagnostic reasoning from the reflective response alone. Read the submitted code file first.
2. **An artifact only counts if it is verifiable in the submission.** A student who names a variable, line, function, or assumption that does not exist in the code scores **0 on Accuracy**, regardless of how specific or confident the language is. Specificity and accuracy are graded separately on purpose — do not let a high-specificity answer imply a high-accuracy score.
3. **Cite evidence for every score.** For each criterion, the grader records the score plus a one-line citation: the code line, quoted phrase, or specific gap that justifies it. A score with no citation is not valid output. This applies equally to a human TA's grading notes and an AI grader's output.
4. **Apply the runnable-code floor before totaling anything else.** Check whether the code runs first; if not, score all four reflection criteria normally, sum them, then cap at 10/20 and report both numbers.
5. **Borderline cases round down, and are flagged, not resolved silently.** If a response sits between two levels, assign the lower one and add a one-line flag for instructor review. This keeps AI-grader variance from inflating scores and gives the instructor a queue of cases to spot-check rather than a black box.
6. **Do not infer intent.** Score what the response and code state, not what the student probably meant. "The student likely meant X" is not evidence.
7. **Apply criteria identically regardless of response length, tone, or vocabulary.** This is stated in the rubric itself as well, but it is restated here because it is the rule most likely to be silently violated by a grader — human or AI — that is implicitly rewarding effort or fluency.

**Required grading output format** (both grader types produce this):

```
Criterion: [name]
Score: [n]  (or N/A)
Evidence: [one line — quote, line reference, or specific absence]
```

Followed by, in order: each section's applicable maximum and rescaled score, the floor status (applied / not applied), the allowed-set penalty (applied / not applied, with disallowed items listed), the final total, and any borderline flags.

## Scoring mechanics

**Word caps.** Pre-coding ≤100 words across all prompts in that section; post-coding ≤80; debugging ≤40 each. Read only up to the cap; ignore the remainder rather than penalizing it. The caps also appear at the head of each section in the student's response template.

**Absent work.** No reflection submitted → 0 on all four criteria; the floor is irrelevant. No code submitted → treat as failure to execute: score reflection normally, then apply the 10/20 cap. Missing individual answers score 0 on the criteria they would have supported; they are not N/A.

**N/A criteria and rescaling.** A criterion is N/A only when the assignment genuinely gave the student no occasion to demonstrate it:

- *Diagnostic reasoning is N/A* when the code runs and is fully correct **and** no debugging answers were submitted — a student whose program worked first time must not be penalized for having nothing to diagnose. If the code is incorrect and debugging answers are absent, score 0, not N/A.
- *Testing evidence (code rubric) is N/A* when the assignment does not require students to write functions.
- *Robustness (code rubric) is N/A* when the spec names no edge or boundary cases for units 1–6.

When a criterion is N/A: sum the applicable criteria, divide by the applicable maximum, multiply by the section total, and round to the nearest whole point. Record the applicable maximum in the output so the arithmetic is auditable.

**Determinism.** The same submission scored twice must yield the same result. Where a level descriptor could support two readings, apply the lower and flag it — do not resolve it by judgment call. Spot-check a sample of AI-graded submissions against the same rubric to confirm this holds.

**Allowed-set penalty.** Each assignment directory contains `allowed.md`, whose "Effective set" section lists every import and method permitted on that assignment, cumulative from unit 01. Use of anything outside that set costs **5 points off the assignment total**, applied once per assignment regardless of how many disallowed items appear.

- List every disallowed item found in the feedback, even though the penalty is charged once.
- Judge against `allowed.md` only. Do not decide from memory whether something "seems introductory" — if it is not in the effective set, it is disallowed. If `allowed.md` is missing, flag for instructor review and apply no penalty.
- The penalty is a deduction, not a criterion. Do not lower Correctness, Readability, or any other score because of a disallowed import; score the work on its merits, then deduct.

**Order of calculation** — apply in this sequence, and show each step:

1. Score every applicable criterion in both sections; mark N/A where warranted.
2. Rescale each section for N/A criteria (applicable sum ÷ applicable max × section total).
3. Apply the runnable-code floor to the reflection section if the code does not execute.
4. Add the two section scores.
5. Subtract 5 if the allowed-set penalty applies.
6. Floor the result at 0. A total cannot go negative.

Steps 2 and 5 must not be swapped: rescaling a penalty would make it worth something other than 5 points.

**Grade split: Code 80 · Reflective responses 20 = 100**

---

## A. Reflective Responses — 20 points

**Four binding rules** (see Grading Protocol above for how these are enforced mechanically)

1. **Score independently of whether the code is *correct*.** A student whose program produces the wrong output and who accurately diagnoses why earns full marks on specificity, accuracy, and diagnostic reasoning. Grading reflection on correctness suppresses honest failure reporting, which is the point of collecting it.
2. **Runnable-code floor.** If the submitted code does not execute on the stated input — syntax error, crash, no output — cap the total reflective score at **10/20**, regardless of how the four criteria below would otherwise score. The trigger is *failure to execute*, not wrongness: a program that runs cleanly but solves the wrong problem does **not** trigger the floor. A reflection cannot substitute for an executable program; it can substitute for a correct one.
3. **Score specificity, never length.** Named artifacts are the evidence — but only if they are real. Responses over the word cap are read only up to the cap.
4. **Never score** grammar, tone, enthusiasm, self-reported effort, or use of course vocabulary.

### Specificity — 7

Does the response name concrete things?

- **7** Names particular sub-tasks, lines, variables, types, inputs, or cases throughout.
- **5** One or two named artifacts; the rest described in general terms.
- **2** Describes activity without naming anything ("I tested it and fixed the errors").
- **0** Generic, or absent.

### Accuracy — 5

Does the reflection match the submitted code?

Two failure types, distinguished because they score differently:
- **Unsupported** — a claim the code neither confirms nor contradicts (e.g. "I planned this before coding").
- **Fabricated** — a named artifact that is affirmatively absent: a variable, function, line, or case the student names that does not exist in the submitted code. Fabrication caps this criterion at 0 regardless of the rest of the response.

- **5** Every claim about structure, sub-tasks, and failures is verifiable in the code; no fabrications.
- **3** One unsupported claim; no fabrications.
- **1** Two or more unsupported claims, or a program described meaningfully differently from the one submitted; no fabrications.
- **0** Any fabricated artifact, or unrelated to the submission.

*Note:* a fabricated artifact still counts toward Specificity — the two criteria are scored independently on purpose, so a fluent invention earns specificity points but loses all accuracy points. If you would rather fabrication cost both, say so and I will change it.

### Plan-to-outcome linkage — 4

Does the post-coding response connect to the pre-coding plan?

- **4** Names a specific divergence between plan and implementation and what triggered noticing it.
- **3** Notes that something changed, without saying what revealed it.
- **1** Asserts the plan was followed, no evidence.
- **0** No reference to the plan.

### Diagnostic reasoning — 4

Debugging responses: is the divergence point identified?

- **4** Names where expectation and behavior first differed, and which assumption that contradicted.
- **3** Names the location but not the assumption.
- **1** Describes the symptom only.
- **0** Jumps to the fix with no diagnosis, or debugging answers absent while the code is incorrect.
- **N/A** Code runs and is fully correct, and no debugging answers were submitted. Rescale per Scoring mechanics.

**Applying the floor:** score all applicable criteria first, rescale if any are N/A, then apply the 10/20 cap if the code does not execute. Record the raw sum, the applicable maximum, and the capped score, so the student can see what the reflection alone earned.

**Grader note to students:** Full credit on specificity, accuracy, and diagnosis is available when your code runs but produces the wrong answer. If your code does not run at all, reflective credit is capped at 10/20 even with an excellent diagnosis — a working program is a floor, not optional.

---

## B. Code Submission — 80 points

### Correctness — 25

- **25** Correct for all cases stated in the spec, including named edge cases.
- **17** Correct for typical cases; fails an edge case.
- **8** Partially correct, or correct only for the example input.
- **0** Does not execute, or executes but does not address the task.

### Decomposition quality — 20

- *Units 1–2:* **20** Distinct steps separated, each with a clear purpose; intermediate values held in well-named variables rather than buried in one expression. **13** Mostly separated, one step conflated. **6** Logic largely in one undifferentiated block. **0** No discernible structure.
- *Units 3–10:* **20** Each function does one job, takes meaningful parameters, returns a value, and could be tested alone. **13** One function does two jobs, or depends on a value it should receive as a parameter. **6** Functions exist but are arbitrary splits. **0** No functional decomposition where the problem warranted it.

### Robustness — 12

- *Units 1–6:* handling of edge and boundary inputs named in the spec.
- *Units 7–10:* anticipates realistic failures, catches specific exceptions near where they occur, reports skipped or bad records clearly.
- **12** Meets the above fully. **8** Handles the obvious case; broad `except` or one edge missed. **4** Single blanket try/except, or no boundary handling. **0** Absent where required. **N/A** Units 1–6 only, where the spec names no edge or boundary cases — rescale per Scoring mechanics.

### Readability — 12

- **12** Names describe what values represent; comments explain intent, not syntax.
- **8** Mostly clear; some placeholder names.
- **4** Names obscure meaning.
- **0** Unreadable without tracing.

### Testing evidence — 11

**Applies only to assignments that require students to write functions.** Testing means calling a function with chosen inputs and checking the returned value — no imported packages. On assignments whose deliverable is a script rather than functions, this criterion is **N/A**; rescale per Scoring mechanics.

- **11** Calls the function with inputs beyond the example, including at least one boundary or unusual case, and shows the results were checked against expectations.
- **7** Calls the function with the example plus one variation.
- **3** Ran the function once.
- **0** No evidence the function was executed.
- **N/A** The assignment does not require writing functions.

On script assignments (units 1–2, and later scripts), verification appears under Correctness and Robustness instead — do not double-count it here.

### Unit-9 substitution

For recursion assignments, Decomposition quality is scored as: **20** base case correct and reachable, each call provably reduces the problem. **13** Correct with a redundant or unreachable branch. **6** Base case present, reduction unclear. **0** Infinite recursion or no base case.

---

## C. Prompt Development — instructor use, not graded

Vet a generated prompt set before it reaches students.

**Gates — all must pass or the set is not shippable**

1. Every prompt tagged to exactly one stage.
2. Quotas met for the assignment's prompt count: comprehension monitoring or planning ≥4 (≥5 at unit 10), process monitoring ≥1, self-explanation ≤1.
3. No solution content anywhere.
4. Every prompt ≤40 words, one question mark.
5. No construct beyond the unit's band.
6. Both debugging prompts fire before any code edit.

**Quality — score 0–3 each; ship at ≥10 of 12 with nothing below 2**

- **Artifact specificity** — every prompt forces a named concrete thing.
- **Problem specificity** — the set could not be pasted onto a different assignment.
- **Method neutrality** — prompts name goals, never approaches.
- **Load compliance** — within all response caps and under 15 minutes total.
