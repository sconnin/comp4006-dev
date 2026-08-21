'''
COMP 4006

Assignment 1 - Variables & Boolean Expressions

Student Name:
Date Submitted:
Time Spent (approx.):

General Homework Guidelines:
- Submit two files to Canvas: this completed .py file, and a separate .docx file containing
  the reflective prompts and your responses. Do not submit .ipynb files.
- Rename this file before submitting, to hw1_firstname_lastname.py -- your own first and
  last name, lower case, separated by underscores (e.g. hw1_ada_lovelace.py). An assignment
  that asks for several files is submitted as one .zip named the same way, ending .zip
  instead of .py.
- Only use what is listed in this assignment's methods-allowed.md effective set.
  Methods: print(), input(), type(), int(), float(), str(), bool(), round(), .format(),
  dir(), id(), help().
  Language features: f-strings, arithmetic and comparison operators, and/or/not, True/False.
  Control flow (if, for, while) is not part of this assignment -- it is introduced next week.
- Use inline and/or multiline comments to explain what your code is doing, and to answer
  any question that asks for a written response.
- Follow PEP 8: snake_case for variables, ALL_CAPS for constants, spaces around operators,
  and descriptive variable names (e.g. session_seconds, not x).
- Test your code with every input value named in an exercise's requirements before submitting,
  and leave the output of your final run(s) in place.
- Print all output with a label that identifies the exercise and item (e.g. "Exercise 2, Item B:")
  so the grader can match your output to the requirement without guessing.
- Where an exercise asks for a "hand-calculated" value, work it out yourself using reasoning
  only -- on paper, in your head, or in a comment -- before running any code or using Python
  (including a calculator app) to check it. Write that value down first, then run your code and
  compare. The point is to test your own understanding, not to transcribe an answer Python
  already gave you.

Total points for this file: 80, made up of two parts.
- 70 points are spread across the seven exercises below, using the point value shown on each.
- 10 points are scored once, on the submission as a whole: whether every exercise is present and
  the file follows the instructions in this header. Those 10 points are the easiest in the
  assignment to keep and the easiest to lose by not reading.

The requirements printed above each exercise are complete -- everything you need to do the
assignment is in this file. See code-rubric.docx for how each exercise's points are awarded.

Several exercises ask for a short written response (e.g. a hand-calculated value, an
explanation, a justification) in addition to code. Write these directly into this file as
comments, in the location indicated for each exercise -- they are graded as part of that
exercise's points.

This file does NOT include the reflective prompts. Those are a separate 20-point component:
answer them in a .docx file and upload it to Canvas alongside this .py file.
'''

#############################################################################
# Exercise 1 -- Verifying Arithmetic Expressions (7 pts)
#############################################################################

# Scenario: A monitoring script computes a derived metric from raw sensor
# readings. Before trusting the script, you hand-verify two of its
# expressions, then confirm your hand-calculation in code.
#
# Topics: arithmetic operators, operator precedence, int/float type, type()
#
# Requirements:
# 1. For each expression below, first write a one-line comment stating your
#    hand-calculated value and type.
#    A) 5 + 3 / 5 * (4 - 10)
#    B) 17 // 3 ** 4
# 2. Assign each expression to a variable, then print the variable's value
#    and its type().
# 3. In a trailing comment, state whether the printed result matched your
#    hand-calculation.

# --- Item A ---
# Hand-calculated value/type:


# --- Item B ---
# Hand-calculated value/type:


#############################################################################
# Exercise 2 -- Access-Control Conditions (7 pts)
#############################################################################

# Scenario: A login system grants access based on three security flags:
# whether multi-factor authentication (MFA) is enabled, whether the
# connection is over a trusted VPN, and whether the account is flagged as
# compromised.
#
# Topics: boolean literals, relational operators, logical operators
# (not, and, or) and their precedence.
#
# Requirements:
# 1. Initialize three boolean variables: mfa_enabled, vpn_connected,
#    account_flagged, set to values of your choice.
# 2. Write and print the result of each of the following, computed from
#    your variables (not hard-coded booleans):
#    A) mfa_enabled and not account_flagged
#    B) vpn_connected or account_flagged
#    C) not vpn_connected == account_flagged
#    D) mfa_enabled and not account_flagged or vpn_connected
# 3. In a trailing comment, identify which one of A-D would most easily be
#    misread if a reader ignored operator precedence, and state the correct
#    evaluation order in words.

# --- Trailing comment (precedence explanation) ---


#############################################################################
# Exercise 3 -- Fixing Invalid Identifiers (5 pts)
#############################################################################

