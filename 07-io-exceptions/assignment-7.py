'''
COMP 4006

Assignment 7 - File I/O and Exceptions

Student Name:
Date Submitted:
Time Spent (approx.):

General Homework Guidelines:
- Submit two files to Canvas: this completed .py file, and a separate .docx file containing
  the reflective prompts and your responses. Do not submit .ipynb files.
- Rename this file before submitting, to hw7_firstname_lastname.py -- your own first and
  last name, lower case, separated by underscores (e.g. hw7_ada_lovelace.py).
- Only use the methods and language features listed below.
  Carried forward from weeks 1-6: print(), input(), type(), int(), float(), str(), bool(),
  round(), .format(), dir(), id(), help(), range(), len(), enumerate(), isinstance(), sum(),
  locals(), globals(), main(), all list and tuple methods, all set methods, all dictionary
  methods, all string methods except .encode(), .maketrans(), .translate() and
  .format_map(), list(), tuple(), set(), frozenset(), dict(), min(), max(), zip(),
  sorted(), reversed(), any(), all(), hash(), ord(), chr().
  New this week -- opening a file and the file object's own methods: open(), .read(),
  .readline(), .readlines(), .write(), .writelines(), .close().
  New this week -- the json module: json.load(), json.dump(), json.loads(), json.dumps().
  New this week -- the csv module: csv.reader(), csv.writer(), .writerow(), .writerows().
  New this week -- language features: with open(...) as file:, the file modes 'r', 'w' and
  'a', encoding='utf-8' as a keyword argument to open(), newline='' as a keyword argument to
  open(), iterating a file object directly with for line in file:, try/except, except naming
  a specific exception class, except naming several classes in a tuple, try/except/else,
  try/except/finally, raise including raise ValueError('message'), FileNotFoundError, and
  import json and import csv.

- YOU NEED ONE DOWNLOADED FILE: senators.json, posted to Canvas beside this assignment.
  Save it into the SAME FOLDER as this .py file. Nothing this week builds a path, so the
  data file has to sit right beside your code. Do not rename it. Do not open it in Excel
  and re-save it.
  If it is missing or in the wrong folder, open() raises FileNotFoundError and your program
  stops -- which means the whole file does not run, and that costs you far more than one
  exercise. Check this before you start.
- EVERY OTHER FILE this assignment uses, this assignment creates. Exercises 2, 3 and 5 write
  the files they read, so you never need a second download.
- Two filenames must NOT exist: missing_one.txt and missing_two.txt, in Exercise 3. Do not
  create them. They are missing on purpose -- that is the whole point of the exercise.

- EVERY open() you write uses "with". A file opened without it stays open when something
  goes wrong partway through, and that is exactly the case "with" exists to handle. This
  costs Correctness points even when your answer is right.
- EVERY open() you write passes encoding='utf-8'. The data file contains names with accents
  and curly quotation marks in them. Without the encoding it may read incorrectly, or fail
  outright, on some machines and not others -- which is the worst kind of bug to chase.
- EVERY except you write names an exception class, or several classes in a tuple. A bare
  "except:" with no class is out of scope. It catches everything, including the mistakes you
  have not thought of yet, so a typo turns into a silently wrong answer instead of an error
  message. The session shows you this; do not use it here.
- NEVER print an entire file. senators.json is 145,089 characters long. Print a length, a
  count, or the first few lines. An exercise that dumps the whole file to the screen has not
  followed the instructions.
- NEVER name a variable file, open, list, dict, set or str. Doing so replaces the builtin of
  that name for the rest of your file, and the error shows up much later with a message that
  says nothing about naming. This costs Readability points.
- There is no import except json and csv. The os module, pathlib and openpyxl are all out of
  scope, and so are .seek() and .tell().
- Skip a CSV header row with enumerate() -- skip the row whose index is 0. You will find
  next() used for this everywhere online; next() is out of scope for this course.
- COMPREHENSIONS are allowed and are not required. List, set and dictionary comprehensions
  have all been available since weeks 4, 5 and 6. Every exercise here is written for the
  loop, and either choice is fine. Nested-loop, ternary and generator forms are still out.

- EVERY function you write needs a docstring as the first statement in its body, giving:
  one or two lines on what the function does; an "Args:" section naming each parameter, its
  type, and what it is for; and a "Returns:" section giving the returned type and what it is.
- EVERY function you write returns a value. A function that only prints has returned None.
- Put your function calls beneath the definitions, under a "# --- calls ---" marker.
- Follow PEP 8: snake_case for names, ALL_CAPS for constants, four-space indentation,
  spaces around operators, and descriptive names (line_count, not n).
- Comments explain WHY, not what.
- Test your code with every value named in an exercise's requirements before submitting, and
  leave the output of your final run in place.
- Print all output with a label that identifies the exercise (e.g. "Exercise 3:").
- RUN YOUR WHOLE FILE TWICE IN A ROW before submitting, and check that the output is the
  same both times. This is new this week and it matters: your program now writes files, and
  a file left behind by the first run is still there for the second one. If your two runs
  disagree, you have used 'a' somewhere you meant 'w'.

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
# Exercise 1 -- Reading a File as Text (10 pts)
#############################################################################

r'''
Scenario: A dataset has arrived. Before anything can be analysed, someone has to open it and
find out what is actually in there -- and a file is just characters until something parses
it.

