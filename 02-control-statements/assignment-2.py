'''
COMP 4006

Assignment 2 - Control Statements

Student Name:
Date Submitted:
Time Spent (approx.):

General Homework Guidelines:
- Submit two files to Canvas: this completed .py file, and a separate .docx file containing
  the reflective prompts and your responses. Do not submit .ipynb files.
- Rename this file before submitting, to hw2_firstname_lastname.py -- your own first and
  last name, lower case, separated by underscores (e.g. hw2_ada_lovelace.py). An assignment
  that asks for several files is submitted as one .zip named the same way, ending .zip
  instead of .py.
- Only use the methods and language features listed below.
  Methods: print(), input(), type(), int(), float(), str(), bool(), round(), .format(),
  dir(), id(), help(), range(), len(), enumerate(), isinstance().
  Language features: f-strings, arithmetic and comparison operators, and/or/not, True/False,
  if/elif/else, for...in, while, break, continue, in/not in, is/is not.
  Lists, tuples, dictionaries, and sets are NOT part of this assignment -- they begin in week 4.
  Functions are NOT part of this assignment -- they begin in week 3. You will repeat some
  patterns across exercises, and that is expected this week.
- Use inline and/or multiline comments to explain what your code is doing, and to answer
  any question that asks for a written response.
- Follow PEP 8: snake_case for variables, ALL_CAPS for constants, four-space indentation,
  spaces around operators, and descriptive variable names (e.g. failed_attempts, not x).
- Test your code with every input value named in an exercise's requirements before submitting,
  and leave the output of your final run(s) in place.
- Print all output with a label that identifies the exercise (e.g. "Exercise 3:") so the
  grader can match your output to the requirement without guessing.
- Only Exercise 2 asks the user for input while it runs. Every other exercise sets its values
  in variables at the top, so the grader can run this file straight through.

Total points for this file: 80, made up of two parts.
- 70 points are spread across the seven exercises below, using the point value shown on each.
- 10 points are scored once, on the submission as a whole: whether every exercise is present
  and the file follows the instructions in this header. Those 10 points are the easiest in the
  assignment to keep and the easiest to lose by not reading.

The requirements printed above each exercise are complete -- everything you need to do the
assignment is in this file. See code-rubric.docx for how each exercise's points are awarded.

Several exercises ask for a short written response (an explanation, a count, a justification)
in addition to code. Write these directly into this file as comments, in the location indicated
for each exercise -- they are graded as part of that exercise's points.

This file does NOT include the reflective prompts. Those are a separate 20-point component:
answer them in a .docx file and upload it to Canvas alongside this .py file.
'''

#############################################################################
# Exercise 1 -- Threat Level Triage (7 pts)
#############################################################################

# Scenario: A security dashboard assigns each detected event a threat score
# from 0 to 100 and must label it Critical, High, Medium, or Low so an
# analyst knows what to open first.
#
# Topics: if / elif / else, comparison operators, branch ordering.
#
# Requirements:
# 1. Assign a variable threat_score an integer value.
# 2. Using a single if / elif / else chain, print exactly one label:
#      90 and above -> Critical
#      70 to 89     -> High
#      40 to 69     -> Medium
#      below 40     -> Low
# 3. Verify with threat_score values 95, 70, 39, and 0.
# 4. Also assign a boolean variable alert_suppressed. Using the compound
#    boolean logic from week 1, compute and print is_actionable -- true when
#    the score is 70 or above AND the alert is not suppressed. This is a
#    single boolean value, not a branch. The chain above answers "which
#    label"; this answers "should anyone act".
# 5. In a trailing comment, state what would print for a score of 95 if the
#    >= 40 test came first, and why.


# --- Verification notes (95, 70, 39, 0 all tested) ---


# --- Trailing comment (branch ordering explanation) ---


#############################################################################
# Exercise 2 -- Failed Login Monitor (10 pts)
#############################################################################

# Scenario: An authentication service locks an account after three
# consecutive failed passcode entries. You are writing the entry loop.
#
# Topics: while, break, counters, input(), int() casting, loop termination.
#
# Requirements:
# 1. Set a constant CORRECT_PASSCODE to an integer of your choice, and a
#    constant MAX_ATTEMPTS to 3.
# 2. Using a while loop, prompt the user with input() for a passcode and
#    cast it to int.
# 3. If the entry matches, print "Access granted." and leave the loop with
#    break.
# 4. If it does not match, increment a counter and print how many attempts
#    remain.
# 5. When the counter reaches MAX_ATTEMPTS, print "Account locked." and stop.
# 6. In a trailing comment, paste the console output of two sample runs: one
#    where access is granted on the second attempt, and one that reaches
#    lockout.


# --- Sample run 1 (granted on second attempt) ---


# --- Sample run 2 (reaches lockout) ---


#############################################################################
# Exercise 3 -- Sensor Sweep with Skipped Readings (10 pts)
#############################################################################

