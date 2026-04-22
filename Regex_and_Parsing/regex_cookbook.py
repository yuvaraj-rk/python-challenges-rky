import re

#Grouping with Parentheses ()
# Parentheses create groups: group(1) for the first group, group(2) for the second.
# The first group (\d\d\d) captures the area code.
# The second group (\d\d\d-\d\d\d\d) captures the main number.
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242.')

# To retrieve all groups at once, use the groups() method, which returns a tuple.
area_code, main_number = mo.groups()

print(f"Area Code: {area_code}") #mo.group(1)
print(f"Main Number: {main_number}") #mo.group(2)
print(f"Full Match: {mo.group(0)}") #mo.group()
print(mo.groups())

'''
labex:project/ $ python3 main.py
Area Code: 415
Main Number: 555-4242
Full Match: 415-555-4242
('415', '555-4242')
'''


#Alternation with the Pipe |
# The pipe | matches one of several patterns within a group.
# Here, it matches 'man', 'mobile', 'copter', or 'bat'.
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')

print(f"Full match: {mo.group()}")
print(f"Group 1: {mo.group(1)}")

'''
labex:project/ $ python3 main.py
Full match: Batmobile
Group 1: mobile
'''


#Repetition with Quantifiers

#Optional Matching with ?

import re

# The (wo)? group is optional. It will match 'wo' if it exists, or match nothing if it doesn't.
bat_regex = re.compile(r'Bat(wo)?man')

mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())

'''
labex:project/ $ python3 main.py
Batman
Batwoman
'''

#Zero or More with *
import re

# The (wo)* group can appear zero or more times.
bat_regex = re.compile(r'Bat(wo)*man')

mo1 = bat_regex.search('The Adventures of Batman') # Zero 'wo'
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwowowowoman') # Four 'wo's
print(mo2.group())

'''
labex:project/ $ python3 main.py
Batman
Batwowowowoman
'''

#One or More with +
import re

# The (wo)+ group must appear at least once.
bat_regex = re.compile(r'Bat(wo)+man')

mo1 = bat_regex.search('The Adventures of Batwoman') # One 'wo'
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batman') # Zero 'wo's
print(mo2 is None) # This will print True because no match is found.

'''
labex:project/ $ python3 main.py
Batwoman
True
'''

#Specific Repetitions with {}
'''
Curly brackets {} allow you to specify an exact number of repetitions, or a range.

{3} matches exactly three times.
{3,5} matches between three and five times.
{3,} matches three or more times.
{,5} matches up to five times.
'''
import re

# (Ha){3} matches 'Ha' repeated exactly 3 times.
ha_regex = re.compile(r'(Ha){3}')
mo1 = ha_regex.search('HaHaHa')
print(mo1.group())

'''
labex:project/ $ python3 main.py
HaHaHa
'''

#Greedy and Non-Greedy Matching
'''
By default, Python's regex is "greedy," meaning it matches the longest possible string. To make it "non-greedy" (match the shortest possible string), add a question mark ? after the quantifier.
'''
import re

# Greedy match: {3,5} matches the longest possible string (5 'Ha's).
greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_ha_regex.search('HaHaHaHaHa')
print(f"Greedy match: {mo1.group()}")

# Non-greedy match: {3,5}? matches the shortest possible string (3 'Ha's).
non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
print(f"Non-greedy match: {mo2.group()}")

'''
labex:project/ $ python3 main.py
Greedy match: HaHaHaHaHa
Non-greedy match: HaHaHa
'''

#The findall() Method
'''
While search() returns only the first match, 
the findall() method returns a list of all non-overlapping matches in the string. 

If the regex has groups, findall() returns a list of tuples, 
where each tuple contains the strings for each group.
'''
import re

# If the regex has no groups, findall() returns a list of strings.
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matches = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(matches)

'''
labex:project/ $ python3 main.py
['415-555-9999', '212-555-0000']
'''


#Making Your Own Character Classes []
'''
Square brackets [] let you define a custom character class that will match any single character within it. For example, [aeiou] matches any lowercase vowel. You can also specify a range, like [a-z] for any lowercase letter or [0-9] for any digit.

A caret ^ as the first character inside the brackets creates a negative character class, which matches any character not in the class.
'''
import re

# [aeiouAEIOU] matches any vowel, lowercase or uppercase.
vowel_regex = re.compile(r'[aeiouAEIOU]')
vowels = vowel_regex.findall('Robocop eats baby food. BABY FOOD.')
print(vowels)

