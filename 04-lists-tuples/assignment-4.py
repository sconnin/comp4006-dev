'''
COMP 4006

Assignment 4 - Lists & Tuples

Student Name:
Date Submitted:
Time Spent (approx.):

General Homework Guidelines:
- Submit two files to Canvas: this completed .py file, and a separate .docx file containing
  the reflective prompts and your responses. Do not submit .ipynb files.
  Note this is ONE .py file, not a .zip. Last week's assignment needed an archive because it
  spanned two files; this one does not.
- Rename this file before submitting, to hw4_firstname_lastname.py -- your own first and
  last name, lower case, separated by underscores (e.g. hw4_ada_lovelace.py).
- Only use the methods and language features listed below.
  Methods: print(), input(), type(), int(), float(), str(), bool(), round(), .format(),
  dir(), id(), help(), range(), len(), enumerate(), isinstance(), sum(), locals(),
  globals(), .lower(), main(), .append(), .clear(), .copy(), .count(), .extend(), .index(),
  .insert(), .pop(), .remove(), .reverse(), .sort(), list(), tuple(), min(), max(), zip(),
  sorted(), reversed(), any(), all().
  Language features: f-strings, arithmetic and comparison operators, and/or/not, True/False,
  if/elif/else, for...in, while, break, continue, in/not in, is/is not, def, return,
  parameters and arguments, default parameter values, keyword arguments, None, docstrings,
  type hints, global, local vs. global scope, import, __name__ and '__main__', list and
  tuple literals, indexing, negative indexing, slicing, nested indexing, index assignment,
  tuple unpacking, returning several values, *args in a function definition, concatenation
  and repetition, list comprehensions (the plain form and the if-filtered form).
- Strings methods other than .lower() are NOT part of this assignment -- they begin in
  week 5. Sets and dictionaries begin in weeks 5 and 6. There is no file reading this week,
  which is why the data in Exercise 6 is typed directly into this file; that is week 7.
- There is no del statement in this assignment. Remove items with .pop(), .remove() or
  .clear().
- *args IS part of this assignment, in a function definition (Exercise 6). Last week's file
  told you it was waiting for a week when you knew what a tuple was. This is that week.
  **kwargs still waits for week 6, because what it hands your function is a dictionary.
- EVERY function you write needs a docstring as the first statement in its body, giving:
  one or two lines on what the function does; an "Args:" section naming each parameter, its
  type, and what it is for; and a "Returns:" section giving the returned type and what it is.
- EVERY function you write returns a value. A function that only prints has returned None.
- A function that is GIVEN a list must not change that list unless the exercise says to.
  Build a new list and return it. Exercise 2 is where this idea is examined directly.
- Put your function calls beneath the definitions, under a "# --- calls ---" marker. Do not
  scatter calls between definitions.
- Follow PEP 8: snake_case for names, ALL_CAPS for constants, four-space indentation,
  spaces around operators, and descriptive names (asking_prices, not p).
- Comments explain WHY, not what. The docstring says what the function does; comments inside
  the body explain your reasoning.
- Test your code with every value named in an exercise's requirements before submitting, and
  leave the output of your final run in place.
- Print all output with a label that identifies the exercise (e.g. "Exercise 3:") so the
  grader can match your output to the requirement without guessing.
- No exercise asks the user for input while it runs. Every exercise sets its values in
  variables, so the grader can run this file straight through.

Total points for this file: 80, made up of two parts.
- 70 points are spread across the six exercises below, using the point value shown on each.
- 10 points are scored once, on the submission as a whole: whether every exercise is present
  and the file follows the instructions in this header. Those 10 points are the easiest in
  the assignment to keep and the easiest to lose by not reading.

The requirements printed above each exercise are complete -- everything you need to do the
assignment is in this file. See code-rubric.docx for how each exercise's points are awarded.

Several exercises ask for a short written response (an explanation, a comparison, a
justification) in addition to code. Write these directly into this file as comments, in the
location indicated for each exercise -- they are graded as part of that exercise's points.

This file does NOT include the reflective prompts. Those are a separate 20-point component:
answer them in a .docx file and upload it to Canvas alongside this .py file.
'''


#############################################################################
# Exercise 1 -- Asking Price Index (8 pts)
#############################################################################

