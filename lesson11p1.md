# Python Lesson 11 Part 1
As your programs get more complicated, you will probably need to add some things to your programs and learn how to use some new tools to make debugging easier. There is enough to this that we will just look at the adding in items to start. One that we have already seen is the try/except code block. As a quick reminder, it looks like this:
```
def MyDiv(dividBy):
    try:
        return 42 / dividBy
    except ZeroDivisionError: # to catch all errors, use just except:
        print('Error: Bad argument')

MyDiv(0)
```
These are very helpful in cases where you know there is the possibility of an error so you can raise it and say what happened instead of the program just not working. You can raise your own exceptions in addition to just catching ones from other functions.
```
# Let's raise our own exception
raise Exception('This is the error message.')
# This tells us we had an error and gives a traceback
# If there is no try/except, the program just crashes

# Usage is often that a function raises the exception and that the
#  surrounding code catches it. Let's redo MyDiv to be like this
def MyDiv(dividBy):
    if dividBy == 0:
        raise Exception('One cannot divide by zero')
    else:
        return 42 / dividBy

try:
    MyDiv(0)
except Exception as err:
    print("The error was:", err)
```
We can also use assertions to check if things are going as we planned.
```
# Assertions are another way to check that things are proceeding according
#  to plan
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
# No assertion error
assert ages[0] <= ages[-1]
ages.sort(reverse=True)
# Assertion error
assert ages[0] <= ages[-1]
# Usually, use assertions when you want the program to crash and use
#  raise plus try-catch when you want to work around a possible
#  issue and keep the program running

# Let's try another assertion example, a traffic light
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    #assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)
# The code does not crash, but does lead the the dangourous state where
#  neither direction is red; not good. Let's uncomment the assertion
#  and rerun (remember to reset the lights also)
```
Logging can also help us figure out what went wrong with a program. For simple programs you are running at the command line or interpreter, just using print is easy and effective. For more complex things where you want an easy way to shut off some logging and to log to a file, there is the logging module.
```
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname) s -  %(message)s')
# A factorial function
def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total


logging.debug('About to run function')
print(factorial(5))
logging.debug('Just ran the function')
# With the logging, we can see where things are going wrong
# Let's fix and rerun

# You can disable all the printing coming from the logging calls with...
logging.disable(logging.CRITICAL)
logging.debug("test")
# Disabling logging is one-way and is meant to apply when you no
#  longer want to do logging to the whole file (there is no enable)
# To configure printing to a file
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')
# This would have to replace the logging config line above
```
A last tip for this part of debugging is how to turn on variable values in the console. From the console, use %xmode Verbose to turn this on.
```
def func1(a, b):
    return a / b

def func2(x):
    a = x
    b = x - 1
    return func1(a, b)
# Try with the default: %xmode Plain and then setting %xmode Verbose
func2(1)
```
[Python Lesson 11p2](lesson11p2.md) - more debugging