# Scenario: A teammate's draft script uses variable names that won't run.
# You are cleaning it up before deployment.
#
# Topics: valid identifier rules, naming conventions (snake_case,
# ALL_CAPS constants).
#
# Requirements:
# 1. For each proposed name below, write one short comment stating whether
#    it is valid Python syntax, and if not, exactly which rule it breaks:
#    speed Of Light, x_2, 3Attempts, vertical-distance, B5V
# 2. For each invalid name, write a corrected version following this
#    course's naming conventions, assign it a value, and print it.
# 3. For "speed Of Light", correct it as a constant (it does not change
#    during the program) and follow the constant-naming convention.

# --- Validity notes ---


# --- Corrected variables ---


#############################################################################
# Exercise 4 -- Data Sample Grid (10 pts)
#############################################################################

# Scenario: A dataset is stored as a square grid of pixels (e.g., a
# thumbnail image). You need to report the grid's perimeter (total border
# cells) and area (total cells) for storage planning.
#
# Topics: variable initialization, arithmetic expressions, int, float,
# PEP 8 formatting.
#
# Requirements:
# 1. Initialize a variable side_length representing pixels per side of a
#    square image.
# 2. Compute and print the perimeter and area, each in a clearly labeled
#    line.
# 3. Run and verify your program with three different values of
#    side_length (e.g. 4, 10, 25), changing only the initial assignment
#    each time. Leave your final run's output in the submission.

# --- Verification notes (three side_length values tested) ---


#############################################################################
# Exercise 5 -- Session Duration Converter (13 pts)
#############################################################################

# Scenario: A security log records a user session length in seconds. For
# the incident report, you need it broken into hours, minutes, and
# seconds.
#
# Topics: integer (//) vs. true (/) division, modulo (%), integer
# arithmetic, avoiding floating-point rounding error.
#
# Requirements:
# 1. Assign a variable session_seconds an integer value.
# 2. Using only integer arithmetic (// and % -- no round() here), compute
#    hours, minutes, and seconds as three separate variables.
# 3. Print the result as "H hours, M minutes, S seconds".
# 4. Verify your program against two starting values: 300 (expect 0h 5m 0s)
#    and 4503 (expect 1h 15m 3s). Leave both verification runs' output, or
#    a comment noting both were checked, in your submission.

# --- Verification notes (300 and 4503 both tested) ---


#############################################################################
# Exercise 6 -- Model Deployment Eligibility Report (19 pts)
#############################################################################

# Scenario: Before a trained model can be deployed, it must pass automated
# checks: minimum accuracy, minimum validation sample size, and a
# data-integrity flag. You are writing the report generator a data science
# team will reuse for every candidate model.
#
# Topics: boolean expressions built from relational + logical operators,
# f-strings, variables that drive output so the report updates
# automatically when inputs change.
#
# Requirements:
# 1. Initialize variables for a candidate model: accuracy (float, e.g.
#    0.94), sample_size (int, e.g. 1200), data_verified (bool).
# 2. Compute and print, using f-strings referencing your variables (not
#    literal True/False text):
#    - Accuracy requirement (>= 0.90)
#    - Sample size requirement (> 1000)
#    - Data integrity requirement (data_verified must be True). The
#      `is` operator is not part of this assignment -- compare with ==,
#      or use the boolean variable on its own.
#    - Final eligibility: all three requirements must hold
# 3. Print a "Logic Explanation" section showing the substituted boolean
#    values step by step (e.g. "Final = True and True and True" then
#    "Final = True"), matching your actual computed values -- not
#    typed-out placeholders.
# 4. Change one input variable to a value that flips the final
#    eligibility, rerun, and leave both the original and modified report
#    output in your submission, each clearly labeled.

# --- Original run ---


# --- Modified run ---


#############################################################################
# Exercise 7 -- Analyst Registration Prompt (9 pts)
#############################################################################

# Scenario: A command-line tool asks a new analyst for their name and the
# number of records they plan to process, then confirms the entry back to
# them.
#
# Topics: input(), str/int type mismatch, explicit casting, f-strings.
#
# Requirements:
# 1. Prompt the user for their full name and store it in a variable.
# 2. Prompt the user for the number of records they plan to process (a
#    whole number) and store it, explicitly cast to int.
# 3. Print: "Hello <name>, you're registered to process <record count>
#    records." using an f-string.
# 4. In a trailing comment, state what error would occur if step 2's cast
#    were removed and the record count were concatenated with + instead
#    of an f-string.

# --- Trailing comment (error explanation) ---
