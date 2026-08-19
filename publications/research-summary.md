# Research Summary — Metacognition, Self-Regulation, and Reflective Prompts in Programming Education

Three papers, summarized for what they imply about writing effective, actionable reflective
decomposition prompts for introductory Python students.

- Loksa, Ko, Jernigan, Oleson, Mendez, & Burnett (2016). *Programming, Problem Solving, and
  Self-Awareness: Effects of Explicit Guidance.* CHI 2016.
- Loksa & Ko (2016). *The Role of Self-Regulation in Programming Problem Solving Process and
  Success.* ICER 2016.
- Loksa, Margulieux, Becker, Craig, Denny, Pettit, & Prather (2022). *Metacognition and
  Self-Regulation in Programming Education: Theories and Exemplars of Use.* ACM TOCE.
- Rich, Egan, & Ellsworth (2019). *A Framework for Decomposition in Computational Thinking.*
  ITiCSE 2019.

---

## 1. Naming the process explicitly is what makes prompts effective, not prompting alone

The CHI 2016 paper's strongest result is that *explicit instruction on the problem-solving
stages themselves* — not just prompting students to reflect — is what moved outcomes
(productivity, self-efficacy, growth mindset). The intervention that worked combined four
things: a lecture naming six problem-solving stages, a physical tracker for which stage a
student was in, on-demand prompts asking students to name their current stage, and
context-sensitive hints tied to that stage.

**Implication for this course's prompts:** a prompt only works if the student has already been
taught the vocabulary it uses. This matches the course's own "no untaught vocabulary" rule and
the unit-by-unit stage bands already in `CLAUDE.md` — the research gives a concrete reason for
that constraint, not just a style preference. A comprehension-monitoring prompt asking about
"sub-tasks" is doing real cognitive work only from Unit 3 onward, once students have been taught
what a function boundary is.

## 2. Six problem-solving stages map directly onto the existing prompt "Stages"

Loksa et al.'s stage model — reinterpret the problem prompt, search for analogous problems,
search for solutions, evaluate a potential solution, implement a solution, evaluate the
implemented solution — is the direct ancestor of the six stages already defined in `CLAUDE.md`
(reinterpret the prompt · find analogous problems · find solutions · evaluate a solution ·
implement · evaluate the implementation). The two studies validate that this decomposition is
not arbitrary: it is the one used to code think-aloud transcripts and to structure explicit
instruction that produced measurable gains.

**Implication:** the existing Stage tagging in `reflection-prompts.md` is well-grounded. Where it
could be sharpened is in *balance*: the ICER paper found that reinterpreting the problem and
evaluating solutions were the stages novices skipped most — only 15 of 37 participants ever
verbalized reinterpreting the prompt, and just half verbalized evaluation. These are exactly the
stages current quotas should protect, since students underuse them without prompting.

## 3. Self-regulation types are uneven in both frequency and effectiveness — this should drive quota weighting

The ICER 2016 paper's five self-regulation types (planning, process monitoring, comprehension
monitoring, reflection on cognition, self-explanation) are the direct source of this course's
"regulation types" taxonomy. Three findings matter for how prompts should be weighted:

- **Comprehension monitoring and planning were the only two types with a measurable
  relationship to fewer errors** (more of each correlated with fewer errors, for the more
  experienced group in the study). This supports the course's existing rule that comprehension
  monitoring or planning must appear at least 4 times per assignment — the research backs that
  minimum, it isn't an arbitrary floor.
- **Self-explanation was not associated with fewer errors, and for more experienced students it
  was associated with *more* errors.** The paper's interpretation: students self-explain more
  when they are already struggling, so its presence is a symptom, not a fix. This directly
  supports the course's cap of self-explanation ≤ 1 per assignment — over-relying on
  self-explanation prompts risks rewarding articulate confusion rather than accurate
  understanding.