Topics: open() with "with", encoding='utf-8', .read(), .readline(), .readlines(),
for line in file:, the trailing newline, .rstrip().

Requirements:
1. Write count_characters(filename). Open the file with "with" and encoding='utf-8', read it
   with .read(), and return the number of characters. Do NOT print the string itself.
2. Write first_line(filename) that uses .readline() and returns the first line WITH ITS
   NEWLINE REMOVED.
3. Write all_lines(filename) that uses .readlines() and returns the list.
4. Write count_lines_by_loop(filename) that uses "for line in file:" and returns the number
   of lines, without building a list.
5. Call all four on 'senators.json'. Print the character count, the first line, the length of
   the list from requirement 3, and the count from requirement 4.
6. Print the FIRST THREE items of the list from requirement 3 AS A LIST, in a single
   print() call, so you can see exactly what they contain. Then print the same three with
   .rstrip() applied, one per line.
7. In the trailing comment below, say why requirements 3 and 4 give the same number, and
   state which of the two you would choose for a file far larger than this one, and why.

Hint for requirement 6: printing a line on its own hides its newline. Printing the LIST shows
you each string exactly as Python holds it, '\n' included -- which is why requirement 6 asks
for the list in one call and the stripped version line by line.
'''


# --- calls ---


# --- Trailing comment (why the two counts agree, and which you would choose) ---


#############################################################################
# Exercise 2 -- Writing a Briefing File (10 pts)
#############################################################################

'''
Scenario: The findings from Exercise 1 have to leave the program and land somewhere a
colleague can read them. That means writing a file -- and writing destroys before it
creates.

Topics: the 'w' and 'a' modes, .write(), .writelines(), the newline you have to supply
yourself, reading back to confirm.

Requirements:
1. Write write_briefing(filename, lines). Open filename in 'w' mode and write every string
   in lines using .writelines(). Return the number of strings written.
2. Write append_line(filename, text). Open filename in 'a' mode, write text, and return
   True.
3. Build BRIEFING holding exactly these three strings, EACH ENDING IN A NEWLINE CHARACTER:
   'Senate dataset briefing', 'Records: 100', 'Source: senators.json'.
4. Call write_briefing('briefing.txt', BRIEFING), then append_line to add
   'Reviewed by: analyst' with a newline. Print both return values.
5. Read briefing.txt back with .readlines() and print the list, then print how many lines it
   holds.
6. Call write_briefing a second time on the same file, this time with a list holding the
   single string 'overwritten' plus a newline. Read the file back again and print what it
   now holds.
