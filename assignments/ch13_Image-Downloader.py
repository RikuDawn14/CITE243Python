# Program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photo, and then downloads all the resulting images.

"""
===========================================================
Program Name: ch13 Photo scraper 
Author: Matthew Balthaser
Date: 2025-0910-19
Description:
    This program goes to a photo sharing site and searches for
    category of photos then downloads them.
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.
===========================================================
"""

import time
import os
import requests
from bs4 import BeautifulSoup
import textwrap
from urllib.parse import urlparse, urljoin

### Function to verify that the URL given by user is a valid URL ###
def url_val(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme in ('http', 'https') and parsed.netloc)

### Function that trys to connect to the URL and returns an error if not able ###
def url_check(url: str) -> tuple[bool, str, requests.Response]:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return False, "Request timed out", None
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server", None
    except requests.exceptions.HTTPError as e:
        return False, f"HTTP error: {e}", None
    except Exception as e:
        return False, f"Unexpected error: {e}", None
    return True, "Success. That was a valid URL, searching for images.", response

### Function to search web page to find images ###
def image_find(url: str, response):
    
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    img_urls = []
    for img in images:
        src = img.get('src')
        if src:
            img_url = urljoin(url, img['src'])
            if img_url:
                img_urls.append(img_url)
    total = len(img_urls)
    print(f"Found {total} images.")
    down = input("Would you like to download these images? 'Y/N'\n\t=> ").strip().lower()
    if down == 'y':
        dirChoose(img_urls, total)
    else:
        print("Images not downloaded. Exiting program")
        return


### Function to chose download location ###
def dirChoose(img_urls, total):
    
    file_path = input("\nEnter file path for custom save location or leave blank to use your current directory.\nExample </home/Rico>\n\t=> ")

    if not file_path:
        file_path = os.path.getcwd()
    if not os.path.exists(file_path):
        mkdir(file_path, img_urls, total)
    else:
        download(file_path, img_urls, total)

### Function to make directory if it doesnt exist ###
def mkdir(file_path, img_urls, total):
    mkdir = input(f"The directory {{file_path}} does not exist.\nWould you like to create it? (y/n)\n\t=>  ").strip().lower()

    if mkdir == "y":
        try:
            os.makedirs(file_path)
            print(f"Created directory: {file_path}")
            time.sleep(1)
            download(file_path, img_urls, total)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("\nFiles not saved. Exiting program.")
        time.sleep(1)
        return

### Function to doenload the image files ###
def download(file_path, img_urls, total):
    num = 0
    fails = 0
    for url in img_urls:

        try:
            filename = os.path.basename(url)
            img = requests.get(url)
            image_file = os.path.join(file_path, filename)
            with open(image_file, 'wb') as f:
                num += 1
                print(f"Downloading: {filename}:{num}/{total} ")
                f.write(img.content)
                time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            fails += 1
    print("=" * 60)
    print(f"Completed {num} out of {total} with {fails} fails.")
    print("=" * 60)
    time.sleep(1)



### Start of program ###
print("=" * 60)
print("Image downloader".center(60))
print("=" * 60)
print('') # Left blank for readability.
print("*" * 60)
print("WARNING".center(60))
print("*" * 60)
startText = textwrap.dedent("""
        This is a program to search an image sharing site.
        It will then download those images to a desiered location.
        This may result in a large number of downloads.""")
print(startText)
start = input("\nPress 'Y' then hit ENTER to continue.\nOtherwise enter any key or leave blank and hit ENTER to exit.\n\t=> ").strip().lower()
if start == "y":
    print("\n---PROGRAM STARTING---\n")
    time.sleep(1)
    while True:
        url = input("Please input a full URL for a website to search, then hit ENTER.\n\t=> ") # get URL from user
        if not url:
            print("\nYou must enter a URL.\n")
        else:
            print("\nPlease wait while we search.\n")
            time.sleep(1)
            if not url_val(url):
                print("Invalid URL. Make sure to include 'http://' or 'https://'\n")
                continue
            
            success, message, response = url_check(url)
            if not success:
                print(f"Failed to get page: {message}\n")
                continue
            else:
                print(f"{message}")
                image_find(url, response)


else:
    print("Goodbye!")
    time.sleep(1)

input("Press any KEY to exit.")