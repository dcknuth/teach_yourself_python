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

# Next line only needed if current python file is in another dir
os.chdir("C:/Users/dave/Documents/GitHub/teach_yourself_python")
from to_1080_hc import To1080HC
os.chdir(imgDir)
To1080HC(imgIn, targetDir)

from time import time
t0 = time()
To1080HC(imgIn, targetDir)
t1 = time()
print("Time needed to do the image conversion was", t1 - t0, "seconds")

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
