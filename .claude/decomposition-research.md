# Research Grounding for the Prompt-Generation Rules

Read only when revising the rules in CLAUDE.md or justifying one. Not needed for routine prompt generation.

**Sources:** Loksa, Ko, Jernigan, Oleson, Mendez & Burnett (2016, CHI) · Loksa & Ko (2016, ICER) · Loksa, Margulieux, Becker, Craig, Denny, Pettit & Prather (2022, TOCE)

---

## Which rule rests on which finding

| Rule in CLAUDE.md | Finding | Source |
|---|---|---|
| Stage 1 required in every pre-coding set | Only 15 of 37 novices verbalized any reinterpretation of the prompt; students began coding before understanding, then had to stop mid-implementation | Loksa & Ko 2016 |
| Comprehension monitoring + planning ≥ 4 of 7 | Regression models: comprehension monitoring ~3-error decrease, planning ~1-error decrease per verbalization (CS2 group) | Loksa & Ko 2016 |
| Self-explanation ≤ 1 | Self-explanation predicted *more* errors; authors read verbalized self-explanation as a struggle signal, not a cause of success | Loksa & Ko 2016 |
| Process monitoring ≥ 1 | Falkner et al.: none of 841 student-reported strategies fell into "keeping records and monitoring" — a complete blind spot | via TOCE 2022 |
| Test-case prediction required pre-coding | Prather et al.: higher completion, less time, fewer submissions. Craig et al. (n=831): helps when students misread the prompt (Stage 1), not when they struggle with implementation (Stages 4–5) | via TOCE 2022 |
| Debugging prompts as pre-edit gates | Parham et al.: debugging schema and goal-replanning co-occurred in only ~12% of observed actions; novices fix without revisiting goals | via TOCE 2022 |
| Analogical-transfer prompt at unit 10 | 83% of analogous-problem searches occurred where worked examples were visible; students largely stopped searching on context-shifted problems | Loksa & Ko 2016 |
| "Name the goal, not the method" | The CHI intervention deliberately taught what each stage achieves without prescribing how | Loksa et al. 2016 |
| Calibration bands by unit number | Self-regulation was only effective alongside adequate programming knowledge; disciplined self-regulation without it may exhaust and frustrate learners | Loksa & Ko 2016 |
| Require a nameable artifact | Measurable signal of improved metacognition was students *naming specific strategies* and writing more, not reflecting more warmly | Loksa et al. 2016 |

## The six problem-solving stages

1. Reinterpret the problem prompt
2. Search for analogous problems
3. Search for solutions
4. Evaluate a potential solution
5. Implement a solution
6. Evaluate the implemented solution

Nominally sequential, revisited iteratively as students discover what the problem actually requires.

## The five self-regulation types

Planning · Process monitoring · Comprehension monitoring · Reflection on cognition · Self-explanation

## Ko's six learning barriers — for coding help requests

**Design** (don't know how to start) · **Selection** (don't know which feature to use) · **Use** (don't know how to use a feature) · **Coordination** (can't combine features) · **Understanding** (see a failure, no theory why) · **Information** (have a theory, can't confirm it)

A healthy shift over a term runs from design/selection toward understanding/information — students getting further before getting stuck. This was the observed effect of the CHI intervention.

## Help-request template (worth adopting alongside the prompts)

1. What am I trying to make happen?
2. What have I already tried?
3. Which stage am I stuck in?

## Grounding for the load limits

Self-regulation was only effective when paired with adequate programming knowledge; Loksa & Ko warn that disciplined self-regulation without sufficient knowledge may only exhaust and frustrate learners. The TOCE survey adds that internal-process measures like think-aloud are unreliable precisely because they are used during periods of high cognitive load. Both point the same direction: reflective demands that compete with the coding task will be abandoned or performed insincerely. Hence the word caps, single-question rule, and 20% time ceiling.

## Grounding for the reflection rubric rules

- **Credit independent of code success.** The CHI end-of-day survey question explicitly invited failure reporting — students were asked what they tried if they did not solve the problem. Grading reflection on whether the code worked would suppress exactly the responses that carry diagnostic signal.
- **Specificity over length.** The measurable difference between groups was that students *named specific strategies*; greater word count was a side effect. Meanwhile self-explanation volume predicted more errors, so rewarding elaboration risks rewarding struggle.
- **Decomposition weighted in the code rubric.** Falkner et al. found decomposition among the CS-specific strategies novices report, and that CS-specific strategy use rises with expertise (1:1 for novices, 1.6:1 for final-year students). Making it a graded criterion keeps it visible rather than incidental.

## Cautions

- Hull & du Boulay added motivational and metacognitive feedback to a tutoring system and found **no significant learning gains**. Prompts are not self-evidently effective.
- The TOCE survey's central criticism of the field: studies invoke metacognition as motivation and then never measure it. If these prompts are worth deploying, they are worth checking — count named strategies per response and track help-request barrier types across the term.