# Scenario: A property analyst has a run of asking prices in the order they
# were listed. Before computing anything, they need to pull specific positions
# out of the run and check they are reading the right ones.
#
# Topics: list literals, indexing, negative indexing, slicing, len().
#
# Requirements:
# 1. Create a list named asking_prices holding, in this order:
#    475000, 595000, 500000, 445000, 329000, 399000, 1050000, 485000
# 2. Print the first price using an index, and the last price using a NEGATIVE
#    index. Do not use len() to reach the last one.
# 3. Print len(asking_prices), then print the largest index that is valid for
#    this list. Work that second number out yourself; do not type 7.
# 4. Print the slice asking_prices[2:5], then print how many items it contains.
# 5. Print the first three prices and the last three prices, each using a slice
#    with one bound left out.
# 6. In the trailing comment below, state what asking_prices[8] would do and
#    name the exception by its exact class name. Do NOT put that line in your
#    code -- describe it.


# --- calls ---


# --- Trailing comment (what asking_prices[8] would do) ---


#############################################################################
# Exercise 2 -- Watchlist Edits (10 pts)
#############################################################################

# Scenario: An analyst keeps a watchlist of asking prices and edits it as
# listings come and go. A colleague is given "the same watchlist" to review.
#
# Topics: mutability, index assignment, aliasing, .copy(), .append(),
# .insert(), .extend(), .pop(), .remove().
#
# Requirements:
# 1. Create watchlist holding 475000, 595000, 500000, 445000.
# 2. Create colleague_view by assigning watchlist to it directly. Create
#    archived_copy using .copy().
# 3. Append 329000 to watchlist, then change its first item to 480000 by index
#    assignment.
# 4. Print all three lists with labels.
# 5. Print watchlist is colleague_view, and watchlist is archived_copy.
# 6. In the trailing comment below, state which of the two other names changed
#    and why, referring to what = and .copy() each did. Name the one line in
#    your code that made the difference.
# 7. Working from watchlist as it now stands, and printing it after each step:
#      a. .pop() its last item. Print WHAT .pop() RETURNED as well as the list.
#      b. .remove(595000)
#      c. .insert(1, 610000)
#      d. .extend([250000, 260000])


# --- calls ---


# --- Trailing comment (which name changed, and why) ---


#############################################################################
# Exercise 3 -- Affordable Listings Filter (11 pts)
#############################################################################

# Scenario: A buyer has a ceiling. The analyst needs the subset of asking
# prices at or below it, without losing the original run.
#
# Topics: a function that takes a list and returns a new list, .append() in a
# loop, .index(), .count(), in.
#
# Requirements:
# 1. Create market_prices holding, in this order: 475000, 595000, 500000,
#    445000, 329000, 399000, 1050000, 875000, 485000, 300000
#    Keep them in that order -- the results below depend on it.
# 2. Write a function affordable_listings(prices, ceiling) that returns a NEW
#    list of the values at or below ceiling, in their original order. It must
#    not change prices.
# 3. Give it a docstring in the format described in this file's header.
# 4. Call it with market_prices and a ceiling of 500000. Print the returned
#    list, and print how many values it holds.
# 5. Print market_prices again afterwards, to show it is unchanged.
# 6. Using market_prices, print: the index of 500000; how many times 475000
#    occurs; whether 1050000 is in the list; and whether 999 is in the list.
# 7. In the trailing comment below, explain why in and .index() are not
#    interchangeable, naming the situation in which only one of them will do.


# --- calls ---


# --- Trailing comment (in vs .index()) ---


#############################################################################
# Exercise 4 -- Ranking Listings (11 pts)
#############################################################################

# Scenario: The same run of prices has to be shown three ways in a report: as
# listed, cheapest first, and most expensive first. The original order must
# survive for the audit trail.
#
# Topics: .sort() against sorted(), .reverse() against reversed(), zip().
#
# Requirements:
# 1. Create listed_prices holding 475000, 595000, 500000, 445000, 329000,
#    399000 and build_years holding 1971, 1932, 1998, 1910, 1986, 2010.
# 2. Use sorted() to make an ascending list without changing listed_prices.
#    Print both, then print listed_prices again to show it survived.
# 3. Make a separate copy of listed_prices with .copy(), call .sort() on the
#    copy, and print WHAT .sort() RETURNED as well as the sorted copy.
# 4. Produce a descending list using sorted() followed by .reverse(). Print it.
# 5. Print list(reversed(listed_prices)) -- the original order backwards, which
#    is NOT the same thing as a descending sort.
# 6. Use zip() to pair each price with its build year, convert the result with
#    list(), and print each pair on its own line. Then print the second field
#    of the first pair using nested indexing.
# 7. In the trailing comment below, state which of .sort() and sorted() step 2
#    required and why, and say in one sentence how step 4's output differs from
#    step 5's.


# --- calls ---


# --- Trailing comment (.sort() vs sorted(); step 4 vs step 5) ---


