#!/usr/bin/env python3
#
# Author: Richee Wilson
#
# Python version 3 required
#
# Purpose:
#
# I wrote this script to optimise images for a camera club website.
# In the website we display the winning images from monthly competitions and
# feature some images in the news items (blog).
# The gallery pages from the site became sluggish due to the large file sizes
# the higher resolution images made.  This script reduces the pixel
# dimensions to 1024 x 768 and lowers the quality to 80%.  I run the website
# and use this script regularly for this purpose.  This has significantly
# improved the performance of the website.  It's a wordpress site and the
# url is https://www.watfordcameraclub.org.uk/
#
# Usage:
#
# If your machine has the python3 interpreter installed, you can run this
# from your terminal inside any directory.  You must make an
# input directory here and place all your jpg files inside the
# input directory.
#
# This script will copy all *.jpg image files from the inside the input
# directory including all subdirectories and resize them to the desired pixel
# dimensions set in the "maxsize" tuple below (see comments in the code below)
# and output the results to the output directory at 80% jpg quality
# (quality can also be modified, again see comments in the code below).
#
# Note that all images must be jpg files and end in the .jpg extention.
#
# This script must be run inside a directory that contains an input directory.
# All images must be contained inside the input directory.  Sub diretories are allowed.
#
# The resized images will be saved under the output directory inside the script's current directory
# and will retain the original diretory structure as presented inside the input directory.
# There is no need to create the output directory, this script will do that for you.
#
#
import sys
from PIL import Image
import glob
import shutil
from shutil import copytree, ignore_patterns
#
# Change values here to the desired image dimensions in pixels.  1st value = width & 2nd value = height.
maxsize = (1024, 768)
try:
    # copies directory structure from input/ into output/
    shutil.copytree("input", "output", dirs_exist_ok=True,
                    ignore=ignore_patterns("*.*"))
except IOError:
    sys.exit('You must create an "input" folder (case sensitive) in the current directory containing jpg files to run this script.')

count = 0
# finds all images in the input path recursively
for input_img_path in glob.glob('input/**/*.[Jj][Pp][Gg]', recursive=True):
    print(input_img_path)
    # while retaining sub directory structure replaces input/... with output/...
    output_img_path = str(input_img_path).replace("input", "output")
    print(output_img_path)
    with Image.open(input_img_path) as im:
        im.thumbnail(maxsize)  # resize the image as defiled by "maxsize"
        # save the resized image to 80% quality (modify if desired) into the output directory
        im.save(output_img_path, "JPEG", quality=80)
        print(f"processing file {input_img_path} done...")
        count += 1
print()
if count == 0:
    print('No files were processed, did you put your jpg files in the "input" folder?')
else:
    print(str(count)+" images have been processed, you will find them inside the output directory.")
print()

#