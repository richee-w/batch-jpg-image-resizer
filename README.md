# Batch jpg image resizer

Author: Richee Wilson

Python version 3 required

## Purpose

I wrote this script to optimise images for a camera club website.
In the website we display the winning images from monthly competitions and
feature some images in the news items (blog).
The gallery pages from the site became sluggish due to the large file sizes
the higher resolution images made. This script reduces the pixel
dimensions to 1024 x 768 and lowers the quality to 80%. I run the website
and use this script regularly for this purpose. This has significantly
improved the performance of the website. It's a wordpress site and the
url is [https://www.watfordcameraclub.org.uk](https://www.watfordcameraclub.org.uk/)

## Usage

If your machine has the python3 interpreter installed, you can run this
from your terminal inside any directory. You must make an
input directory here and place all your jpg files inside the
input directory.
This script will copy all \*.jpg image files from the inside the input
directory including all subdirectories and resize them to the desired pixel
dimensions set in the "maxsize" tuple below (see comments in the code below)
and output the results to the output directory at 80% jpg quality
(quality can also be modified, again see comments in the code below).

**Note: All images must be jpg files and end in the .jpg extension.**

This script must be run inside a directory that contains an input directory.
All images must be contained inside the input directory. Sub directories are allowed.

The resized images will be saved under the output directory inside the script's current directory
and will retain the original directory structure as presented inside the input directory.
There is no need to create the output directory, this script will do that for you.
