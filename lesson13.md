# Python Lesson 13
Time and dates, Scheduling tasks and Launching Programs

Time can mean a few things when programming, including how long your program runs, what day it is, task scheduling, giving a little time for something else to happen or for the user to see something and others. There are included modules to help with some of those, aptly named, time and datetime.
```
# Let's see some of what the time module can do
import time

# What is time?
t = time.time()
print(t)
# What is that number?
# It is the number of 'ticks' from the 'epoch' converted to seconds,
#  and a curiosity of computer science. A 'tick' could be a thousanth
#  or a millionth of a second depending on your computer.
#  The epoch is 12AM January 1st, 1970 at UTC/GMT/Coordinated Universal
#  Time/Grenwitch Mean Time/Global Mean Time
# For our first use of time, let's find a rough run time of computing the
#  factorial of 1,000 (we will want to select everything with the two
#  times and run it together)
# Start time
t1 = time.time()
ans = 1
for i in range(1, 1001):
    ans *= i
t2 = time.time()
print("Factorial is", ans, "and it took", t2 - t1, "seconds")
# So... Computers are fast and Python can deal with arbitrarily large
#  integers
# There are other ways that can do more refined run-time measures,
#  but this is usually OK for things that make a big difference and
#  take a little while

# What about a human readable time instead of ticks?
t = time.ctime()
print(t)
# This might be good for a readable timestamp or to use in a filename

# What if we just need to wait a bit before doing the next thing
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

# How about a bit more flexible time for a date and time stamp?
import datetime
now = datetime.datetime.now()
print(now)
# This gets us a date and time that matches our local time
# With this object we can easily get the part we want
print("Year =", now.year, "Month =", now.month, "Day =", now.day)
# You can also take a Unix timestamp from time and make it a datetime
fromUnixTime = datetime.datetime.fromtimestamp(time.time())
# You can do operations between datetimes
fromUnixTime - now
# Subtracting gets us this nice timedelta object that tells us how
#  far apart the two datetimes are
# We can make a timedelta and add it to get a future (or past) time
forward = datetime.timedelta(hours=2)
setAlarm = now + forward
print(setAlarm)
# We can also do some conversion operations by function
forward.total_seconds()
# Using datetime like this makes things very readable
futureDate = datetime.datetime.now() + datetime.timedelta(days=1000)
print(futureDate)
# If you don't like the format the date is in when you print by default
#  you can use strftime() using a common formating lauguage
futureDate.strftime('%Y/%m/%d %A %I:%M:%S%p')
# Good to get the format you like or need to feed to another program
# You can also go the other way and get a date string you are given
#  and get it to a datetime object
inputDate = 'October 21, 2019, at 4:29 PM'
dtDate = datetime.datetime.strptime(inputDate, '%B %d, %Y, at %I:%M %p')
print(dtDate)
```
We are not going to go into multithreading via module as it is not really a Python strong suit and has many issues even if it were Python-friendly. However, we will see how to run an external program. That will let us give work to other programs that are already fast and multi-threaded (modules often do this for us too). Together with what is above, we can schedule programs and ship work to be done externally. So how do we run another program from Python?
```
# Easiest way
import subprocess
# Waits for return value
cmd = 'notepad'
subprocess.run(cmd)
print("Back to Python")
```
To run just one thing and wait until it is finished, you can use subprocess.run(). Usually, if you provide more information, you will have better luck. For instance, “notepad” is in the default path and we seem to be getting some help to know that it really means “notepad.exe”. It would produce a more stable result to use something like “C:\\Windows\\System32\\notepad.exe” as the command. Let’s try Popen() which does not wait by default.
```
# Make a Python program to sleep for 10 seconds
with open("sleep10.py", 'w') as f:
    f.write("import time\ntime.sleep(10)\nprint('Waking up')\n")

# Don't wait for return
cmd = r'C:\Users\dave\AppData\Local\Programs\Python\Python39\python.exe'
script = "sleep10.py"
arg_list = [cmd, script]
print(*arg_list)
subprocess.Popen(arg_list)
print("Back to Python")

# Wait for it, just to see if it is sleeping
subprocess.run(arg_list)
# No print shows for us from the sub-process
subprocess.run(arg_list, capture_output=True)
# Now we get output as part of the return value
```
Here we created a simple Python program to sleep for 10 seconds, then ran it with Popen, which continued to the print function right away. One should use run() for its simplicity if it works for your case. If it gives you trouble, or you want an immediate return to the program that called it, you should use Popen(). You should also be ready to provide full paths to everything and to study the docs for Popen() to get exactly what works for what you need to do. If the program you are going to run has any meaningful chance of an error, you will want to capture the returncode and handle errors as needed. Instead of going through more examples now, we are going to use this a lot in the next lesson.

[Python Lesson14 Part 1](lesson14p1.md) - Image manipulation