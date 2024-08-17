# Python Lesson 6
This one is all about strings. In addition to indented parts, select triple quoted strings that span lines before pressing F9.
```
# Class 6 - Working with strings

# Escape characters
# We already know how to get a single quote into a string, use double quotes
# We can also do this with an escape character '\'
x = 'Elyse\'s purse'
# \" Double quotes
# \t tab
# \n New line
# \\ Backslash
print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw strings use whatever is in the container character
y = r'\What\if\I\need\a\lot\of\backslashs'
# Multiline strings use triple single quotes '''
y = '''Hi!
Hello'''
print(y)

# We already know that you can work with a string similar to a list
print(y[:3])
# You can also search for sub-strings in a string with 'in'
'Elyse' in x
# We can also use some other ways of creating longer strings than '+'
# String interpolation with %s
name = 'Elyse'
age = 12
print('My name is %s and I am %s years old' %(name,age))
# Notice how the integer was converted to a string
# f-strings with {}
print(f'My name is {name} and I am {age} years old')

# Some useful string methods
# lower()
'apples' == 'Apples'
'apples'.lower() == 'Apples'.lower()
print('Hello World!'.upper())
# Note that these functions return a different string and don't change the
#  original string as strings are immutable
# You can test the properties of strings
'apples'.islower()
'apples'.isupper()
'123'.isalpha()
'123'.isalnum()
'123'.isnumeric()
'123'.isdecimal()
'123'.isdigit()
'elyse'.istitle()
# or change properties of strings
print('elyse'.title())

# When would these be useful
print('Enter your name: ', end='')
name = input().title()
print(f'Hi {name}. What is your age: ', end='')
while True:
  age = input()
  if age.isdigit():
    break
  else:
    print('Please enter a whole number for your age')
print(f'Name: {name}, Age: {age}')

# more...
'Hello World!'.startswith('Hello')
'Hello World!'.endswith('!')

# join and split
x = 'How many words are in this sentance?'
len(x.split())
x = ['one', 'two', 'three', 'four', 'five']
print(' '.join(x))
print(', '.join(x))
# These let us count words and sentences or process spreadsheets or get
#  data into them and lots of other stuff. You will use them often
# The partition method is like split, but keeps the item used to seperate
'Hello, world!'.partition('o')
# Try with multiple assignment
before, sep, after = 'Hello, world!'.partition('o')
print(before)

# Justify text. You can use rjust(), ljust() and center and they will pad
#  your string with the spaces needed
'Elyse'.center(20)
x = ['Elyse', 'is', 'Great']
for i in x:
  print(i.center(20))
for i in x:
  print(i.rjust(20))
# We can also use other characters instead of space
for i in x:
  print(i.center(20,'='))
# This would be useful if we need to print lots of data in nice groups
#  Like maybe for a picnic
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# Dealing with extra white space, sometimes you just want the data
spam = '    Hello, World    '
spam.strip()
spam.lstrip()
spam.rstrip()
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')

# Letters are really numbers
ord('A')
ord('B')
ord('a')
ord('!')
chr(65)
ord('A') < ord('B')
chr(ord('A') + 1)

# Questions at the bottom https://automatetheboringstuff.com/2e/chapter6/
# Try the first table printer project
```
[Python Lesson 7](lesson07.md) - regular expressions