# Python Lesson 14 Part 2
Now we are going to try some image operations in parallel on a number of images. This is common to format for a web site or if you want to apply a style to a bunch of pictures. To get some more interesting images to work on, grab [this zip file](pclass/sample_picts.zip) full of images from Unsplash (the images here usually can be used without a fee, at least for our educational purpose here.) I’m going to assume we put the zip file in a directory called “unsplash” inside a “pclass” directory. First we are going to unzip the file, clean up and get a pipeline to work on a single image.
```
# Same path as used in the last lesson
magick = r'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe'
# Set directory with photos
imgDir = 'C:/Users/dave/pclass/unsplash'

pictsZip = 'sample_picts.zip'
# change to the directory we are going to work in
import os
os.chdir(imgDir)
# unzip the images
import zipfile
picts = zipfile.ZipFile(pictsZip)
picts.extractall()
picts.close()
os.unlink(pictsZip)

# on just one picture
# resize, then increase contrast, then save as webp
targetDir = '1080_high_contrast'
os.mkdir(targetDir)
imgIn = 'david-ford-dwAPgmdGlfA-unsplash.jpg'
args = ['convert', imgIn, '-resize', 'x1080', '-brightness-contrast',
        '0x20']
imgOut = targetDir + '/' + imgIn.split('.')[0] + '.webp'
# make our command
cmd = [magick] + args + [imgOut]
from subprocess import run
process = run(cmd, capture_output=True, universal_newlines=True)
```
This got us our images to work on, deleted the zip, created a directory for output images and did a resize plus contrast enhancement on one image, then saved the image as a webp file inside the target directory. Not bad, but we should clean up a few things. Instead of running line-by-line, let’s make an actual Python module with a function that includes inputs for the filename and output directory. Let’s check for the target directory so we don’t get an error if it exists and for the input file to nicely care for that. Let’s also do the right thing and import and use subprocess in the "best practice" way. This will get things ready to run in parallel on their own. I will call this to_1080_hc.py
```
# imports
import subprocess, os, pathlib

# Path to ImageMagick
magick = r'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe'

def To1080HC(input_file, target_directory):
    """
    to_1080_hc.py input_file target_directory
    Will converto the input_file image to 1080 vertical pixels, increase the
    image contrast by 20% and save into the target_directory as a webp file
    """
        
    # Test to see if we have good input
    if not os.path.exists(input_file):
        raise Exception(f'The file {input_file} does not exist')
    if not os.path.exists(target_directory):
        try:
            os.mkdir(target_directory)
        except Exception as err:
            print("There was a problem making the target directory", str(err))
    
    args = ['convert', input_file, '-resize', 'x1080', '-brightness-contrast',
            '0x20']
    filePath = pathlib.Path(input_file)
    imgOut = target_directory + '/' + filePath.stem + '.webp'
    # make our command
    cmd = [magick] + args + [imgOut]
    process = subprocess.run(cmd, capture_output=True,
                             universal_newlines=True)
    # Handle the case of a bad run
    if process.returncode != 0:
        raise Exception(f'ImageMagick run failed using this command:\n{cmd}')
    return()
```
We can run this new function like this
```
# Next line only needed if current python file is in another dir
os.chdir("C:/Users/dave/Documents/GitHub/teach_yourself_python")
os.chdir(imgDir)
To1080HC(imgIn, targetDir)
```
And we can do a good-enough timing like this (run the whole thing at once)
```
from time import time
t0 = time()
To1080HC(imgIn, targetDir)
t1 = time()
print("Time needed to do the image conversion was", t1 - t0, "seconds")
```
Next let's use our function to do the same conversion for all our files in a loop. since we have 16 images we would expect this to take about 16 times as long.
```
# Now do all the jpg files
# Get the list of image files
imagelist = []
for file in os.listdir():
    fend = file[-4:]
    fend = fend.lower()
    if fend == '.jpg':
        imagelist.append(file)
# Start a time count, then call our function on each
t0 = time()
for imgIn in imagelist:
    To1080HC(imgIn, targetDir)
t1 = time()
print("Time to do", len(imagelist), "conversions was", t1 - t0, "seconds")
```
This took about 0.335 seconds for one image and about 8.5 for 16. This is probably a bit more than 16x because the landscape oriented images end up a bit bigger than our portrait oriented test.
We did this set automatically, but one at a time. So now, how can we try to run all these conversions at the same time? We could find the number of cores in our system and then make a run pool to always have that number of conversion jobs running. However, 16 is not that many so the operating system will probably sort it out fine. Let’s just run them all and see what happens.
To do this, let’s modify our module to run a conversion, without waiting, as another function.
```
# imports
import subprocess, os, pathlib

# Path to ImageMagick
magick = r'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe'

def To1080HC(input_file, target_directory):
    """
    To1080HC input_file target_directory
    Will converto the input_file image to 1080 vertical pixels, increase the
    image contrast by 20% and save into the target_directory as a webp file
    """
        
    # Test to see if we have good input
    if not os.path.exists(input_file):
        raise Exception(f'The file {input_file} does not exist')
    if not os.path.exists(target_directory):
        try:
            os.mkdir(target_directory)
        except Exception as err:
            print("There was a problem making the target directory", str(err))
    
    args = ['convert', input_file, '-resize', 'x1080', '-brightness-contrast',
            '0x20']
    filePath = pathlib.Path(input_file)
    imgOut = target_directory + '/' + filePath.stem + '.webp'
    # make our command
    cmd = [magick] + args + [imgOut]
    process = subprocess.run(cmd, capture_output=True,
                             universal_newlines=True)
    # Handle the case of a bad run
    if process.returncode != 0:
        raise Exception(f'ImageMagick run failed using this command:\n{cmd}')
    return()


def To1080HCp(input_file, target_directory):
    """
    To1080HCp.py input_file target_directory
    Will converto the input_file image to 1080 vertical pixels, increase the
    image contrast by 20%, save into the target_directory as a webp file and
    return the status of the running subprocess
    """
    
    # Test to see if we have good input
    if not os.path.exists(input_file):
        raise Exception(f'The file {input_file} does not exist')
    if not os.path.exists(target_directory):
        try:
            os.mkdir(target_directory)
        except Exception as err:
            print("There was a problem making the target directory", str(err))
    
    args = ['convert', input_file, '-resize', 'x1080', '-brightness-contrast',
            '0x20']
    filePath = pathlib.Path(input_file)
    imgOut = target_directory + '/' + filePath.stem + '.webp'
    # make our command
    cmd = [magick] + args + [imgOut]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    return(process)

```
Our new function has ‘p’ at the end and will return the process status instead of waiting for the subprocess to finish. Now we need to start all 16 subprocesses and then wait for them all to finish.
```
# If we run our module to see if the new function is OK, it should re-import
# Then import the new function
# Next line only needed if current python file is in another dir
os.chdir("C:/Users/dave/Documents/GitHub/teach_yourself_python")
from to_1080_hc import To1080HCp
os.chdir(imgDir)
# Now start all of the subprocesses and then wait on all of them
sp_list = []
t0 = time()
for imgIn in imagelist:
    p = To1080HCp(imgIn, targetDir)
    sp_list.append(p)
for p in sp_list:
    p.wait()
t1 = time()
print("Time to do", len(imagelist), "conversions was", t1 - t0, "seconds")
```
This ran in about 3 seconds, so faster, but not the 16x for the number of cores. Windows does have some overhead for each process start, then an SSD actually likes to have a queue depth of requests from 8-12. You will probably have to experiment quite a bit before you find the best mix of things to run at once for your system. Or just wait a few seconds. Also, ImageMagick has a 'morgrify' command that will take the same action on a set of images and that could also be tried.

[Python Lesson 15](lesson15.py) - Web Scraping