7. In the trailing comment below, say what happened to the four lines from requirement 5,
   and name the single character in the open() call that caused it.

Warning: neither .write() nor .writelines() adds a newline for you. print() has been doing
that silently since week 1 and this is the week it stops. If you leave the newlines out of
BRIEFING your file will hold one long line, and .writelines() will not warn you.
'''


# --- calls ---


# --- Trailing comment (what happened to the four lines, and which character did it) ---


#############################################################################
# Exercise 3 -- Files That Are Not There (12 pts)
#############################################################################

'''
Scenario: A batch job is handed a list of filenames. Some of them do not exist. The job's
purpose is to process the ones that do -- stopping at the first bad name is not an option.

Topics: try/except, FileNotFoundError, catching several classes in one except, why a bare
except is a trap, try inside a loop against try around it.

Requirements:
1. Write read_or_none(filename). Try to open filename and return its first line with the
   newline removed. If the file does not exist, catch FileNotFoundError, print a message
   naming the file, and return None. Catch that class by name.
2. Using what Exercise 2 taught you, write a file batch_notes.txt in 'w' mode holding the
   single line 'batch notes' followed by a newline. Then build FILENAMES holding
   'senators.json', 'missing_one.txt', 'batch_notes.txt' and 'missing_two.txt', in that
   order. Do NOT create the two missing files.
3. Write read_all(filenames). Loop over the list, call read_or_none on each, and return a
   list holding only the results that are not None. The try must be INSIDE read_or_none, so
   the loop keeps going after a failure. Print the returned list and its length.
4. Write to_number(value). Return float(value). Catch ValueError and TypeError IN A SINGLE
   except NAMING BOTH, and return None when either is raised.
5. Call to_number on '12.5', on 'abc', and on None, and print each result.
6. In the first trailing comment below, say what read_all would return if the try were moved
   out of read_or_none and wrapped around the loop in requirement 3 instead. Do NOT write
   that version in your code -- describe it.
7. In the second trailing comment, say in one sentence why "except:" on its own is worse
   than "except FileNotFoundError:" here.
'''


# --- calls ---


# --- Trailing comment 1 (what read_all would return if the try wrapped the loop) ---


# --- Trailing comment 2 (why a bare except is worse here) ---


#############################################################################
# Exercise 4 -- Validating Before You Trust (12 pts)
#############################################################################

'''
Scenario: The numbers coming out of a file are strings, and some of them are wrong in ways
float() will happily accept. A negative seat count is not a parsing error -- it is a data
error, and the program has to say so itself.

Topics: else and finally, raise, the difference between a problem you catch and a problem
you declare.

Requirements:
1. Write validate_count(value). Inside a try, convert value with float(). Use
   "except ValueError:" to return the string 'not a number'. Use an "else:" block that
   raises ValueError('seat count cannot be negative') when the number is below zero, and
   otherwise returns the number. Add a "finally:" block that prints a one-line message
   naming the value it was given.
2. Call validate_count on '12', on 'abc', and on '-3'. The third one will raise, so wrap
   that call in its own try / except ValueError and print the message from the exception.
3. Print the return value of each of the first two calls.
4. Write total_valid(values). Loop over values, call validate_count on each inside a try,
   skip any value that raises or returns 'not a number', and return the total of the rest.
5. Call total_valid with ['2', '2', 'abc', '-1', '1'] and print the result.
6. In the first trailing comment below, say how many times the finally message printed
   during requirement 5, and why that number is what it is.
7. In the second trailing comment, say in one sentence why requirement 1 uses raise for the
   negative value instead of returning 'not a number' for it as well.
'''


# --- calls ---


# --- Trailing comment 1 (how many times finally printed, and why) ---


# --- Trailing comment 2 (why raise, and not 'not a number', for a negative value) ---


#############################################################################
# Exercise 5 -- Writing and Reading a CSV (14 pts)
#############################################################################

'''
Scenario: The results have to go somewhere a spreadsheet can open. That means CSV -- and CSV
is a text file with commas in it, right up until one of your fields contains a comma.

