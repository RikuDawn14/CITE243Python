# Program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photo, and then downloads all the resulting images.

"""
===========================================================
Description:
    This program goes to a photo sharing site and searches for
    category of photos then downloads them.
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.
===========================================================
"""
# get url for site
# scrape site for images
# offer to download images
# create dir if not found

import time
import os
import requests
import bs4
import textwrap

def user_input():
    
    while True:
        url = input("Please input a URL for a website to search, then hit ENTER.\n\t=> ") # get URL from user
        if not url:
            print("\nYou must enter a URL.\n")
        else:
            print("\nPlease wait while we search.\n")
            url_search(url)

def url_search(url):
    j

def download():
    r
def mkdir():
    r

### Start of program ###
print("=" * 60)
print("Image downloader".center(60))
print("=" * 60)
print.textwrap.dendent("""This is a program to search a image sharing site.
        It will then download those images to a desiered location.
        ***WARNING***
        This may result in a large number of downloads.""")
start = input("\nPress 'Y' then hit ENTER to continue.\nOtherwise enter any key or leave blank and hit ENTER to exit.").strip().lower()
if start == "y":
    print("\n---PROGRAM STARTING---\n")
    user_input()