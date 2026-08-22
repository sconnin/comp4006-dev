'''
COMP 4006

Assignment 6 - Dictionaries

Student Name:
Date Submitted:
Time Spent (approx.):

General Homework Guidelines:
- Submit two files to Canvas: this completed .py file, and a separate .docx file containing
  the reflective prompts and your responses. Do not submit .ipynb files.
- Rename this file before submitting, to hw6_firstname_lastname.py -- your own first and
  last name, lower case, separated by underscores (e.g. hw6_ada_lovelace.py).
- Only use the methods and language features listed below.
  Carried forward from weeks 1-5: print(), input(), type(), int(), float(), str(), bool(),
  round(), .format(), dir(), id(), help(), range(), len(), enumerate(), isinstance(), sum(),
  locals(), globals(), main(), all list and tuple methods, all set methods, all string
  methods except .encode(), .maketrans(), .translate() and .format_map(), list(), tuple(),
  set(), frozenset(), min(), max(), zip(), sorted(), reversed(), any(), all(), hash(),
  ord(), chr().
  New this week -- dictionary methods: .fromkeys(), .get(), .items(), .keys(), .popitem(),
  .setdefault(), .values(). Note .clear(), .copy(), .pop() and .update() were already on the
  list from lists and sets, and they work on dictionaries too.
  New this week -- functions: dict().
  New this week -- language features: dictionary literals, the empty dictionary {}, key
  access with record['name'], key assignment, nested access, "in" and "not in" testing KEYS,
  iterating a dictionary with for, unpacking .items() in a loop, view objects, insertion
  order, | and |= to merge dictionaries, dict() argument forms, **kwargs in a function
  definition, and dictionary comprehensions.

- COMPREHENSIONS are allowed and are not required. The session shows the dictionary form,
  and list and set comprehensions have been available since weeks 4 and 5. Every exercise
  here is written for the loop, and either choice is fine. Nested-loop, ternary and
  generator forms are still out of scope.
- try/except is NOT part of this assignment. Exercise 2 asks you to avoid a KeyError rather
  than catch one, and .get() is this week's answer to that problem. Error handling is week 7.
- There is no import of any kind. In particular the json module is week 7, together with
  reading files. The session compares JSON with dictionaries, but nothing here asks you to
  read or write any.
- There is no del statement. Remove entries with .pop(), .popitem() or .clear().
- **kwargs IS part of this assignment, in a function definition (Exercise 6). Week 3 told
  you it was waiting for a week when you knew what a dictionary was. This is that week.
  ** at a call site is still out of scope, as * has been since week 4.
- Set operations on dictionary views -- record.keys() | other_set and the like -- are out of
  scope. Merging two dictionaries with | is a different thing and IS allowed.

- EVERY function you write needs a docstring as the first statement in its body, giving:
  one or two lines on what the function does; an "Args:" section naming each parameter, its
  type, and what it is for; and a "Returns:" section giving the returned type and what it is.
- EVERY function you write returns a value. A function that only prints has returned None.
- A function that is GIVEN a dictionary must not change it unless the exercise says to.
  Build a new one and return it.
- NEVER name a variable dict, list, set or str. Doing so replaces the builtin of that name
  for the rest of your file, and the error shows up much later with a message that says
  nothing about naming. This costs Readability points.
- Print a dictionary directly when its order matters, and through sorted() when it does not.
  Unlike a set, a dictionary keeps the order things were added, so its printed form is the
  same every run. Where an exercise wants alphabetical output it says so.
- Put your function calls beneath the definitions, under a "# --- calls ---" marker.
- Follow PEP 8: snake_case for names, ALL_CAPS for constants, four-space indentation,
  spaces around operators, and descriptive names (service_ports, not d).
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
# Exercise 1 -- Building a Service Record (8 pts)
#############################################################################

'''
Scenario: A platform team keeps one record per running service. Before anything can be
looked up, the record has to exist -- and there is more than one way to build it.

Topics: dictionary literals, dict() with keyword arguments, dict(zip(...)), .fromkeys(),
len(), list() on a dictionary.

Requirements:
1. Build service_literal with a dictionary literal, holding 'name' -> 'auth-api',
   'port' -> 8443, 'region' -> 'us-east', 'healthy' -> True.
2. Build the same record again as service_kwargs, using dict() with keyword arguments.
3. Create FIELDS holding 'name', 'port', 'region', 'healthy' and VALUES holding 'auth-api',
   8443, 'us-east', True. Build the record a third time as service_zipped, using dict() and
   zip().