- **Process monitoring was rare (median of 0–1 per student across six problems) but not linked
  to errors either way.** It functioned more as a way for students to segment their work than as
  a corrective mechanism. This is consistent with treating it as a light-touch, low-quota
  requirement (≥ 1 per assignment) rather than a heavily weighted one.

## 4. Self-regulation is only useful once there is enough domain knowledge to regulate

Both empirical papers converge on the same warning: *prompting a student to reflect does not
help if they don't yet have the programming knowledge to act on the reflection.* The ICER paper
found that CS1 participants' self-regulation attempts were frequent but shallow and largely
ineffective at reducing errors, while more experienced (CS2) participants' self-regulation,
though also imperfect, related more clearly to fewer errors. The authors' explicit hypothesis is
a **timing effect**: self-regulation skill without adequate prior knowledge may exhaust and
frustrate learners rather than help them.

**Implication:** this is the strongest evidence in the corpus for the course's existing
unit-by-unit bands (concrete → structural → strategic) and for keeping early prompts anchored to
something concrete (a variable, a line, a printed value) rather than asking early students to
reason abstractly about their own strategy. A Unit 1 student asked a Unit 7-style "what
approach did you take and what did you reject" prompt is being asked to regulate knowledge they
don't have yet — the research suggests this could be actively counterproductive, not just
ineffective.

## 5. Concrete, problem-specific prompting outperforms generic reflection

The CHI 2016 intervention worked in part because it was concrete: a physical token to track
current stage, hints tied to the *specific anti-pattern* a student's code exhibited (e.g., an
icon appearing next to a `for` loop missing an iterator pattern), and help-request prompts that
asked students to name their *current* problem-solving state before receiving help. Campers who
received this scaffolding wrote significantly longer, more specific descriptions of their own
strategies at the end of each day than the control group (both in count of named strategies and
in word count) — evidence that concrete, in-the-moment framing produces more specific
self-reports than an unprompted "how did it go" question would.

**Implication:** this is direct support for two rules already in `CLAUDE.md`: that prompts must
require naming a specific artifact (a line, a variable, a sub-task) rather than allowing vague
"private intent" answers, and that graders must be able to verify the answer against the
submitted code. The research shows this isn't just a grading-practicality rule — concreteness is
also what produces higher-quality self-regulation in the first place.

## 6. Novices barely reinterpret the problem or evaluate solutions unless asked — pre-coding and post-coding prompts should target these directly

The ICER study's biggest surprise: of 37 participants, only 15 ever verbalized reinterpreting the
problem prompt, and this was concentrated on the two *hardest*, most unfamiliar problems — not
spread evenly. Evaluation of a completed solution was similarly rare (under half of CS1
participants). Left unprompted, novices tend to start coding before they've fully understood the
problem, then hit knowledge gaps mid-implementation that could have been caught earlier.

**Implication:** this validates the mandatory Stage-1 reinterpretation prompt already required in
Pre-Coding. It also motivates Post-Coding's retrospective prompts (which exercise was actually
hardest, where the first approach broke down) — without a required prompt, novices are unlikely to
evaluate what they built against what they expected on their own. (An earlier version of this
course's Post-Coding section asked students to compare their code to an explicit "pre-coding
plan"; that framing was dropped because no pre-coding prompt actually produced a plan artifact to
compare against — see `reflection-prompts.docx` for the current, plan-free version.)

## 7. Terminology across metacognition/self-regulation/SRL is genuinely inconsistent in the field — a reason to keep this course's vocabulary closed and simple

The 2022 TOCE review's most notable finding is second-order: even researchers cannot agree on
clean boundaries between "metacognition," "self-regulation," and "self-regulated learning" (SRL)
— the review states outright that "the distinctions between these terms are as unspecified as the
definitions of each term." Multiple competing theoretical models exist (Flavell, Bandura,
Zimmerman, Pintrich, Boekaerts, Efklides, Winne & Hadwin, Hadwin et al.), each carving up the same
underlying cognitive-control process differently.

