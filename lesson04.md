# Python Lesson 4
Lists, tuples, mutable vs. immutable and how to see the Python object ID. Lists are a huge part of Python, so this is a longer lesson. Remember, for indented sections, select the whole section and then press F9.
```
# Lists and Tuples
# We have already seen lists when we looked at the for loop and range function
spam = ['cat', 'bat', 'rat', 'elephant']
# Now we will learn a little more. Like, you can access each individual item
#  with sqare brackets and a number
print("first item is", spam[0])
print("Third item is", spam[2])
print("Last item is", spam[len(spam)-1])
# You can see that access is 'zero based' meaning the first item is at the
#  zero position and the last item will be in the length-1 position
#  If we forget the -1 we will get an error
print("Last item is", spam[len(spam)])
# There is also another way to get to the end of a list, negative indexes
print("This is also the last item in the list:", spam[-1])
print("First item is", spam[-4])
# Note that negative indexes start at -1

# You can also have lists of lists
myMatrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]
# Which you then access with two indexes, a row and a column
print("The one", myMatrix[0][0])
print("The six", myMatrix[1][2])
# You can also mix types
myList = [spam, myMatrix[1]]

# A way to get a list that is a part of another list is with a 'slice'
print(spam[1:3])
# Notice that this works like the range function and goes 'up to' 3, but
#  does not include that index
# You can still use negative indexs
print(spam[1:-1])
# and you can leave out one side to go to that end of the list on that side
print(spam[:2])
print(spam[2:])
# You can also change an element of a list
spam[1]='batmonkey'

# You can combine lists in a sililar way to strings with + and *
print(spam + spam)
print(spam * 10)
# You can delete an item from a list with the keyword 'del'
del spam[1]
# OR we could have used the method 'remove', spam.remove('bat'). Note that
#  this way uses the item and not an index
# Now what if we wanted to put 'bat' back? We can use the insert method
spam.insert(1, 'bat')
# There is also an 'append' method that will always put the new item at
#  the end of the list

# Wait, what is the difference between a keyword, function and method
#  A keyword is a special, reserved word in the Python language
#  A function starts with the function name, like print()
#  A method acts on an object, like spam.append() with the object listed first

# Lists make many coding tasks easier and more flexable
# This loop let's you enter cat names and prints them out
catNames = []
while True:
  print('Enter the name of cat ' + str(len(catNames) + 1) +
    ' (Or enter nothing to stop.):')
  name = input()
  if name == '':
    break
  catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
  print('  ' + name)
# Think how hard that would be without lists

# The last example used 'name in catNames' to feed the for loop, but the
#  range function also works quite nicely
for x in range(len(catNames)):
  print('Cat', x+1, 'is', catNames[x])
# Notice this is nice when we need both the index and the list item. Also
#  notice the different ways we used the print function and '+'
# There is also another way to do this with the 'enumerate' function
for x, name in enumerate(catNames):
  print('Cat', x+1, 'is', name)
# It will return two things, the index and then the item in that position

# The 'in' and 'not' operators and the index function
# We just used 'in' to get each item of a list, but we can also use it to
#  see if an item is in the list
'Kitty' in catNames
# We can add 'not' to see if the thing is not in the list
'Kitty' not in catNames
# If we need to know the index of an an item in a list, we can use the index
#  function and provide it the item to look for (you need to replace 'e' with
#  the name of one of your cats)
catNames.index('e')

# You can also assign the item in a list to singe varibles at once. This is
#  called unpacking
spam = [1, 2, 3]
x,y,z = spam
# The number of variables and the length of the list need to match or you will
#  get an error
firstCat, remainingCats = catNames
  
# random.choice and random.shuffle
# When we did our number guessing game we had randint choose a number.
# We can use random.choice to choose from a list
import random
random.choice(catNames)
# We can also randomize the order of a list
random.shuffle(catNames)
print(catNames)
# Notice that it did not give us a new list, but shuffled the current list.
#  This is called an 'in place' operation
# What if we want to get it back in order? We can use the sort method
catNames.sort()
print(catNames)
# Notice that this was also in 'in place' operation
# We can reverse the order
catNames.sort(reverse=True)
print(catNames)
# This sort is not alphabetical, it is ASCIIbetical
catNames.append('Z')
catNames.sort()
print(catNames)
# All capital letters come before all lowercase letters
# What if we really need alphabetical? We can pass in a 'key' function
catNames.sort(key=str.lower)
print(catNames)
# The key function will change the case to lower before it is compared for
#  position
# If you want to reverse the order of the list, but not sort it use reverse()
catNames.reverse()
print(catNames)

# Strings can be treated as lists of letters. So all these are OK:
x = "Elyse Knuth"
'E' in x
'Knuth' in x
x[:5]
for i in x:
  print(i)


# Mutable and Immutable data types
# Mutable data types can be changed, Immutable data types cannot be changed
# This is OK in a list
catNames[0] = 't'
# but not for a string
x[4] = 'A'
# because the string type is immutable, you can't change it after creating it
# However, you can make a new string and assign it to the old name
x = x[:4] + 'A' + x[5:]
print(x)

# There is also an immutable list type. It is called a 'tuple'
x = (5,4,3,2,1)
print(x)
x[0] = 1
# Note that it is immutable like a string and that we use '()' to create it
#  instead of square brackets
# If you need a tuple with just one value, use a trailing comma
x = (1,)
type (x)
x = (1)
type (x)
# You can easily convert lists to tuples and tuples to lists if you need to
type(catNames)
catNames = tuple(catNames)
type(catNames)
catNames = list(catNames)
type(catNames)

# Magic 8 ball again with lists
import random
# Make a list of responces
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
# Then just use a single print line
print(messages[random.randint(0, len(messages) - 1)])


# Explaining 'reference' variables
# Whiteboard variables (Whiteboard here meant that we drew these out to help
#  see how things were stored by the computer)
spam = 42
cheeze = spam
spam = 100
print(cheeze)
# Now Whiteboard a list
spam = [0,1,2]
cheeze = spam
spam[1] = "Hello World!"
print(cheeze)
# So if all variables just 'reference' a point in memory, can we see that tag?
id(spam)
id(cheeze)
# Let's try the other test again
spam = 42
cheeze = spam
id(spam)
id(cheeze)
spam = 100
id(spam)
# Using a reference is also how 'in place' functions can work
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# What if I don't want a reference, but a copy that will not change the
#  original?
# For that, we can use the copy module
import copy
id(spam)
cheeze = copy.copy(spam)
id(cheeze)
# spam and cheeze point to different lists
# So if you change something in list cheeze
cheeze[3] = 4
print(spam) # spam stays the same
print(cheeze) # only cheeze changes
# There is a special case to know about. If we have a list of lists
#  then we need to use deepcopy()

# Game of Life demo and code walkthrough

# Questions from bottom of https://automatetheboringstuff.com/2e/chapter4/
```
You can optionally do some of the questions from the link at the end. Below is the Game of Life demo that uses most of what has been learned so far and is kinda neat. You can put it in a new file, run it with F5 and then stop it with <Ctrl> + c in the console window.
```
# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering
```
[Python Lesson 5](lesson05.md)