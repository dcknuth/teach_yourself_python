# Python Lesson 9
Reading and Writing files

We can use variables while a program is running, but to keep something after we are done or take input we might want to do that with files. Files have a name and a path. An example for Windows would be:

C:\Users\dave\Documents\test.txt

Python will usually handle doing the right thing no matter which slash you use, so I will go with '/' since we will not have to deal with the escape use of '\\'. We will also assume everything we will be doing is for text files and not cover binary files here. Last thing to mention here is about the "working directory". If you don’t use a full path and only include a file name, it will read or write to the directory you run the Python program from or, if you are using an IDE, from whatever that program sets the working directory to be.
```
# OK, let's write to a file
# Set our file path
path = 'C:/Users/Dave/Documents/test.txt'
# Set the text we will write with triple quotes
sonnet = '''When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,'''
# Open a file for writing
myFile = open(path, 'w')
# Write to the file
myFile.write(sonnet)
# Close the file
myFile.close()

# In almost the same way, we can read the file back in. However, let's do it
#  line by line, which is one of the most common ways to get data into Python
myFile = open(path)
while(True):
  curLine = myFile.readline()
  if not curLine:
    break
  else:
    print(curLine)
myFile.close()
```
Pretty easy, but why the extra, empty lines? Well, each line we read in from the file has a newline and then the print() function adds another one at the end by default. We could fix this by telling the print statement not to add the newline or by stripping off the newline before printing. For completeness, let’s try the second method.
```
# Let's do that again in an even more common way and fix the double newlines
with open(path) as myFile:
  curLine = myFile.readline()
  while curLine:
    print(curLine.strip())
    curLine = myFile.readline()
# In this case, we don't need to close the file, as it will do that for us at
#  the end of with:
```
What if we want to do a little more with the file system and with file paths?
```
# Let's create a directory
import os
os.makedirs('C:/Users/Dave/Documents/temp')
# We can also make several directories in a path
os.makedirs('C:/Users/Dave/Documents/temp/delicious/walnut/waffles')
# List all the files in a directory
os.listdir('C:/Users/Dave/Documents/temp')
# Another, newer path module
from pathlib import Path
# This type of import allows us to use just the object name alone without
#  the module name
# Let's print the current working directory
Path.cwd()
# Using Path we can get the parts of a file path easily
p = Path('C:/Users/Dave/Documents/test.txt')
print("First part is the anchor:", p.anchor)
print("To get the containing directory as a Path object:", p.parent)
print("The name of the file", p.name)
print("Name without extention:", p.stem)
print("Just the file extention:", p.suffix)
print("Just the drive letter:", p.drive)
```
What about checking if files or directories exist to either prevent overwriting files or to prevent errors from ending our program?
```
# Let's check if a file exists
winDir = Path('C:/Windows')
notADirectory = Path('C:/This/Folder/Does/Not/Exist')
ourFile = Path('C:/Users/Dave/Documents/test.txt')
winDir.exists()
winDir.is_dir()
notADirectory.exists()
ourFile.is_file()
ourFile.is_dir()
```
When reading and writing files as we did at the start, we can either use a string or a Path to do so. So we now know how to read and write files with some text, but what if we would like to save our program variables to maybe read in later or send to another Python program?
```
# What about saving variables?
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
# Under the hood, this will create three files to do the storage on a
#  Windows system and one file on a Mac
# Let's clear the list of cats
cats = []
print(cats)
# Now read them back in, but let's use 'with' so we can't forget to close
with shelve.open('mydata') as shelfFile:
    cats = shelfFile['cats']
# Now check if we have our cats back
print(cats)
```
This will be helpful to save variables that are not easy to just print as text strings, but what if we want to be able to look inside the files easily. Since shelve will store the data as a binary file, let’s look at another option we have to save our variables that is easier to inspect, as a python script.
```
# Now let's try storing some data as a Python file
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
with open('myCats.py', 'w') as fw:
    fw.write('cats = ' + pprint.pformat(cats) + '\n')
# Clear cats
cats = []
# Now let's pull them back in
import myCats
print(myCats.cats)
# and if we wanted just cats?
from myCats import cats
print(cats)
```
This is pretty neat and we can look into the myCats.py file to see what is there. It is probably more common to use either shelve or to export to a JSON file (which we will get to later) as it is also in readable plain-text, compatible with other Python modules and other programming languages and systems.

[Python Lesson 10](lesson10.md) - Organizing Files