4. Print all three, then print whether all three are equal to each other.
5. Use .fromkeys() with FIELDS to build blank_record, in which every value is None. Print it.
6. Print how many keys service_literal has, and print its keys as a LIST.
7. In the trailing comment below, state what service_literal[0] would do and name the
   exception class. Do NOT put that line in your code -- describe it. Then say in one
   sentence why a dictionary has no "first" item in the way a list does.
'''


# --- calls ---


# --- Trailing comment (what service_literal[0] would do, and why) ---


#############################################################################
# Exercise 2 -- Reading and Editing a Record (10 pts)
#############################################################################

'''
Scenario: A record has to be read for fields that may not be present, then amended as the
service changes.

Topics: key access, KeyError, .get() with and without a default, key assignment, .pop(),
.popitem(), .update(), .clear().

Requirements:
1. Create service holding 'name' -> 'auth-api', 'port' -> 8443, 'region' -> 'us-east',
   'healthy' -> True.
2. Print service['name'].
3. Print .get('owner'), then .get('owner', 'unset'). Then print whether 'owner' is in the
   dictionary, and print its length, to show that .get() did not add anything.
4. In the trailing comment, state what service['owner'] would do and name the exception
   class. Do NOT put that line in your code.
5. Make a copy of service called working, using dict(). Add 'owner' -> 'platform' to it
   and print it. Then change 'port' to 9443 and print it again. In the trailing comment, say
   how those two lines differ in effect and why they look identical.
6. Print what .pop('healthy') returns, as well as the keys that remain. Then print
   .pop('gone', 'none') -- a key that is not there, with a default.
7. Print what .popitem() returns, and say in the trailing comment which entry it removed.
8. Print what .update({'region': 'eu-west', 'tier': 2}) RETURNS, then print working.
9. Call .clear() on working and print it and its length. Then print service, to show the
   original was never touched.
'''


# --- calls ---


# --- Trailing comment (KeyError; add vs update; what .popitem() removed) ---


#############################################################################
# Exercise 3 -- Reporting Over a Registry (12 pts)
#############################################################################

'''
Scenario: The registry maps each service to its port. A report needs it in the order it was
built and again in alphabetical order, plus a few totals.

Topics: iterating keys, .items() unpacking, view objects, insertion order, sorted(), sum(),
max(), min(), len().

Requirements:
1. Create SERVICE_PORTS holding, in this order: 'auth-api' -> 8443, 'billing' -> 9100,
   'search' -> 8080, 'alerts' -> 7000.
2. Loop over it with for and print each KEY on its own line. In the trailing comment, say
   what the loop variable holds.
3. Loop over .items(), unpacking into two names, and print each service with its port on one
   line.
4. Print .keys() directly and .values() directly, then print list() of .keys(). In the
   trailing comment, say what the first two printed and why the third looks different.
5. In the same trailing comment, state what SERVICE_PORTS.keys()[0] would do and name the
   exception class. Do NOT put that line in your code.
6. Print the keys in the order they were added, then print them in alphabetical order using
   sorted(). In the trailing comment, say why both were needed here when a set in week 5
   only ever needed the second.
7. Print sorted() of .items().
8. Print the total of all the ports, the highest port, the lowest port, and how many
   services there are.
'''


# --- calls ---


# --- Trailing comment (the loop variable; views; order vs sorted()) ---


#############################################################################
# Exercise 4 -- Counting Log Severities (12 pts)
#############################################################################

'''
Scenario: A day's log lines are reduced to their severity levels. The report needs how many
of each, and which was most common.

Topics: counting with .get(), the same with .setdefault(), "in" testing keys, sorted(),
sum() over values.

Requirements:
1. Create EVENTS holding, in this order: 'WARN', 'INFO', 'ERROR', 'WARN', 'INFO', 'WARN',
   'CRITICAL', 'INFO', 'ERROR', 'WARN'. Print how many events there are.
2. Write count_levels(events) returning a NEW dictionary mapping each level to how many
   times it occurs, built with a for loop and .get(). Give it a docstring. Print the result.
3. Write count_levels_setdefault(events) producing the same result using .setdefault()
   instead. Print its result, then print whether the two agree.
4. In the trailing comment, state what counts[level] = counts[level] + 1 would do on the
   first occurrence of a level, and name the exception class.
