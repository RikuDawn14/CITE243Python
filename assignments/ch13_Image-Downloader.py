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
        url = input("Please input a full URL for a website to search, then hit ENTER.\n\t=> ") # get URL from user
        if not url:
            print("\nYou must enter a URL.\n")
        else:
            print("\nPlease wait while we search.\n")
            url_search(url)

def url_search(url):
    j

def download():
    
    file_path = input("\nEnter file path for custom save location or leave blank to use your current directory. Example </home/Rico>")

    if not file_path:
        file_path = os.Path.cwd()
    
    folder = os.path.dirname(file_path)
    
    if not os.path.exists(folder):
        mkdir(folder)

def mkdir(folder):
    mkdir = input(f"The directory {{folder}} does not exist.\nWould you like to create it? (y/n): ").strip().lower()

    if mkdir == "y":
        try:
            os.makedirs(folder)
            print(f"Created directory: {folder}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("\nFiles not saved. Exiting program.")
        time.sleep(1)
        exit()

### Start of program ###
print("=" * 60)
print("Image downloader".center(60))
print("=" * 60)
startText = textwrap.dedent("""
        ***************
        *** WARNING ***
        ***************
        This is a program to search a image sharing site.
        It will then download those images to a desiered location.
        This may result in a large number of downloads.""")
print(startText)
start = input("\nPress 'Y' then hit ENTER to continue.\nOtherwise enter any key or leave blank and hit ENTER to exit.").strip().lower()
if start == "y":
    print("\n---PROGRAM STARTING---\n")
    time.sleep(1)
    user_input()
else:
    print("Goodbye!")
    time.sleep(1)
    exit()