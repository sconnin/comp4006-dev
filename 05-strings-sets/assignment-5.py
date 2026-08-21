'''
COMP 4006

Assignment 5 - Strings & Sets

Student Name:
Date Submitted:
Time Spent (approx.):

General Homework Guidelines:
- Submit two files to Canvas: this completed .py file, and a separate .docx file containing
  the reflective prompts and your responses. Do not submit .ipynb files.
- Rename this file before submitting, to hw5_firstname_lastname.py -- your own first and
  last name, lower case, separated by underscores (e.g. hw5_ada_lovelace.py).
- Only use the methods and language features listed below.
  Carried forward: print(), input(), type(), int(), float(), str(), bool(), round(),
  .format(), dir(), id(), help(), range(), len(), enumerate(), isinstance(), sum(),
  locals(), globals(), .lower(), main(), .append(), .clear(), .copy(), .count(),
  .extend(), .index(), .insert(), .pop(), .remove(), .reverse(), .sort(), list(),
  tuple(), min(), max(), zip(), sorted(), reversed(), any(), all().
  New this week -- string methods: .capitalize(), .casefold(), .center(), .endswith(),
  .expandtabs(), .find(), .isalnum(), .isalpha(), .isascii(), .isdecimal(), .isdigit(),
  .isidentifier(), .islower(), .isnumeric(), .isprintable(), .isspace(), .istitle(),
  .isupper(), .join(), .ljust(), .lstrip(), .partition(), .removeprefix(),
  .removesuffix(), .replace(), .rfind(), .rindex(), .rjust(), .rpartition(), .rsplit(),
  .rstrip(), .split(), .splitlines(), .startswith(), .strip(), .swapcase(), .title(),
  .upper(), .zfill().
  New this week -- set methods: .add(), .difference(), .difference_update(), .discard(),
  .intersection(), .intersection_update(), .isdisjoint(), .issubset(), .issuperset(),
  .symmetric_difference(), .symmetric_difference_update(), .union(), .update().
  New this week -- functions: set(), frozenset(), hash(), ord(), chr().
  New this week -- language features: string indexing and slicing, string immutability,
  both quote styles, escape sequences, raw strings, "in" as a substring test, + and * on
  strings, set literals, set operators | & - ^, and set comparisons <= >= < >.

- COMPREHENSIONS are still NOT part of this assignment -- neither list nor set. Python has
  a shorter way to write a loop that builds a list or a set, and you will find it online.
  It is held back until a later unit. Write the loop.
- try/except is NOT part of this assignment. Exercise 2 asks you to judge whether text
  looks like a number; do it with the string test methods above, not by attempting a
  conversion and catching the failure. Error handling is week 7.
- .encode(), .maketrans(), .translate() and .format_map() are NOT part of this assignment.
  The first hands back a type this course never covers, and the other three need a
  dictionary, which is week 6.
- DICTIONARIES are week 6. You will print type({}) once in Exercise 5, because knowing what
  {} actually builds is the point of that requirement. Nothing in this assignment asks you
  to create or use a dictionary.
- There is no del statement. Sets remove with .discard(), .remove() and .clear().
- There is no file reading. Every string you need is typed into this file, which is why the
  data looks hard-coded. Reading from a file is week 7.

- EVERY function you write needs a docstring as the first statement in its body, giving:
  one or two lines on what the function does; an "Args:" section naming each parameter, its
  type, and what it is for; and a "Returns:" section giving the returned type and what it is.
- EVERY function you write returns a value. A function that only prints has returned None.
- A function that is GIVEN a list or a set must not change it unless the exercise says to.
  Build a new one and return it.
- ALWAYS print a set through sorted(). A set does not keep its items in any particular
  order, so printing one directly can come out differently each time you run it. Wrapping
  it in sorted() gives you the same output every run, which is what makes your work
  comparable to the expected results.
- Put your function calls beneath the definitions, under a "# --- calls ---" marker.
- Follow PEP 8: snake_case for names, ALL_CAPS for constants, four-space indentation,
  spaces around operators, and descriptive names (raw_usernames, not u).
- Comments explain WHY, not what.
- Test your code with every value named in an exercise's requirements before submitting, and
  leave the output of your final run in place.
- Print all output with a label that identifies the exercise (e.g. "Exercise 3:").

Total points for this file: 80, made up of two parts.
- 70 points are spread across the six exercises below, using the point value shown on each.
- 10 points are scored once, on the submission as a whole: whether every exercise is present
  and the file follows the instructions in this header.

The requirements printed above each exercise are complete -- everything you need to do the
assignment is in this file. See code-rubric.docx for how each exercise's points are awarded.

Several exercises ask for a short written response in addition to code. Write these directly
into this file as comments, in the location indicated for each exercise -- they are graded as
part of that exercise's points.

This file does NOT include the reflective prompts. Those are a separate 20-point component:
answer them in a .docx file and upload it to Canvas alongside this .py file.
'''


#############################################################################
# Exercise 1 -- Reading a Log Entry (8 pts)
#############################################################################

