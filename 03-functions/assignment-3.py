'''
COMP 4006

Assignment 3 - Functions & Variable Scope

Student Name:
Date Submitted:
Time Spent (approx.):

General Homework Guidelines:
- This assignment is submitted as ONE .zip archive, not a single .py file. See "What you
  submit" below -- read it before you start, because it changes how you organize your work.
- Rename this file to hw3_firstname_lastname.py -- your own first and last name, lower case,
  separated by underscores (e.g. hw3_ada_lovelace.py).
- Only use the methods and language features listed below.
  Methods: print(), input(), type(), int(), float(), str(), bool(), round(), .format(),
  dir(), id(), help(), range(), len(), enumerate(), isinstance(), sum(), locals(),
  globals(), .lower(), main().
  Language features: f-strings, arithmetic and comparison operators, and/or/not, True/False,
  if/elif/else, for...in, while, break, continue, in/not in, is/is not, def, return,
  parameters and arguments, default parameter values, keyword arguments, None, docstrings,
  type hints, global, local vs. global scope, import, __name__ and '__main__',
  a function held in a variable (a name with no parentheses is the function itself).
  Lists, tuples, dictionaries, and sets are NOT part of this assignment -- they begin in
  week 4. This is why no function here returns two values: "return a, b" builds a tuple.
  If an exercise seems to need two results, it needs two functions.
  *args and **kwargs are NOT part of this assignment. Python does have a way to accept an
  unknown number of arguments, and that is what it is called -- but what it hands your
  function is a tuple or a dictionary, so it waits for weeks 4 and 6.
- EVERY function you write needs a docstring as the first statement in its body, giving:
  one or two lines on what the function does; an "Args:" section naming each parameter, its
  type, and what it is for; and a "Returns:" section giving the returned type and what it is.
- EVERY function you write returns a value. A function that only prints has returned None.
  Unless an exercise asks you to print, returning is the requirement.
- Put your function calls beneath the definitions, under a "# --- calls ---" marker, or
  inside main() where the exercise asks for one. Do not scatter calls between definitions.
- Follow PEP 8: snake_case for names, ALL_CAPS for constants, four-space indentation,
  spaces around operators, and descriptive names (e.g. sample_count, not n).
- Comments explain WHY, not what. The docstring says what the function does; comments inside
  the body explain your reasoning.
- Test your code with every input value named in an exercise's requirements before
  submitting, and leave the output of your final run(s) in place.
- Print all output with a label that identifies the exercise (e.g. "Exercise 3:") so the
  grader can match your output to the requirement without guessing.
- No exercise asks the user for input while it runs. Every exercise sets its values in
  variables or passes them as arguments, so the grader can run this file straight through.

WHAT YOU SUBMIT

Two .py files, together in one .zip archive named hw3_firstname_lastname.zip:

    hw3_firstname_lastname.zip
        hw3_firstname_lastname.py     <- this file: Exercises 1-5, and part of Exercise 6
        storage_helpers.py            <- you create this: Exercise 6's two helpers only

Both files sit directly inside the archive. Do not put them in a folder inside the zip.

storage_helpers.py must be named EXACTLY that. Everyone in the class uses the same module
name, so the import line is the same in every submission. Do not rename it after yourself.

Use an underscore, not a hyphen. This is not a style preference: a module name containing a
hyphen CANNOT be imported. "import storage-helpers" is a syntax error, and Python reads the
hyphen as a minus sign. This is the first time in this course that how you name a file
changes whether your code runs at all.

Check before you submit: unzip your archive somewhere else and run the primary file. If the
import fails, NOTHING in the file runs -- not even Exercises 1 through 5, however correct
they are -- and that is graded as a submission that does not run. It costs you Correctness
points on Exercise 6 and caps your reflective responses at 10 out of 20. Two minutes of
checking protects a large number of points.

The .docx with your reflective prompts and responses is uploaded to Canvas separately,
alongside the .zip. Do not put it inside the archive.

Total points for this file: 80, made up of two parts.
- 70 points are spread across the six exercises below, using the point value shown on each.
- 10 points are scored once, on the submission as a whole: whether every exercise is present,
  whether both files are present and correctly named, and whether the file follows the
  instructions in this header. Those 10 points are the easiest in the assignment to keep and
  the easiest to lose by not reading.

The requirements printed above each exercise are complete -- everything you need to do the
assignment is in this file. See code-rubric.docx for how each exercise's points are awarded.

Several exercises ask for a short written response (an explanation, a comparison, a
justification) in addition to code. Write these directly into this file as comments, in the
location indicated for each exercise -- they are graded as part of that exercise's points.

This file does NOT include the reflective prompts. Those are a separate 20-point component:
answer them in a .docx file and upload it to Canvas alongside this .zip.
'''