**Implication:** this is a strong argument for the course's existing decision to use a **closed
list** of five regulation types rather than importing a full theoretical model wholesale, and for
banning the word "metacognition" itself in student-facing material. If the research community
hasn't converged on stable terminology, introductory students shouldn't be handed an unstable or
jargon-heavy vocabulary either. The course's five-type taxonomy (planning, process monitoring,
comprehension monitoring, reflection on cognition, self-explanation) is closest to the
Loksa & Ko (2016) empirical coding scheme, which has the advantage of being validated directly
against programming problem-solving transcripts rather than adapted from a general education
theory.

## 8. Verbal self-report is a noisy signal — a reason to require concrete, checkable answers

The ICER paper is explicit about a limitation directly relevant to grading design: think-aloud
and self-report data are inherently noisy, vary with a participant's comfort thinking aloud, and
can miss cognitive activity that happens too fast or too automatically to verbalize. Their own
statistical models had modest explanatory power (R² of 0.43–0.66) even with a controlled lab
setting and trained coders reaching only 83–88% inter-rater agreement.

**Implication:** self-report (i.e., a student's written reflection) is inherently an imperfect
window into what they actually did. This supports the course's existing grading protocol
requirement that graders verify every claimed artifact against the submitted code rather than
trusting the reflection at face value — the research suggests that even well-designed self-report
prompts will contain some gap between what a student says they did and what they actually did,
so verification against code isn't optional rigor, it's a necessary correction for a known
weakness in the data source.

## 9. Decomposition is not one move — it's an iterative process with an axis-selection step and an evaluation step, neither of which this course's prompts currently ask about

Rich, Egan, & Ellsworth (2019) reviewed nine widely-used measures of computational thinking and
found that nearly all of them either don't measure decomposition at all, or reduce it to counting
how many pieces ("blocks") a student's solution was split into — which reveals nothing about *how*
the student decided where to split, or whether the split actually helped. To fix this, the authors
built a decompositional framework from case studies across STEM and non-STEM fields (engineering,
ethnography, philosophy, product design). Three findings matter here:

- **Decomposition has two distinct forms that are usually conflated.** *Substantive* decomposition
  is breaking a problem into its component parts along a chosen **axis** (e.g., splitting a queue
  class into "storage" and "add/remove operations"). *Relational* decomposition is identifying how
  those parts relate to each other — by sequence, dependence, location, or function (e.g.,
  recognizing that "add" and "retrieve" in a queue must preserve first-in-first-out order). Most
  measures, and most instruction, only ever ask about the first.
- **Decomposition is a five-step iterative cycle, not a single action taken once at the start:**
  (1) identify a candidate axis to split along, (2) proactively evaluate whether that axis would
  add useful understanding before committing to it, (3) accept or reject the axis — reject sends
  the student back to step 1 with a new candidate, (4) execute the split using the accepted axis,
  (5) **retroactively evaluate** whether the resulting decomposition actually helped solve the
  problem. Critically, the authors stress this is not linear: expert problem-solvers re-decompose
  at multiple points, including *during* debugging — not only before writing any code.
- **Axis selection is a real decision, not a mechanical step.** Two people can substantively
  decompose the same problem differently depending on what axis they choose (physical parts vs.
  function vs. time-sequence vs. dependency), and the paper's engineering source material notes
  that functional decomposition is especially useful "when there is no established concept or
  preconceived structure" — exactly the situation a novice programmer is in on an unfamiliar
  problem.

**Implication:** this is the most direct evidence yet that a single "list your sub-tasks before
coding" prompt — which is currently the only decomposition-adjacent prompt in this course's
template, and it only fires for units 3–6 — captures at most step 4 (execute) of a five-step
process, and only the substantive half of decomposition at that. It does not ask *why* the student
split the problem the way they did (axis selection/evaluation, steps 1–3), whether they considered
how the parts relate to each other (relational decomposition — sequence, dependence, function), or
whether the split they chose actually turned out to help (retroactive evaluation, step 5). See the
assessment against `reflection-prompts.docx` below.

---

## Summary table: research finding → existing course rule it supports

| Finding | Course rule it grounds |
|---|---|
| Explicit stage instruction, not just prompting, drives gains | Vocabulary must be taught before a prompt uses it; band prompts by unit |
| Six-stage model validated empirically | Existing Stage 1–6 taxonomy in `CLAUDE.md` |
| Comprehension monitoring/planning linked to fewer errors | Quota: comprehension monitoring or planning ≥ 4 |
| Self-explanation not linked to fewer errors, sometimes more | Quota: self-explanation ≤ 1 |
| Self-regulation needs prior knowledge to be effective | Bands: concrete (1–2) → structural (3–6) → strategic (7–10) |
| Concrete, problem-specific scaffolding outperforms generic reflection | Checklist rule 2 & 4: name a specific artifact, unanswerable without this problem |
| Novices skip reinterpretation and evaluation unless prompted | Required Stage-1 pre-coding prompt; required post-coding plan comparison |
| Field-wide terminology inconsistency | Closed five-type regulation list; no jargon in student-facing text |
| Self-report is a noisy, incomplete signal | Grading protocol: verify every claim against the submitted code |
| Decomposition is a 5-step cycle (axis, evaluate, accept/reject, execute, retroactively evaluate), not one action | **Gap — not currently supported. See assessment below.** |

---

## Does `reflection-prompts.docx` support the Rich et al. decomposition process?

**No, not meaningfully.** The current template (as of this summary) covers at most one of the five
steps, and only for some units. Checked against each step:

| Rich et al. step | Present in `reflection-prompts.docx`? |
|---|---|
| 1. Identify an axis | **No.** No prompt asks what basis the student is splitting the problem along (by function, by sequence, by data, by physical part, etc.). |
| 2. Proactively evaluate the axis | **No.** No prompt asks the student to weigh a candidate split before committing to it. |
| 3. Accept/reject the axis | **No.** There is no prompt inviting the student to consider and discard an alternative breakdown. |
| 4. Execute the decomposition | **Partial, and unit-gated.** Pre-Coding prompt 3's structural-band variant ("What sub-tasks or functions will you write across this assignment...") asks for the *result* of a substantive decomposition, but only for Units 3–6. Units 1–2 and 7–10 get a different prompt 3 (a case almost overlooked; an anticipated failure) that isn't about decomposition at all. |
| 5. Retroactively evaluate the decomposition | **No.** Post-Coding's three prompts (which exercise was hardest, where the approach broke down, which assumption was wrong) ask about difficulty and correctness, not about whether the way the student split the problem into parts was the right split. A student could answer all three fully without ever revisiting how they broke the problem down. |

Two gaps stand out as the most consequential, beyond simple step-coverage:

- **Relational decomposition is entirely absent.** Even the one prompt that touches decomposition
  (Pre-Coding 3, structural band) only asks for a list of sub-tasks or functions — it never asks
  how those parts relate: which ones depend on which, what order they must run in, or what each
  one is *for*. Per Rich et al., this is half of what decomposition means; the current template
  only ever asks about the other half.
- **Decomposition quality is never checked against the finished product.** Rich et al.'s step 5 is
  explicitly about evaluating whether a decomposition helped — this course dropped its closest
  equivalent (comparing finished code to a "pre-coding plan") because no prompt produced a real
  plan artifact to compare against (see finding 6 above). That was the right call given the old
  prompt's design, but it means decomposition quality currently has *no* retrospective check
  anywhere in the template, structural-band units included.

This is a description of the current gap, not a fix — `CLAUDE.md`'s "no function-decomposition
prompts before unit 3" rule and the course's ban on the word "decomposition" in student-facing
text both still apply to any future prompt design addressing it, and unit banding would need to
determine how much of axis-selection/evaluation (steps 1–3) is answerable by students who haven't
yet been taught what a function boundary is.
