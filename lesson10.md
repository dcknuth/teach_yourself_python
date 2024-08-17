# Python Lesson 10
Python has some nice modules to help you look at and organize your directories and files. This section takes a look at a couple of those. First let’s have a look at moving and copying
```
# shell utilities module
import shutil, os
from pathlib import Path

# a quick reminder of Path and home directory
p = Path.home()
print(p)
print(Path.cwd())

# make a file to test on
with open('spam.txt', 'w') as f:
    f.write('Some spam for my file')

shutil.copy(p / 'spam.txt', p / 'some_folder')
# This copied spam.txt to a file named some_folder
# This probably is not what we wanted, so let's delete that and try again
os.unlink('some_folder')
# This is a permenent delete, not a move to the recycler/trash
# We need a directory, so let's make one
os.mkdir('eggs')
# Let's copy to our new directory
shutil.copy(p / 'spam.txt', p / 'eggs')
shutil.move("eggs/spam.txt", "./")
# We already have a file with that name here, so we get an error
# Remove it
os.unlink('spam.txt')
shutil.move("eggs/spam.txt", "./")
# This time it worked. Also ./ is the current directory and ../ is the parent
# We can also rename with move, let's do that and put it back in the folder
shutil.move('spam.txt', 'eggs/ham.txt')
# To remove a directory we would use or.rmdir, but let's clean up this way
shutil.rmtree('eggs')
# That removed the eggs directory and everything inside it
# We used '/' for things. If you use '\' it would have to be C:\\Users\\dave
#  to work correctly
```
Let’s have a look at walking through a directory structure and a bit on file compression
```
# Let's use os.walk to look at the things in our home directory
home_dir = os.walk(Path.home())
# There seems to be no home_dir variable, but let's try to use it anyway
for name, folders, files in home_dir:
    print("name is", name)
    print("Folders are", folders)
    print("Files are")
# This seems to give us back everything in our home dir and subfolders
# We can turn off the "Exclude calables and modules" if we want to see
#  generators in the Variable Explorer. We also see modules like shutil
#  and imported classes like Path. If it gets too messy, turn it back off

# Working with ZIP files, to compress a file
import zipfile
# First we need a very compressable file. Let's generate one with lots of
#  the same cat names
with open("cat_names.txt", "w") as f:
    for x in range(10000):
        f.write("Garfield, Zophie, Tails, ")
    f.write("Garfield, Zophie, Tails.")
# Make a compressed zip file
exampleZip = zipfile.ZipFile('new.zip', 'w')
exampleZip.write("cat_names.txt", compress_type=zipfile.ZIP_DEFLATED)
exampleZip.close()
# Check the size
zip_file = zipfile.ZipFile('new.zip')
file_info = zip_file.getinfo('cat_names.txt')
print("Uncompressed size is", file_info.file_size, "bytes")
print("Compressed size is", file_info.compress_size, "bytes")
xsmaller = round(file_info.file_size / file_info.compress_size, 2)
print(f'Compressed file is {xsmaller}x smaller!')
# remember to close anything that is opened and ZipFile counts as an open
zip_file.close()
```
Finally, an example of when we might use some of this
```
# When might it be good to use this type of stuff?
# Instead of trying this with renames from American to European dates, let's
#  try going from filenames with American dates (the worst) to dates in
#  order of significance (the best, year-month-day)
# Let's make a directory and some files to test on
os.mkdir('test_logs')
log_names = ['log_12-01-2021.txt', 'log_12-14-2021.txt', 'log_01-05-2022.txt']
for name in log_names:
    with open('test_logs/' + name, 'w') as f:
        f.write("Very important logs for today!\n")
# Now that the test files are setup, let's try to rename them with good names
files = os.listdir('test_logs')
for file in files:
    # We probably want to test that each of these is the file we think it is
    parts = file.split('_')
    # This should give us exactly two parts with log as the first part
    if len(parts) == 2 and parts[0] == 'log':
        cur_date, file_type = parts[1].split('.')
        # It should be a text file
        if file_type == 'txt':
            # This should be one of our log files, so get the date parts
            month, day, year = cur_date.split('-')
            # We should now have everything we need to rename
            new_name = 'test_logs/' + f'log_{year}-{month}-{day}.txt'
            shutil.move('test_logs/' + file, new_name)
# Now a sort by filename also sorts by the log date
# We should clean up
shutil.rmtree('test_logs')
```
[Python Lesson 11 part1](lesson11p1.md) - Debugging