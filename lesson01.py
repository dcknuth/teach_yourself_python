# https://automatetheboringstuff.com/ as inspiration
# Our first python class

# We can run a single line
# Click on the line and press F9
2+2
# When we press F9 it will run only that line or the highlighted section

# Click on the first line below and then press F9
# That will bring you to the next line and you can keep pressing F9
# all the normal math operators
1+1
2-1
5*5
7/3

# more interesting math operators
# exponent: x to the power of y
2**10
# modulus: if x is divided by y, what is the remainder
9%4
# floor division: if x is divided by y, what is the part before the decimal
#  OR what is the part without the remainder
9//4


# Data types
# Integers
-2
0
2
# Floating point
1.5
0.234
# Strings
'Dave'
"Elyse"

# You have already seen what Python will do when you add numbers
# What does it do when you add strings?
"Elyse" + " " + "Knuth"
# What if you multiply a string?
"Elyse " * 50
# Can we multiply a string by a Float?
"Elyse " * 5.0
# No, we can't
# But sometimes, we can use a function to change one type into another
1 + int('1')
1 + '1'

# Storing values in variables, like x and y
# Anything you set to the left of '=' becomes a variable
x = 2
Elyse = 12
# Variables are case sensitive
elyse = 5

Elyse

# Good variables can be letters, numbers and '_', but can't
#  start with a number
# If you can do an operation on the type, you can do it on a
#  variable of that type
elyse + x

# It is nice to be consistant with your variable style. Let's use
# camel case: elyseKnuth for regular variables
# this is snake case: elyse_knuth
# and this is pascal case: ElyseKnuth

# First Program!
# This program says hello and asks for my name
print('Hello world!')
print('What is your name?') # Ask for your name
myName = input()
print("It's good to meet you " + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

# Questions
# Do from the bottom of https://automatetheboringstuff.com/2e/chapter1/

bacon = 20
bacon + 1
bacon = bacon + 1
bacon
'spam' + 'spamspam'
'spam' * 3
float(4)
float('4.4321')
'I have eaten ' + 99 + ' burritos.'
'I have eaten ' + str(99) + ' burritos.'

# In this little assignment you are given a string of space separated
#  numbers, and have to return the highest and lowest number.

# Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and
#  highest number is first.