'''
labex:project/ $ python3 main.py
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
'''

#Anchors: Caret ^ and Dollar Sign $
'''
Anchors are used to assert a position in the string.

The caret ^ matches the beginning of the string.
The dollar sign $ matches the end of the string.
When used together (^...$), they enforce that the entire string must match the pattern.
'''

import re

# ^Hello matches strings that start with 'Hello'.
begins_with_hello = re.compile(r'^Hello')
match1 = begins_with_hello.search('Hello world!')
print(match1 is not None) # True

# \d+$ matches strings that end with one or more digits.
ends_with_number = re.compile(r'\d+$')
match2 = ends_with_number.search('Your number is 42')
print(match2.group()) # '42'

# ^\d+$ matches strings that consist only of digits.
whole_string_is_num = re.compile(r'^\d+$')
match3 = whole_string_is_num.search('1234567890')
print(match3 is not None) # True

'''
labex:project/ $ python3 main.py
True
42
True
'''


#The Wildcard Character .
'''
The dot . (or wildcard) character matches any single character except a newline. 
It's a useful shorthand for "any character".
'''
import re

# The . character matches any character (except newline).
# So, .at matches 'cat', 'hat', 'sat', etc.
at_regex = re.compile(r'.at')
matches = at_regex.findall('The cat in the hat sat on the flat mat.')
print(matches)

'''
labex:project/ $ python3 main.py
['cat', 'hat', 'sat', 'lat', 'mat']
'''

#Advanced Methods and Flags
#Matching Everything with Dot-Star .*
'''
The combination .* is a common pattern that matches any character (.) repeated zero or more times (*). 
It's used to match any sequence of characters. By default, it's greedy and will match as much text as possible.

To make it non-greedy, use .*?. This will match the shortest possible string.
'''

import re

# The pattern (.*) captures everything between 'First Name: ' and ' Last Name: '.
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Al Last Name: Sweigart')
print(f"First Name: {mo.group(1)}")
print(f"Last Name: {mo.group(2)}")

'''
labex:project/ $ python3 main.py
First Name: Al
Last Name: Sweigart
'''

#Matching Newlines with re.DOTALL
'''
By default, the dot . character does not match newline characters (\n). 
To change this, you can pass re.DOTALL as a second argument to re.compile(). 
This flag allows . to match all characters, including newlines.
'''

import re

# With re.DOTALL, '.*' will match across multiple lines.
newline_regex = re.compile('.*', re.DOTALL)
mo = newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())

'''
labex:project/ $ python3 main.py
Serve the public trust.
Protect the innocent.
Uphold the law.
'''

#Case-Insensitive Matching with re.IGNORECASE
'''
To make your regex ignore case (e.g., match "cat", "Cat", and "CAT"), 
pass re.IGNORECASE or its shorthand re.I as the second argument to re.compile().
'''

import re

# re.I makes the pattern 'robocop' match 'Robocop', 'ROBOCOP', etc.
robocop = re.compile(r'robocop', re.I)
match = robocop.search('Robocop is part man, part machine, all cop.')
print(match.group())

'''
labex:project/ $ python3 main.py
Robocop
'''

#Substituting Strings with the sub() Method
'''
The sub() method finds all occurrences of a pattern and replaces them with a specified string. 
It takes two arguments: the replacement string and the string to search.
'''
import re

# The pattern 'Agent \w+' matches 'Agent ' followed by one or more word characters.
names_regex = re.compile(r'Agent \w+')
result = names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(result)

'''
labex:project/ $ python3 main.py
CENSORED gave the secret documents to CENSORED.
'''

#Managing Complex Regexes with re.VERBOSE
'''
When regex patterns become complex, they can be hard to read. 
By passing re.VERBOSE to re.compile(), you can write your regex 
across multiple lines and add comments to explain different parts. 
Whitespace and comments (#) within the string are ignored.

This complex regex:
phone_regex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

Becomes this readable version with re.VERBOSE:
'''

import re

phone_regex = re.compile(r'''(
    (\d{3} | \(\d{3}\))?          # area code (optional)
    (\s | - | \.)?                # separator (optional)
    \d{3}                         # first 3 digits
    (\s | - | \.)                 # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension (optional)
    )''', re.VERBOSE)

mo = phone_regex.search("My phone number is 415-555-4242 ext. 55")
if mo:
    print(f"Found: {mo.group()}")
    
'''
labex:project/ $ python3 main.py
Found: 415-555-4242 ext. 55
'''
