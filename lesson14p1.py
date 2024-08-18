# Since I am on Windows, I use a raw string due to the '\'s
magick = r'C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe'
# Set where are images are and/or will be put (choose what works for you
#  and make sure it exists)
imgDir = 'C:/Users/dave/pclass'

# change to the directory we are going to work in
import os
os.chdir(imgDir)

# a list of the arguments we want to give to ImageMagick
args = ['logo:']
# the image we would like to use/create
img = 'logo.png'
# make our command (a list of all the parts)
cmd = [magick] + args + [img]
# we need the subprocess module, but let's just import run, even though
#  it is not best practice
from subprocess import run
process = run(cmd, capture_output=True, universal_newlines=True)
# We could/should test for errors in a real program, but let's skip
#  that for now and just use Variable Explorer or file explorer
#  and move forward
# Now let's change the args and use identify
args = ['identify']
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# This time, we need to look at what ImageMagick printed
output = process.stdout.split('\n')[0].split()
print("The file type is", output[1], "with a resolution of", output[2])

# Convert between file formats (the original use case). To see a list of
#  formats use "magick identify -list format" in a command prompt
# Let's make a webp version of our png logo
args = ['logo.png', 'logo.webp']
cmd = [magick] + args
process = run(cmd, capture_output=True, universal_newlines=True)
# Webp is supposed to be smaller, let's check
files = ['logo.png', 'logo.webp']
args = ['identify', '-format', '"%b"']
for file in files:
    cmd = [magick] + args + [file]
    process = run(cmd, capture_output=True, universal_newlines=True)
    output = process.stdout.split('\n')[0]
    print("File", file, "is", output, "Bytes in size")
# Could be useful to save space or if the program/web site we want to
#  to use only takes a certain format

# 10"x8" is a common print size we can get a frame in at Walmart
# 300 DPI (dots per inch) is a common print density (ignore
#  the math issue vs. literal dots per inch, it's along a line)
width = 10*300
height = 8*300
# rose: below is a built-in image, like logo:
args = ['rose:', '-resize', f'{width}x{height}^', '-gravity', 'center',
        '-extent', f'{width}x{height}']
img = 'rose10x8-300dpi.jpg'
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# Why so blurry? The rose base image is very small
# Let's format to a 1080 standard TV size
width = 1920
height = 1080
args = ['rose:', '-resize', f'{width}x{height}^', '-gravity', 'center',
        '-extent', f'{width}x{height}']
img = 'rose-full_hd.webp'
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# If you look at the last two images and focus on the edges, you
#  will notice that we are losing a bit of the image on the
#  top/bottom or the sides
# Let's reformat the logo to 4k 16x9, but we don't want to cut
#  the top and bottom of our wizard off, so we will need to
#  put the logo on top of a white background
# First, let's see the damaged wizard
width = 3840
height = 2160
args = ['logo:', '-resize', f'{width}x{height}^', '-gravity', 'center',
        '-extent', f'{width}x{height}']
img = 'logo-4k.webp'
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# Now let's save him (width and height are still the same)
args = ['logo:', '-resize', f'{width}x{height}',
        '-background', 'white', '-gravity', 'center', '-extent', 
        f'{width}x{height}']
img = 'logo-4k_no_clip.webp'
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# Notice we used -background and removed the '^' from the first set
#  of dimensions. The '^' would cause that dimension to resize
#  until it matched the target and any remainder would be cropped
#  in the other dimension

# If we have some machine learning pipeline, we might have
#  to preprocess the image in some way to get it ready
# What if an image came to us rotated 90 degrees and we had to
#  get it back
# Let's just rotate our wizard to see
args = ['logo:', '-rotate', '-90']
img = 'logo-rotate-ccw.webp'
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# Also common is to make the image a black and white bitmap
# Let's use the rose for the next couple
args = ['rose:', '-type', 'grayscale', '-colorspace', 'gray']
img = 'rose-bw.bmp'
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# ImageMagick can also do some more advanced operations, like
#  edge detection (https://imagemagick.org/Usage/convolve/#dog)
args = ['-bias', '50%', '-morphology', 'Convolve', 'DoG:0,0,2.4']
out_img = 'rose-edge.png'
cmd = [magick] + [img] + args + [out_img]
process = run(cmd, capture_output=True, universal_newlines=True)

# Let's see if we can make our wizard move as a GIF
# We are going to have a bunch of temp files, so make a directory
os.mkdir('temp')
wizWidth = 160
wizHeight = 120
width = 300
height = 120
# first generate a logo of the proper size
args = ['logo:', '-resize', f'{wizWidth}x{wizHeight}']
cmd = [magick] + args + ['logo-120.png']
run(cmd, capture_output=True, universal_newlines=True)
# then put all the sub images in the temp directory (will take a sec)
for i in range(width):
    img = f'temp/wiz{i:03d}.png'
    args = ['-size', f'{width}x{height}', 'xc:white', 'logo-120.png',
            '-geometry', f'+{i}+0', '-compose', 'over', '-composite']
    cmd = [magick] + args + [img]
    run(cmd, capture_output=True, universal_newlines=True)
# then make the gif (this will also take a sec)
img = 'wiz.gif'
args = ['-delay', '2', '-loop', '0', 'temp/*.png']
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# view in a web browser with file:///C:/Users/dave/pclass/wiz.gif
# would a webp be smaller?
img = 'wiz.webp'
args = ['wiz.gif']
cmd = [magick] + args + [img]
process = run(cmd, capture_output=True, universal_newlines=True)
# yep, half the size
