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
