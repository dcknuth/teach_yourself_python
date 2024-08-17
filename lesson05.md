# Python Lesson 5
Next to lists, dictionaries are the next most common data structure in Python. They are very useful anywhere you need to relate a key and a value and are very fast at doing it. Remember to select whole indented sections before pressing F9.
```
# Chapter 5 Dictionaries
# Dictionaries can be created with colon separated pairs in curly braces
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# There are 'keys' on the left and 'values' on the right
# You access the values by using the keys
myCat['size']
'My cat has ' + myCat['color'] + ' fur.'
# Keys can be strings or integers or other un-mutable types, like tuples
spam = {12345: 'Luggage Combination', 42: 'The Answer'}
# Dictionaries are unordered, making them different from lists, which are
#  ordered. So, dictionaries can't use an index like spam[0], only a key.
# If you try to use a non-existent key, you will get a key error
spam = {'name': 'Zophie', 'age': 7}
spam['color']
# You can use the keyword 'in' to test if a key is in a dictionary
'color' in spam
'name' in spam

# Dictionary example
birthdays = {'dad': 'July 8', 'Chase': 'June 18', 'mom': 'February 14'}
while True:
  print('Enter a name: (blank to quit)')
  name = input()
  if name == '':
    break
  if name in birthdays:
    print(birthdays[name] + ' is the birthday of ' + name)
  else:
    print('I do not have birthday information for ' + name)
    print('What is their birthday?')
    bday = input()
    birthdays[name] = bday
    print('Birthday database updated.')
    
# Dictionaries have some special methods to help you work with them. keys()
#  will give you a list of the keys, values() will give a list of values and
#  items() will give you a list of key:value pairs
for v in spam.values():
  print(v)
  
for i in spam.items():
  print(i)

# These methods return tuples if you want a list instead
list(spam.keys())

# Use the method get() to return the value if the key exists and return
#  another value if it does not
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
# Similarly setdefault() will set a value for the key only if the key is not
#  already in the dictionary
picnicItems.setdefault('eggs', 1)
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
# Let count the number of times letters occur in a string
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# Make an empty dictionary
count = {}
for character in message:
  count.setdefault(character, 0) # If we have not seen this letter yet set at 0
  count[character] = count[character] + 1 # add 1 to our count
print(count)
# Nicer printing of dictionaries
import pprint
pprint.pprint(count)
# If you want to save a string of the nicer print use pformat()
myPretty = pprint.pformat(count)

# Let's make a tic-tac-toe game in another file
# Will be posted after this one

# A more complex example of dictionaries in dictionaries
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
  numBrought = 0
  for k, v in guests.items():
    numBrought = numBrought + v.get(item, 0)
  return numBrought

print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

# Do the questions at the end of https://automatetheboringstuff.com/2e/chapter5/
# Note on dictionaries and speed of a program
# https://medium.com/@randerson112358/algorithm-analysis-time-complexity-simplified-cd39a81fec71
```
The tic-tac-toe game will be at the end, but there are a couple more things about dictionaries that I would now add on to a lesson about them. Mainly a couple useful functions and a module with some dictionary extensions.
```
# There is a common case where you need a default for your dictionary
from collections import defaultdict
# Luckily, there is the collections module to help
# I use this most when the value needs to be a list and I am appending
# In order to append, the list needs to be there already
# Just tell defaultdict what type you need
animals = defaultdict(list)
# An empty list will then be there for us when we need it
animals["Cats"].append("Tails")
animals["Cats"].append("Fluffy")
animals["Dogs"].append("Lacey")
animals["Dogs"].append("Spot")
animals["Dogs"].append("Hunter")
# The first of each entry into cats and dogs would have given an error without
#  the default empty list
print(animals)

# The other thing that comes up a lot is counting, for which there is
#  another dictionary class (though we could use defaultdict with int)
from collections import Counter
num_animals = Counter()
# A Counter dictionary already has a default of 0
for animal_type in animals.keys():
    for animal in animals[animal_type]:
        num_animals[animal_type] += 1
print(num_animals)

# Last all the dictionaries have a function to give you max value in the dict
num_animals.most_common(1)
# The '1' says we only want the top key value pair, by the value
```
And here is the (lame) tic-tac-toe game. You have to fill in the game matrix with marks for player 1 or 2 and then run the function to see who won. Below it is set such that player 1 wins in the top row. Yes, nothing to do with dictionaries, but the lesson was short and I needed to keep my daughter entertained.
```
game = [[1,1,1],
        [2,2,1],
        [1,2,2]]

def whoWon(g):
    '''Return the player that won or 0'''
    # Test rows
    for r in g:
        if r[0] == r[1] and r[1] == r[2]:
            return(r[0])
    # Test columns
    for i in range(len(g)):
        if g[0][i] == g[1][i] and g[1][i] == g[2][i]:
            return(g[0][i])
    # Test diagonals
    if g[0][0] == g[1][1] and g[1][1] == g[2][2]:
        return(g[1][1])
    if g[0][2] == g[1][1] and g[1][1] == g[2][0]:
        return(g[1][1])
    return(0)

print(whoWon(game))
```
[Python Lesson 6](lesson06.md)