#############################################################################
# Exercise 5 -- Listing Records (12 pts)
#############################################################################

# Scenario: A single listing's four fields never change once recorded. The
# analyst needs them as one value that can be passed around and taken apart,
# and needs a summary that reports two numbers at once.
#
# Topics: tuple literals, immutability, the one-element comma, unpacking,
# returning several values, choosing a container.
#
# Requirements:
# 1. Create a tuple sample_record holding 475000, 168, 143, 1971, in that
#    order. The fields are (price, lot_size_m2, living_space_m2, build_year).
# 2. Unpack it into four named variables in a SINGLE statement, and print each
#    with a label naming the field it holds.
# 3. Print type(sample_record). Then print type((4)) and type((4,)), and state
#    in the trailing comment what the comma does.
# 4. Try changing the record's first field by index assignment. Do NOT leave
#    that line live -- put it in a comment and name the exception class it
#    would raise.
# 5. Write a function price_range(prices) that returns the lowest and the
#    highest value AS TWO VALUES, using min() and max().
# 6. Give it a docstring in the format described in this file's header.
# 7. Call it with [475000, 595000, 500000, 445000, 329000, 399000] twice: once
#    assigning the result to a SINGLE name, printing that name and its type();
#    and once unpacking it into low and high. Print the spread (high - low).
# 8. In the trailing comment below, answer this: week 3 said a function returns
#    exactly one value, so two results needed two functions. Does price_range
#    break that rule? Explain in one or two sentences.


# --- calls ---


# --- Trailing comment (the comma; and does price_range break week 3's rule?) ---


#############################################################################
# Exercise 6 -- Portfolio Report (18 pts)
#############################################################################

# Scenario: The analyst has twenty listings and must report on them. Some rows
# carry a data-entry error and some are missing a field; the report has to be
# right anyway.
#
# Topics: a list of tuples as a table, nested indexing, a loop with unpacking,
# aggregating a column, any() and all(), *args.
#
# A note on the data: normally this would be read from a file. File reading is
# week 7, so the rows are typed directly into this file below. Copy the block
# exactly as it appears -- the expected results depend on these exact numbers.
#
# Two of the build years are data-entry errors: someone typed a trailing zero,
# so 2002 became 20020. Two more listings have no build year at all, recorded
# as None. Both problems are in the data on purpose.
#
# Requirements:
# 1. Copy the LISTINGS block below into your file exactly, keeping the comment
#    that names the field order.
# 2. Write price_column(rows) returning a NEW list of every listing's price, in
#    order. Print how many values it holds, and their sum().
# 3. Print the average price, rounded to two decimal places.
# 4. Print the lowest and the highest price. Then use .index() to find the
#    position of the highest, and print that whole listing tuple.
# 5. Write usable_build_years(rows) returning a NEW list of build years that
#    are BOTH present AND plausible -- a year of None is left out, and so is
#    any year after 2023. Print the list's length, and the earliest and latest
#    year in it.
# 6. In the trailing comment below, state what the latest build year would have
#    been WITHOUT the <= 2023 check, and say why that wrong answer would not
#    have crashed the program.
# 7. Build a list of True/False values recording whether each listing's price
#    is above 1000000, and print any() of it. Do the same for whether each
#    living space is at least 80, and print all() of it. Do the same for
#    whether each build year is present, and print all() of it.
# 8. Write total_of(*values) that accepts ANY NUMBER of numeric arguments and
#    returns their total. Call it with three prices typed directly as
#    arguments, and print the result. State in the trailing comment what type
#    values is inside the function.
# 9. Every function in this exercise returns a value, and none of them changes
#    LISTINGS.

# (price, lot_size_m2, living_space_m2, build_year)
LISTINGS = [
    (475000, 168, 143, 1971),
    (595000, 292, 147, 1932),
    (500000, 128, 156, 1998),
    (445000, 83, 92, 1910),
    (329000, 132, 101, 1986),
    (399000, 129, 133, 2010),
    (1050000, 4405, 117, 1986),
    (485000, 96, 124, 2011),
    (300000, 296, 103, 1964),
    (875000, 620, 240, 2002),
    (535000, 198, 156, 1977),
    (350000, 653, 108, 2004),
    (319000, 162, 86, 1988),
    (295000, 758, 103, 1966),
    (489000, 363, 133, 1978),
    (539000, 470, 133, 1930),
    (422500, 217, 126, 20020),
    (345000, 158, 98, 20110),
    (325000, 262, 136, None),
    (389000, 103, 82, None),
]


# --- calls ---


# --- Trailing comment (the latest year without the check; and what *values is) ---