# Exercise 3 needs this. Imports go at the top of a file, above everything else.


#############################################################################
# Exercise 1 -- Accuracy Reporter (8 pts)
#############################################################################

# Scenario: A model evaluation script reports accuracy as a percentage. The
# same conversion is needed in three different places in the pipeline, so it
# belongs in a function rather than being retyped.
#
# Topics: def, one positional parameter, return vs. print, docstrings.
#
# Requirements:
# 1. Write a function accuracy_as_percentage that takes one parameter, a
#    proportion between 0.0 and 1.0, and RETURNS that value as a percentage
#    rounded to one decimal place. It must not print anything.
# 2. Give it a docstring in the format described in this file's header.
# 3. Call it with 0.9437 and assign the result to a variable. Print that
#    variable with a label, using an f-string.
# 4. Write a second function, show_accuracy, that takes the same parameter and
#    PRINTS the percentage instead of returning it. Call it, assign its result
#    to a variable, and print that variable too.
# 5. In the trailing comment below, state what that second variable holds and
#    why, and say which of the two functions could be used inside another
#    calculation.


# --- calls ---


# --- Trailing comment (what the second variable holds, and why) ---


#############################################################################
# Exercise 2 -- Sample Window Total (10 pts)
#############################################################################

# Scenario: A quality check totals the sample identifiers in a contiguous
# window of a dataset, to confirm no records were dropped during transfer. The
# window's start and end move between runs.
#
# Topics: several positional parameters, argument order at the call site, a
# loop inside a function, sum() against a hand-written accumulator.
#
# Requirements:
# 1. Write a function window_total_loop taking two parameters, first_id and
#    last_id, that uses a for loop and an accumulator to total every integer
#    from first_id to last_id INCLUSIVE, and returns the total.
# 2. Write a second function window_total_sum with the same two parameters that
#    returns the same total using sum() and a range(), with no loop of your own.
# 3. Give both functions docstrings.
# 4. Call both with first_id = 1 and last_id = 60, print both results with
#    labels, and print whether the two results are equal.
# 5. Call window_total_loop again with the arguments reversed -- 60 then 1 --
#    and print what it returns.
# 6. In the trailing comment below, state what the reversed call returned and
#    why no error was raised, and say which of the two functions you would keep
#    if you could keep only one, and why.


# --- calls ---


# --- Trailing comment (the reversed call, and which function you would keep) ---


#############################################################################
# Exercise 3 -- Signal Distance (12 pts)
#############################################################################

# Scenario: A sensor array reports how far a detected signal lies from the
# array's origin. Most readings are two-dimensional, but the calculation must
# still work when only one axis is supplied.
#
# Topics: default parameter values, type hints, import math, isinstance() as a
# guard.
#
# Requirements:
# 1. Add "import math" at the TOP of this file, in the space marked above
#    Exercise 1.
# 2. Write a function signal_distance with a required parameter x_offset and a
#    second parameter y_offset that DEFAULTS to 0.0. It returns the
#    straight-line distance from the origin, rounded to two decimal places.
# 3. Include type hints on both parameters and on the return value. Use one
#    plain type per hint.
# 4. Compute the distance with math.sqrt().
# 5. Call the function three ways, printing each result with a label:
#      - with both arguments: 3.0 and 4.0        (expect 5.0)
#      - with only x_offset: 12.5                (expect 12.5)
#      - with both again, using values of your choice
#    Do not use 5.0 for the single-argument call. A one-axis distance is just
#    the offset itself, so signal_distance(5.0) also returns 5.0 -- the same
#    number as the call above it, which would make the two lines impossible to
#    tell apart in your output.
# 6. Add a guard at the START of the function: use isinstance() to check that
#    x_offset is a float or an int, and return -1.0 if it is not. Call the
#    function once with a string argument to show the guard working.
# 7. In the trailing comment below, state what the type hints do and do not do,
#    using your result from requirement 6 as the evidence.


# --- calls ---


# --- Trailing comment (what type hints do and do not do) ---


#############################################################################
# Exercise 4 -- Report Header Generator (12 pts)
#############################################################################

# Scenario: An analytics tool prints a header at the top of every generated
# report. Most reports use the same defaults, but any field can be overridden
# when a caller needs to.
#
# Topics: default parameter values, keyword arguments, calling one function
# several ways, .format() vs. f-strings.
#
# Requirements:
# 1. Write a function build_report_header with four parameters: title
#    (required), author (defaults to "Anonymous"), report_date (defaults to
#    "Today"), and format_style (defaults to "Standard").
# 2. It RETURNS a single string containing all four fields, each on its own
#    line, in the form:
#      Report: <title>
#      Author: <author>
#      Date: <report_date>
#      Format: <format_style>
#    It must not print.
# 3. Build that string with .format(), not an f-string. Both were taught in
#    week 1; this exercise asks for the one students use less.
# 4. Call the function four times and print each result with a label:
#      - with only the required argument
#      - with some optional values as positional arguments
#      - with optional values as keyword arguments
#      - with the same keyword arguments in a different order from the
#        parameter list
# 5. Print a separator line of forty "=" characters beneath each header,
#    without typing forty characters.
# 6. In the trailing comment below, state whether calls 3 and 4 produced
#    identical output, and explain why the parameter order in the definition
#    did or did not matter.