r'''
Scenario: A security log writes one entry per line in a fixed layout. Before parsing
anything, an analyst pulls fields out by position and confirms they are reading the right
characters.

Topics: string indexing, negative indexing, slicing, len(), "in" as a substring test,
+ and *, immutability, escape sequences and raw strings.

Requirements:
1. Create LOG_ENTRY holding exactly:  2026-02-14 WARN auth jdoe
2. Print its length, and print the largest index that is valid for it. Work the second one
   out from the first; do not type 24.
3. Print the first character by index, and the last by a NEGATIVE index.
4. Using slices, print the date, the level, and the username. The date is the first ten
   characters, the level is positions 11 to 14, and the username is the last four.
5. Print the whole entry reversed, using a slice with a step.
6. Print whether 'auth' is in the entry, and whether 'FAIL' is in the entry.
7. Build and print a summary line joining the date and the username with ' | ' between
   them, using +. Then print a separator made of twelve - characters, using *.
8. In the trailing comment below, state what LOG_ENTRY[11] = 'X' would do and name the
   exception class. Do NOT put that line in your code -- describe it.
9. Print 'col1\tcol2\nrow' and its length. Then print the same text as a raw string and its
   length. In the trailing comment, say why the two lengths differ.
'''


# --- calls ---


# --- Trailing comment (immutability; and why the two lengths differ) ---


#############################################################################
# Exercise 2 -- Normalising Usernames (10 pts)
#############################################################################

'''
Scenario: Usernames arrive from three different systems with inconsistent capitalisation
and stray whitespace. They must be normalised before they can be compared.

Topics: .strip(), .lstrip(), .rstrip(), .lower(), .upper(), .title(), .capitalize(),
.swapcase(), and the content tests .isdigit(), .isalpha(), .isalnum(), .isspace().

Requirements:
1. Create RAW_USERNAMES holding, in this order:
   '  JDoe  ', 'a.smith', '  MCHEN', 'r_patel  ', '  K.O.Brien  '
2. Write a function normalise(names) that returns a NEW list in which every name has been
   stripped of surrounding whitespace and lowercased. It must not change names.
3. Give it a docstring in the format described in this file's header.
4. Print the returned list, then print RAW_USERNAMES again to show it is unchanged.
5. Taking '  JDoe  ' on its own, print the results of .strip(), .lstrip() and .rstrip().
   Wrap each result in square brackets inside the f-string -- f'[{name.lstrip()}]' -- so
   the spaces that remain are visible. Without a marker the three look identical on screen.
6. Print '  JDoe  '.strip() transformed by .upper() and by .swapcase(). Then print
   'ada lovelace' transformed by .title() and by .capitalize(). In the trailing comment,
   state the difference between those last two.
7. Create CODES holding '4417', 'A7', '  ', '3.5', 'admin'. For each one, print the value
   alongside the results of .isdigit(), .isalpha(), .isalnum() and .isspace().
8. In the trailing comment, name one value in CODES for which .isdigit() is False even
   though a person would call it a number, and say what that means for checking input this
   way.
'''


# --- calls ---


# --- Trailing comment (.title() vs .capitalize(); and the .isdigit() limitation) ---


#############################################################################
# Exercise 3 -- Searching an Alert Line (12 pts)
#############################################################################

'''
Scenario: An alert line has to be searched for markers, counted, and redacted before it can
be forwarded outside the security team.

Topics: .find() against .index(), .rfind(), .count(), .startswith(), .endswith(),
.replace(), .removeprefix(), .removesuffix().

Requirements:
1. Create ALERT holding exactly:
   ALERT auth failed for user jdoe from 10.14.7.203 - auth retry pending
2. Print the position of the FIRST 'auth' using .find(), and the position of the LAST using
   .rfind().
3. Print .find('token'). Then, in the trailing comment, state what .index('token') would do
   instead and name the exception class. Do NOT put that line in your code.
4. Print how many times 'auth' occurs.
5. Print whether the line starts with 'ALERT' and whether it ends with 'pending'.
6. Write a function redact(line, name) returning a NEW line with every occurrence of name
   replaced by '****'. Give it a docstring. Call it with ALERT and 'jdoe', print the result,
   then print ALERT again to show it is unchanged.
7. Print the line with the 'ALERT ' prefix removed and, separately, with the ' pending'
   suffix removed, using .removeprefix() and .removesuffix().
8. In the trailing comment, state what .removeprefix() does when the prefix is not there,
   and contrast that with what .index() does when its target is not there.
'''


# --- calls ---


# --- Trailing comment (.index() on a missing target; .removeprefix() on a missing prefix) ---


#############################################################################
# Exercise 4 -- Taking a Record Apart and Putting It Back (12 pts)
#############################################################################

