# Boolean values are True or False
1 == 1 # True
1 == 2 # False
# Other comparison operators
1 != 2 # not equal to
1 < 2  # less than
2 > 1  # greater than
2 >= 2 # greater than or equal to

# Watch out for comparing things of different types
'2' == 2 # False
int('2') == 2 #True

# More boolean operators
True and True # If both are True, True
True or False # If one is True, True
not False     # Reverse the bool value

# You can also string these together
(2 > 1) and (5 == 5)

# Now we can use boolean values to control our code
# Python uses indentation level to create a 'block' of code
# Let's set up some variables and try it
name = 'Elyse'
password = 'esylE'
print('Hi ' + name + ', enter your password:')
pw = input()
if pw == password:
  print('Access granted')
else:
  print('You are not ' + name + '! Intruder alert!')

# If the bool is true, do the block of code. If not, do the 'else' block

# 'if', is a flow control statement that can be optionally paired with 'else'
# It can also be paired with 'elif' (else if) to pair more than two tests
e = 12
c = 15
m = 41
d = 46
age = 41
if age <= e:
  print('Hi Elyse')
elif age <= c:
  print('Hi Chase')
elif age <= m:
  print('Hi Merissa')
else:
  print('Hi Dave')

# There are other control statements
spam = 5
i = 0
while i < 5:
  print('Hello world!')
  i += 1         # Sneaking in a new operator. += is the same as i = i + 1

# 'break' can be used to get out of a block of code
while True:
  print("Type: 'your name'")
  x = input()
  if x == 'your name':
    break  # this does not break out of the 'if' but whatever is outside that
print('Thanks for typeing your name')
# note that our print has to be two levels back

# 'continue' is another control statement that brings you back to the top
#  of the current loop
# Also 0 or 0.0 counts as False and other values will count as True
#  However, try not to use these directly. Use something like a == 0 instead

# The for loop
# For loops have the keyword 'for', then a variable, then the keyword 'in'
#  and then a list. It will evaluate the code block with each item in the list
for i in [1, 2, 3, 4, 5]:
  print((str(i) + ' ') * i)

# The range function
# Python has a neat built in function to give you a list to operate on
range(5)
# As you can see, it only creates an object until you do something with it
print(str(list(range(5))))
# Now we can see that range will feed numbers starting with 0 and stopping
#  one short of the number indicated
print(str(list(range(1,6))))
# With this format of range, we now get the same list as we used with for
for i in range(1,6):
  print((str(i) + ' ') * i)
# For this small example, it seems about the same. What if we wanted to print
#  the even numbers to 100? That would be a long list, so...
for i in range(2,101,2):
  print(str(i))
# We didn't have to make a long list, range did it for us. That third
#  parameter of the range function is the 'step'
# Let's add all the numbers from 0 to 100
x = 0
for i in range(101):
  x += i
print(str(x))
# Python uses this loop style frequently and the range step can be negative
for i in range(5,0,-1):
  print(str(i))
print('Launch')

# Modules are cool
# There are tons of modules for Python and you can probably find one that
#  helps you to do the thing you want to do. Let's test on the random module
import random
# Now roll me six d20s for a new D&D character
for i in range(6):
  print(random.randint(1,20))

# Let's write our first game! Guess what number I'm thinking
secretNumber = random.randint(1,10)
print("I'm thinking of a number between 1 and 10")
while True:
  print('Take a guess')
  myGuess = int(input())
  if myGuess == secretNumber:
    break
print('You guessed it!')

# Can we rewrite this to give high/low hints?

# Should we write a whole rock, paper, scissors game?

# Questions at the bottom of https://automatetheboringstuff.com/2e/chapter2/
