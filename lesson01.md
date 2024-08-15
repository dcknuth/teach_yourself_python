# Python Lesson 1
You should have the Python Spider IDE or interpreter of your choice open and be ready to type items from the next section into a file. If not, get Spider, IDLE, Jupiter or another interpreter running first. If you use something like VS Code, I would just keep running the whole file as you go and ignore the repeated parts. Type (or copy) each section to try it out. You put the code below in the file editor on the left side and then look in the lower right to see the results of running each line (the environment window)
```
# https://automatetheboringstuff.com/ as inspiration
# Our first python class

# We can run a single line
# Click on the line and press F9 (for Spider)
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
```
In the upper right section of the Spider IDE, you can click on the Variable Explorer tab to see all the variables in your current environment. There should already be a couple there. In the next section, each time something is run and you don’t get the prompt back in the environment window (lower, right), it means you will need to select that window and enter your information and the <Enter> key. Do this after running each line with "input()". You should get the prompt (something like "In [16]:") back each time you press the <Enter> key. To run the next line of code, click on that line on the left side and press <F9>.
```
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
```
At the end of most of these, we can choose some questions to do from the on-line book and put in some lines to test out our answers.
```
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
```
Live in the class, we will work a problem from one of the coding challenge sites. Don’t worry if we need some things we have not learned yet. We will work these together to start. They will only be listed here on the page until we have an example from each of the sites we will get questions/puzzles from. Here’s a question from [codewars.com](https://codewars.com/). We are supposed to write the high_and_low function
```
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
```
[Python Lesson 2](lesson02.md)