'''
Scenario: A log record arrives as one comma-separated line. A field has to be redacted and
the record written back out in the same format.

Topics: .split(), .rsplit(), .partition(), .join(), sorted() on a string.

A note on .join(): the separator is the string you call the method ON, and the thing you
pass IN is the list. That reads backwards compared with every other method you have met, so
expect to get it the wrong way round the first time. Requirement 9 asks you what happens
when you do.

Requirements:
1. Create CSV_ROW holding exactly:  jdoe,auth,failed,10.14.7.203
2. Split it on commas into fields. Print the list, print how many fields it holds, and print
   its type().
3. Print the first and the last field by index.
4. Replace the last field with 'REDACTED' by index assignment, and print the list. In the
   trailing comment, say why this is allowed here when LOG_ENTRY[11] = 'X' was not allowed
   in Exercise 1.
5. Rejoin fields with commas using .join(), and print the result.
6. Show the round trip is exact: print whether ','.join(CSV_ROW.split(',')) equals CSV_ROW.
7. Create SENTENCE holding:  the audit found three unresolved alerts
   Split it with no argument. Print the list and its length, then print it rejoined three
   ways: with a single space, with -, and with the empty string.
8. Print '-'.join('abc'). In the trailing comment, explain what .join() did when it was
   given a string instead of a list.
9. In the trailing comment, state what fields.join(',') would do and name the exception
   class. Do NOT put that line in your code.
10. Print 'user=jdoe=x'.partition('=') and its type(). Then print 'a,b,c'.rsplit(',', 1)
    and sorted('cab').
'''


# --- calls ---


# --- Trailing comment (why index assignment works here; what .join() did; the wrong order) ---


#############################################################################
# Exercise 5 -- Distinct Users From an Event Log (11 pts)
#############################################################################

'''
Scenario: A login-event log records one line per attempt, so the same user appears many
times. The audit needs the distinct users.

Topics: set(), uniqueness, unordered and unindexed, .add(), .discard(), .remove(), len(),
sorted() on a set.

Requirements:
1. Create LOGIN_EVENTS holding, in this order:
   'jdoe', 'mchen', 'jdoe', 'rpatel', 'mchen', 'jdoe', 'kobrien', 'rpatel'
2. Print how many events there are.
3. Build a set of the distinct users from it. Print how many there are, and print the users
   themselves THROUGH sorted().
4. In the trailing comment, say why the printed order came from sorted() rather than from
   the set, and what would happen without it.
5. Print type() of your set, of set(), and of {}. In the trailing comment, state which of
   those three is not a set, and what it is instead.
6. Add 'tnguyen' to the set and print the new size. Then add 'jdoe' again and print the size
   again. In the trailing comment, say what that second .add() did.
7. Call .discard('zzz') on the set -- a user who is not in it -- and print the size to show
   nothing happened. In the trailing comment, state what .remove('zzz') would have done
   instead and name the exception class, and say which exception a LIST raises in the same
   situation. Do NOT put the .remove() line in your code.
8. Print sorted(set('hello')). In the trailing comment, say how many characters went in and
   how many came out.
'''


# --- calls ---


# --- Trailing comment (sorted(); what {} is; the duplicate .add(); .remove() vs .discard()) ---


#############################################################################
# Exercise 6 -- Reconciling Two Access Systems (17 pts)
#############################################################################

'''
Scenario: Two systems each hold their own list of authorised users. The audit has to report
who has access to both, who has access to only one, and whether a named group is fully
covered.

Topics: union, intersection, difference and symmetric difference in BOTH method and operator
form; .issubset(), .issuperset(), .isdisjoint() and the comparison operators; in-place
update methods.

Requirements:
1. Create these four sets exactly:
     VPN_USERS    = 'jdoe', 'mchen', 'rpatel', 'kobrien', 'tnguyen'
     PORTAL_USERS = 'mchen', 'rpatel', 'lgarcia', 'tnguyen', 'schen'
     AUDITORS     = 'mchen', 'rpatel'
     CONTRACTORS  = 'aroy', 'bwilson'
2. Print the size of VPN_USERS and of PORTAL_USERS.
3. Using the METHOD form, print through sorted(): everyone with access to either system;
   everyone with access to both; everyone on VPN only; everyone on the portal only; and
   everyone on exactly one of the two.
4. Repeat all five using the OPERATOR form, and for each one print whether the two forms
   produced the same result.
5. Print whether AUDITORS is a subset of VPN_USERS, using both .issubset() and <=.
6. Print whether AUDITORS is a PROPER subset of VPN_USERS using <, and print whether
   VPN_USERS is a proper subset of itself. In the trailing comment, explain the difference
   between <= and < using those two results.
7. Print whether VPN_USERS is disjoint from CONTRACTORS, and whether it is disjoint from
   AUDITORS.
8. Make a copy of VPN_USERS, call .intersection_update(PORTAL_USERS) on the copy, and print
   WHAT THAT CALL RETURNED as well as the copy through sorted(). Then print VPN_USERS
   through sorted() to show the original survived.
9. In the trailing comment, name which pair of things from week 4 .intersection() and
   .intersection_update() behave like, and say in one sentence what a container gives up by
   being a set.
'''


# --- calls ---


# --- Trailing comment (<= vs <; the week-4 pair; what a set gives up) ---