# --- calls ---


# --- Trailing comment (calls 3 and 4, and parameter order) ---


#############################################################################
# Exercise 5 -- Alert Counter Scope (10 pts)
#############################################################################

# Scenario: A monitoring script keeps a running count of alerts raised during a
# shift. Two functions both claim to update it, but only one of them changes
# what the rest of the program sees.
#
# Topics: local scope, global scope, the global keyword, NameError.
#
# Requirements:
# 1. Create a global variable alert_count with the value 10.
# 2. Write a function count_local_alerts that creates its OWN local variable
#    named alert_count with the value 1, adds 5 to it, prints the local value,
#    and returns it.
# 3. Call it, store the returned value in local_result, then print the global
#    alert_count.
# 4. Write a second function count_global_alerts that uses the global keyword
#    to reach the global alert_count, adds 3 to it, prints the new value, and
#    returns it.
# 5. Call it, store the returned value in global_result, then print the global
#    alert_count again.
# 6. Add a third function show_shift_label that assigns a local variable
#    shift_label and returns it. After calling it, try to print shift_label at
#    the top level of this file. Run it, read the error, then comment that line
#    out and write the exact error name in a comment beside it.
# 7. In the multi-line comment below, compare the two counting functions: state
#    the value of the global alert_count after each call, explain the
#    difference, and say why global is generally avoided even though it works
#    here.


# --- calls ---


'''
--- Written response (comparing the two counting functions) ---


'''


#############################################################################
# Exercise 6 -- Storage Unit Converter (18 pts)
#############################################################################

# Scenario: A capacity-planning tool reports storage figures in whichever unit
# the reader expects. The conversion arithmetic is small and reusable, so it
# lives in its own module that the reporting script imports.
#
# Topics: helper functions, one function calling another, importing a module
# you wrote, __name__ and the if __name__ == '__main__': guard, main() as an
# orchestrator, .lower().
#
# THIS EXERCISE SPANS TWO FILES. Re-read "What you submit" in the header.
#
# Requirements -- in storage_helpers.py (a NEW file you create):
# 1. Write _megabytes_to_gigabytes, taking a size in megabytes and returning it
#    in gigabytes, rounded to three decimal places. Use 1024 megabytes to the
#    gigabyte.
# 2. Write _gigabytes_to_megabytes, taking a size in gigabytes and returning it
#    in megabytes, rounded to three decimal places.
# 3. Give both docstrings.
# 4. Add an if __name__ == '__main__': block that calls each helper once and
#    prints the result, so you can test the module on its own.
#
# Requirements -- in this file:
# 5. Import the module with "import storage_helpers", at the top of this file
#    with the other import.
# 6. Write convert_storage taking two parameters, size and current_unit. Using
#    .lower() so that "MB", "mb" and "Mb" are all accepted, use an
#    if / elif / else chain to ASSIGN THE CORRECT HELPER TO A VARIABLE, then
#    call that variable ONCE on the last line to RETURN the converted value.
#    Write the helper's name with NO parentheses when you assign it:
#        converter = storage_helpers._megabytes_to_gigabytes   # no ()
#        ...
#        return converter(size)                                # called here
# 7. If current_unit is neither megabytes nor gigabytes, return -1.0.
# 8. Write a function main that calls convert_storage at least three times --
#    once megabytes to gigabytes, once gigabytes to megabytes, and once with an
#    unrecognised unit -- and prints each result with a label naming the input
#    value, the input unit, and the output unit.
# 9. Call main() on the LAST line of this file, inside an
#    if __name__ == '__main__': block.
# 10. Verify with 2048 megabytes (expect 2.0 gigabytes) and 1.5 gigabytes
#     (expect 1536.0 megabytes). Leave the output of your final run in place.
# 11. In the trailing comment below, state what __name__ holds when you run
#     storage_helpers.py directly and what it holds when this file imports it,
#     and say what would appear in your output if the guard were removed from
#     storage_helpers.py.
# 12. Print the chosen helper's NAME on its own, without parentheses, once -- so
#     you can see what a function looks like when it is not being called. In the
#     trailing comment, say in one sentence what the difference is between
#     writing converter and writing converter(size).


# --- Trailing comment (__name__, the guard, and converter vs converter(size)) ---


# --- main() call goes here, on the last line of the file ---