# Scenario: A monitoring station takes one reading per minute across a
# 60-minute window. The sensor recalibrates every 7th minute and reports
# nothing usable then, so those readings must be skipped before the average
# is computed.
#
# Topics: for with range(), continue, accumulator and counter patterns,
# %, round().
#
# Requirements:
# 1. Loop over minutes 1 through 60 inclusive using range().
# 2. File input arrives in week 7 -- for now, generate each reading inside
#    the loop as:  reading = 20 + (minute % 5)
# 3. Skip any minute where minute % 7 == 0, using continue.
# 4. Accumulate the total of the kept readings and count how many were kept.
# 5. After the loop, print the number kept, the number skipped, and the
#    average of the kept readings rounded to two decimal places with
#    round().
# 6. Print that summary line using .format() rather than an f-string. Both
#    were taught in week 1 and both produce the same output; this exercise
#    asks for the one you use less.
# 7. In a trailing comment, state how many readings were skipped and why
#    that number is what it is.


# --- Trailing comment (skipped count and why) ---


#############################################################################
# Exercise 4 -- Passcode Strength Check (12 pts)
#############################################################################

# Scenario: Before a credential is accepted, a policy engine checks it for
# length and for the presence of at least one digit, then reports a single
# verdict.
#
# Topics: len(), enumerate(), membership (in), counters, for over a string,
# combining boolean results.
#
# Requirements:
# 1. Assign a variable passcode a string value.
# 2. Before examining it, use isinstance() to confirm passcode is a str, and
#    print a short message saying so. Week 1 used type() to ask what
#    something is; isinstance() asks whether it IS a given type, which is
#    the form a guard needs.
# 3. Using enumerate() over passcode, count how many characters are digits.
#    A character is a digit if it is a member of "0123456789".
# 4. Report the position of the first digit found, using the index that
#    enumerate() provides. If there is no digit, say so.
# 5. After the loop, print "Strong" only if the passcode is at least 12
#    characters long AND contains at least one digit; print "Weak"
#    otherwise. Use len() for the length test.
# 6. Verify with at least three values: one strong, one long but with no
#    digit, and one short but containing a digit.


# --- Verification notes (three passcode values tested) ---


#############################################################################
# Exercise 5 -- Floating-Point Accumulation (9 pts)
#############################################################################

# Scenario: A billing pipeline adds a 0.1-unit charge ten times and asserts
# the total equals 1.0. The assertion fails in production and nobody can
# see why.
#
# Topics: for with range(), float accumulation, == on floats, round(),
# integer arithmetic as a workaround.
#
# Requirements:
# 1. Using a for loop over range(), add 0.1 to an accumulator ten times.
# 2. Print the accumulated total without rounding, so the discrepancy is
#    visible.
# 3. Print the result of comparing the total to 1.0 with ==.
# 4. Repeat the accumulation using integers only -- add 1 ten times, then
#    divide by 10 at the end -- and print that result and its == comparison
#    to 1.0.
# 5. Using round() from week 1, print the result of comparing the FLOAT
#    total to 1.0 rounded to two decimal places. You now have three
#    results: one wrong, one right, and one right for a different reason.
# 6. In a trailing comment, state in one or two sentences why the first
#    comparison fails and the second does not, and whether round() fixed
#    the problem or hid it.


# --- Trailing comment (why the comparisons differ) ---


#############################################################################
# Exercise 6 -- Log Retention Countdown (9 pts)
#############################################################################

# Scenario: A retention policy prints a daily warning as an archive
# approaches its purge date. The message must read correctly on the last
# day, when there is one day left rather than several.
#
# Topics: for with a descending range(), if / else for singular and plural,
# f-strings, loop boundaries.
#
# Requirements:
# 1. Assign a variable days_remaining an integer value of 5.
# 2. Count down from days_remaining to 0 inclusive using a for loop with a
#    descending range().
# 3. For each day above 0, print a warning using an f-string, choosing
#    "day" or "days" correctly:
#      5 days remaining before purge.
#      ...
#      1 day remaining before purge.
# 4. When the count reaches 0, print "Archive purged." instead of a warning.
# 5. Verify with days_remaining set to 5 and again to 1.


# --- Verification notes (5 and 1 both tested) ---


#############################################################################
# Exercise 7 -- Packet Fit (13 pts)
#############################################################################

# Scenario: A transfer must be split into packets of exactly two permitted
# sizes, with no remainder and no partial packet. Before starting, the
# system reports whether the payload can be divided exactly.
#
# Topics: nested for loops with range(), boolean flag, break, integer
# arithmetic, exhaustive search.
#
# Requirements:
# 1. Assign three integer variables: payload_size, small_packet, and
#    large_packet.
# 2. Using nested for loops over range(), search for a count of small
#    packets and a count of large packets whose sizes total exactly
#    payload_size.
# 3. Use a boolean flag to record whether a combination was found. Use
#    break to stop searching once one is.
# 4. After the search, print "possible" together with the two counts that
#    worked, or "impossible" if none did.
# 5. Verify with 9, 2, 3 (possible) and 5, 2, 4 (impossible).
# 6. In a trailing comment, state why the "impossible" decision cannot be
#    made inside the loop.


# --- Verification notes (9,2,3 and 5,2,4 both tested) ---


# --- Trailing comment (why "impossible" waits until the search ends) ---
