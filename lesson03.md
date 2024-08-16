# Python Lesson 3
This lesson will cover functions and minor error handling. The whole function definition block should be selected when pressing F9 to run it.
```
# We have used a couple of functions, like len(), input() and range()
# We can also write our own functions with the keyword 'def'
# Let's try it
def Hello():
  print('Howdy!')
  print('Howdy partner!!!')
  print('Hello there')
# Then use it like any other function
Hello()
# We use functions so we don't have to copy and paste a bunch of code. We also
#  use them to do the same thing on a different bit of data
def Hello(name):
  print('Hello ' + name)

Hello('Elyse')
# Is our other function with no parameters still there?
Hello()
# Nope

# Functions can also return values. Python does this with the keyword return
# Let's make a magic 8 ball to try it
from random import randint
def Shake8Ball():
  x = randint(1,9)
  if x==1:
    return 'It is certain'
  elif x==2:
    return 'It is decidedly so'
  elif x==3:
    return 'Yes'
  elif x==4:
    return 'Reply hazy try again'
  elif x==5:
    return 'Ask again later'
  elif x==6:
    return 'Probably not'
  elif x==7:
    return 'My reply is no'
  elif x==8:
    return 'Outlook not so good'
  else:
    return 'Very doubtful'
  
# Try this a couple times
Shake8Ball()


# The 'None' value
# Called null in other languages, it is the value when there is not a value
# The print function returns a None value, so we can do a quick test to show
#  None
x = print('printing...')
x == None # This will be true


# Keyword arguments to functions
# We have seen and used positional arguments with functions like range.
#  We can also set an arguement to a function using a keyword.
# Select both lines and run with F9
print('Hello', end=' ')
print('World')
# Here we use the named parameter 'end' to use a space at the end of the print
#  command instead of the newline. The default seperator for print is a space
print('dogs', 'cats', 'mice')
# We change change that with the keyword argument 'sep'
print('dogs', 'cats', 'mice', sep=' chase ')


# Global and local 'scope'
myScope = 1 # This is in global scope and can be used everywhere
def foo():
  myScope = 2 # This is in local scope and can only be used in the function
  localX = 3
  print('myScope: ' + str(myScope))
  print('localX: ' + str(localX))
foo()  
# Trying to use localScope here will give an error
print('localX: ' + str(localX))
# Using global variables should only be done when you are writing something
#  very small or when you really need to. I like to put my globals in
#  ALL_CAPITALS so that I know when I am using a global
# Finally, you can assign a value to a global variable, but you have to use
#  the keyword 'gloabl' so that Python knows you don't want to just make a
#  local variable


# Try/except code blocks
# Sometimes we want to do something that in some cases, might cause an error.
#  If we don't want to program to stop, we can put that code in a 'try'
#  block. Then we can put an error message or something else to use in the
#  'except' block
def MyDiv(dividBy):
  try:
    return 42 / dividBy
  except ZeroDivisionError: # to catch all errors, use just except:
    print('Error: Bad argument')

MyDiv(7)
MyDiv(2)
MyDiv(0)
MyDiv(1)
```
If you want, pick some of the questions to try at: https://automatetheboringstuff.com/2e/chapter3/

[Python Lesson 4](lesson04.md)