5. Print how many distinct levels there are, and print the levels in alphabetical order.
6. Print sorted() of the counts as items.
7. Print whether 'ERROR' is in the counts, whether 'DEBUG' is, and whether 2 is. In the
   trailing comment, explain that third result.
8. Find and print the most frequent level and its count, using a for loop over .items().
9. Print the total of all the counts, and print whether it equals the number of events.
'''


# --- calls ---


# --- Trailing comment (the KeyError; and why 2 is not "in" the counts) ---


#############################################################################
# Exercise 5 -- Merging Config and Reading Nested Data (12 pts)
#############################################################################

'''
Scenario: Every service starts from a shared default configuration and overrides some of it.
Separately, the fleet is held as one record per service, each record a dictionary of its own.

Topics: |, |=, .update(), nested dictionaries, .items() unpacking over nested data, .get()
with a default on a missing record.

Requirements:
1. Create DEFAULTS holding 'region' -> 'us-east', 'tier' -> 1, 'retries' -> 3, and OVERRIDES
   holding 'tier' -> 2, 'timeout' -> 30.
2. Print DEFAULTS | OVERRIDES, then print OVERRIDES | DEFAULTS. In the trailing comment, say
   what 'tier' is in each and why.
3. Print DEFAULTS again, to show | did not change it.
4. Make a copy of DEFAULTS, apply |= with OVERRIDES, and print it.
5. Make another copy, call .update(OVERRIDES) on it, print WHAT THAT CALL RETURNED, then
   print the copy. Print whether the |= result and the .update() result are equal.
6. Create FLEET as a dictionary of three services, each value itself a dictionary:
     'auth-api' -> {'port': 8443, 'owner': 'platform', 'healthy': True}
     'billing'  -> {'port': 9100, 'owner': 'payments', 'healthy': False}
     'search'   -> {'port': 8080, 'owner': 'platform', 'healthy': True}
7. Print the owner of 'billing' using nested access in a single expression.
8. Loop over FLEET with .items() and build a LIST of every owner. Print it.
9. Loop again and build a list of the services whose 'healthy' is False. Print it, and print
   how many services there are in total.
10. Print the owner of a service that is NOT in the fleet, using .get() twice with defaults
    so that nothing raises. In the trailing comment, say what each default protects against.
'''


# --- calls ---


# --- Trailing comment (which tier wins and why; what each .get() default protects) ---


#############################################################################
# Exercise 6 -- Keys, Keyword Arguments, and Choosing a Container (16 pts)
#############################################################################

'''
Scenario: The registry needs keys that are not simple strings, a reporting function that
accepts whatever settings a caller chooses to pass, and a written justification of the
container used.

Topics: hashability, tuples as keys, **kwargs, sorted() over .items(), .join(), container
choice across all five types.

Requirements:
1. Create BY_COORDS using TUPLES as keys: (40, -73) -> 'nyc-east' and (37, -122) ->
   'sf-west'. Print it, and print the value stored for (40, -73).
2. In the trailing comment, state what {['a', 'b']: 'x'} would do and name the exception
   class. Do NOT put that line in your code. Say in one sentence why a tuple works as a key
   where a list does not.
3. Create a dictionary with a LIST as a value -- for example 'tags' -> ['prod', 'critical']
   -- and print it. In the trailing comment, say why that is allowed when a list as a KEY is
   not.
4. Write describe_service(name, **settings) returning the service name, the TYPE NAME of
   settings, how many settings were given, and their keys in alphabetical order. Give it a
   docstring that documents **settings in the Args: section.
5. Call it with 'auth-api' and the keyword arguments port=8443 and tier=2, and print the
   result. Call it again with only 'auth-api' and print that too.
6. In the trailing comment, state what type settings is inside the function, and say why
   this feature could not have been taught before this week.
7. Write summarise(**settings) returning a single string of key=value pairs in alphabetical
   order, separated by ', ', built with a loop and .join(). Call it with region='eu' and
   tier=2, and call it with nothing at all. Print both results.
8. Take the text 'jdoe,mchen,jdoe' and print it five ways: as the string itself; as a list;
   as a tuple; as a set through sorted(); and as a dictionary of counts.
9. In the trailing comment, state which of those five containers loses information, which
   keeps a duplicate without recording it, and which one COUNTS it. Then name in one
   sentence the question a dictionary answers that a set cannot.
'''


# --- calls ---


# --- Trailing comment (why a tuple key works; what **settings is; the five containers) ---