Topics: csv.writer(), .writerow(), .writerows(), csv.reader(), newline='', skipping a header
with enumerate(), .split(',') and where it breaks.

Requirements:
1. Write write_csv(filename, header, rows). Open filename in 'w' mode with newline='' and
   encoding='utf-8', write header with .writerow() and rows with .writerows(), and return
   the number of DATA rows written.
2. Build HEADER holding 'state', 'party', 'seats', and ROWS holding ['WA', 'Democrat', 2],
   ['TX', 'Republican', 2], ['ME', 'Independent', 1]. Call
   write_csv('seats.csv', HEADER, ROWS) and print the return value.
3. Write read_csv_rows(filename) using csv.reader(). Return a list of every row INCLUDING
   the header. Print it.
4. Write total_seats(filename). Read the file with csv.reader(), skip the header USING
   enumerate() -- skip the row whose index is 0 -- convert the third field with int(), and
   return the total. Print it.
5. Write write_tricky(filename) that uses csv.writer() to write the header 'committee',
   'chair' and the single row ['Energy, Science and Technology', 'Cantwell'] to filename.
   Call it on 'tricky.csv'.
6. Read tricky.csv back TWICE and print both results: once with .readlines() and .split(',')
   on the second line, and once with csv.reader(). Print the length of each result.
7. In the trailing comment below, say why the two lengths in requirement 6 differ, and name
   the CHARACTER in the file that csv.reader() understands and .split(',') does not.

Warning for requirement 4: csv.reader() gives you back strings, not numbers. The seats come
out as '2', not 2. Adding those together without int() either concatenates them or raises,
depending on what you started your total at.
'''


# --- calls ---


# --- Trailing comment (why the lengths differ, and which character is responsible) ---


#############################################################################
# Exercise 6 -- Parsing JSON, and Choosing a Format (12 pts)
#############################################################################

'''
Scenario: The same file Exercise 1 read as 145,089 characters is, in fact, a structure.
Nothing about the file changed -- only what was used to read it.

Topics: json.dumps(), json.loads(), json.dump(), json.load(), the JSON-to-Python type table
in practice, reaching into nested data, choosing a format.

The four names are the thing to get right. load and dump work on a FILE. loads and dumps
work on a STRING -- the s stands for string. Reaching for the wrong one of a pair gives you
an error that does not explain itself.

Requirements:
1. Build SMALL holding 'state' -> 'WA', 'seats' -> 2, 'current' -> True, 'caucus' -> None.
2. Convert SMALL to a string with json.dumps() and print it, then print its type(). Note in
   a comment what happened to True and to None.
3. Convert that string back with json.loads(). Print the result, and print whether it is
   equal to SMALL.
4. Write SMALL to 'small.json' with json.dump(), then read it back with json.load(). Print
   the result, and print whether it is equal to SMALL. Use "with" and encoding='utf-8' on
   both.
5. Write load_senators(filename) that opens the file and returns json.load()'s result. Call
   it on 'senators.json'. Print the type() of the result, its keys AS A SORTED LIST, and the
   number of items in data['objects'].
6. Write count_parties(records) that takes data['objects'] and returns a dictionary mapping
   each party to how many senators hold it. Print it through sorted().
7. Write names_from_state(records, state) that returns a sorted list of the 'lastname' of
   every record whose 'state' matches. The name is nested: each record has a 'person' key
   holding another dictionary. Call it with 'WA' and print the result.
8. Print the value of 'caucus' for the first record, and its type().
9. In the trailing comment below, say which of the three formats in this assignment -- plain
   text, CSV, JSON -- could hold senators.json's data without losing anything, and what a
   CSV would have to do to data['objects'][0]['person']['lastname'] to store it in a column.
'''


# --- calls ---


# --- Trailing comment (which format loses nothing, and what a CSV would have to do) ---
