# Regular expressions
# Regular expressions help you find patterns in text and they are avalible in
#  many different laguages
# First let's find phone numbers without regular expressions
def isPhoneNumber(text):
  if len(text) != 12:
    return False
  for i in range(0, 3):
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False
  for i in range(4, 7):
    if not text[i].isdecimal():
      return False
  if text[7] != '-':
    return False
  for i in range(8, 12):
    if not text[i].isdecimal():
      return False
  return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
# What if the phone number is inside a bigger string?
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
  chunk = message[i:i+12]
  if isPhoneNumber(chunk):
    print('Phone number found: ' + chunk)

# We are getting to a larger amount of code and we might want to handle
#  variations, like (408)879-0855 or with a space after the close )
# Let's try a regex, that's the short version of regular expression
# First we need to get the module
import re
# Then we make a regex object to match a phone number
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Then we use it and create a 'match object'
mo = phoneNumRegex.search('My number is 415-555-4242.')
# Then print the result
print('Phone number found: ' + mo.group())
# So what all happened there?
# First there is the regular expression string r'\d\d\d-\d\d\d-\d\d\d\d'
#  We use a 'raw' string with the r'', because we want all those backslashes
#  The 'd's mean a digit, so three digits, a dash, three more digits, another
#  dash and then four more digits.
# When we give this to re.compile it makes an object that can do that match
# When that object is used on another string, it will do the match and store
#  the results in a 'match object'
# Finally, using .group() on the match object returns the whole match.

# Regex can get very tricky. When working on something complicated it can
#  help to use an on-line, real-time testing tool, like https://pythex.org/
#  It also has a cheat-sheet you can use to see all your matching options

# We can also group our match into pieces. Like if we want the area code of
#  the phone number seperate from the rest
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(0)
# So now we can get the area code and phone number in one shot with groups()
areaCode, phoneNumber = mo.groups()
print('Area code is', areaCode, 'and the phone number is', phoneNumber)
# If you want to look for a special character, you need a '\'
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
areaCode, phoneNumber = mo.groups()
print('Area code is', areaCode, 'and the phone number is', phoneNumber)

# The '|' caracter is sometimes called the 'pipe'. In a regular expression
#  it works like an 'or'
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)
mo.group(0)

# Optional matching with '?'
# This will match if the is there or missing
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
# So this lets us match and return either Batman or Batwoman
# Another example using our phone number example. Sometime you can assume the
#  area code part and we only need the phone number (well, used to be true)
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()

# Matching zero or more with '*'
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman') # Match 0?
mo1.group() # Works
mo2 = batRegex.search('The Adventures of Batwoman') # Match 1?
mo2.group() # Works
mo3 = batRegex.search('The Adventures of Batwowowowoman') # Match more than 1
mo3.group() # Also works

# Matching one or more with '+'
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwoman') # Match 1?
mo2.group() # Works
mo3 = batRegex.search('The Adventures of Batwowowowoman') # Match more than 1
mo3.group() # Also works
mo1 = batRegex.search('The Adventures of Batman') # Match 0?
mo1 == None # Does not work

# Matching a specific number of times with '{x,y}'
# This is what we use to match at least x times, but not more than y times
haRegex = re.compile(r'(Ha){3}') # Match at least three
mo1 = haRegex.search('HaHaHa')
mo1.group() # Works
mo1 = haRegex.search('HaHa') # Does it work with <3?
mo1 != None # No
mo1 = haRegex.search('HaHaHaHa') # Does it work with >3?
mo1 != None # Yes
haRegex = re.compile(r'(Ha){3,5}') # Match three to five
mo1 = haRegex.search('HaHaHaHa') # Does it work with 4?
mo1.group() # Yep
# You can also do something similar to list slices by leaving out one of the
#  numbers
haRegex = re.compile(r'(Ha){3,}') # Same as 3 or more
haRegex = re.compile(r'(Ha){,3}') # Same as up to 3
mo1 = haRegex.search('HaHa') # Does it work with <3?
mo1.group() # Yep
# Wait, when we did the example with 4 'Ha's, why did it not just match 3 and
#  stop, since that is an option?
# By default, a regex does a 'greedy' match. Meaning it will match the most
#  that it possibly can. If you want to use the 'non-greedy' or 'lazy' version
#  you need to add a '?' after the curly braces
haRegex = re.compile(r'(Ha){3,5}?') # Match three to five, lazy style
mo1 = haRegex.search('HaHaHaHa') # What does our match look like this time?
mo1.group()
# This is a bit tricky now as '?' can mean two different things

# The .search() method that we have been using so far will return the first
#  match. What if we want all the matches? We can use .findall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# We get a list of the matches
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# We get a list of tuples

# Character classes
# We have used just the charater class \d which is a digit, but there are more:
# \D = not a digit
# \w = any 'word' charater: letter, digit or '_' (underscore)
# \W = not a 'word' charater
# \s = and 'space' charater: space, tab or newline/return
# \S = not a 'space' charater
# With help from these, a very difficult match can become much easier
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

# So the charater classes are pretty cool, but what if I need other ones?
# You can use '[]' (square brackets) to create your own
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# You can make a range using the '-' (hyphen)
# Like this is a 'word' charater, but without the '_': [a-zA-Z0-9]
# You can use a '^' (carrot) at the beginning to mean 'not'
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

# If a carrot is outside of the '[]' it means match at the beginning
# A '$' means match at the end
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
beginsWithHello.search('He said Hello.') != None
endsWithNumber = re.compile(r'\d$') # Ends with a number
endsWithNumber.search('Your number is 42')
# Wait, what if I wanted to match the whole number?
endsWithNumber = re.compile(r'\d+$')
endsWithNumber.search('Your number is 42')
# and for ensuring the entire string is numbers?
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
wholeStringIsNum.search('12345xyz67890') != None

# Use '.' (dot) to match one of anything
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# Use '.' with '*' (star) to find everything (0 or more) in that spot
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Elyse Last Name: Knuth')
print('Nice to meet you', ' '.join(mo.groups()))
# If we need a 'non-greedy'/'lazy' way to do this match, use '(.*?)'
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()
# and back to greedy
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()

# The shortcut way to match without careing about upper-case vs. lower-case
robocop = re.compile(r'robocop', re.IGNORECASE)
robocop.search('RoboCop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.').group()
robocop.search('Al, why does your book talk about robocop so much?').group()
# Note how the search and the group are on the same line now

# Regex can not just FIND, but also can REPLACE using .sub()
namesRegex = re.compile(r'Agent \w+')
# Let's say your a lawyer and don't want to leak clients' names
myRecords = 'Agent Alice gave the secret documents to Agent Bob.'
namesRegex.sub('CENSORED', myRecords)
# What if you need to use a match in the substitution. Use \1 , \2, \3 etc
agentNamesRegex = re.compile(r'Agent (\w)\w*')
myRecords = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob \
was a double agent.'
agentNamesRegex.sub(r'\1****', myRecords)


# Project
# Let's create mom a way to serch through a big pile of evidence and pull out
#  all the the phone numbers and emails

# Questions at the end of https://automatetheboringstuff.com/2e/chapter7/