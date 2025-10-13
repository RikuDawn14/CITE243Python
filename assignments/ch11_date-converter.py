# Converting Dates from American(MM-DD-YYYY) to European(DD-MM-YYYY) style. 

"""
===========================================================
Program Name: ch11 Date Converter
Author: Matthew Balthaser
Date: 2025-09-28
Description:
    This program converts the dates in a file name.
    It is designed to convert date format in file name and move to user input location.
    
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import os
import re
import shutil
import time

file_numb = 0 # Variable just to keep track of number of files renamed.

### Function to search through directories and check file names to Regex pattern for dates. ###
def walk_dir(start_dir, dest_dir):
    global file_numb
    pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})') # Regex pattern for date format DD-DD-DDDD.
    
    for root, dirs, files in os.walk(start_dir): # os.walk() looks through directory and returns file path and file names.
        
        for filename in files: # For files found by os.walk() attach to variable.
            match = pattern.search(filename) # See if the file name has a date from Regex.
            if match: # If match found increase file_numb by 1 and pass variables to next function.
                file_numb += 1
                rel_path = os.path.relpath(root, start_dir) # Gets relitive path for files in sub-directories.
                date_adjust(root, filename, match, rel_path, dest_dir)

### Function to create new file name to convert the date. ###
def date_adjust(root, filename, match, rel_path, dest_dir):

    mm, dd, yyyy = match.groups() # Give groups 1-3 a variable name for cleaner code.
    new_name = filename.replace(match.group(0), f"{dd}-{mm}-{yyyy}") # Creates new file name with only the dates switched.

    file_save(root, filename, new_name, rel_path, dest_dir)
    
### Function to move files with new name and directory. ###
def file_save(root, filename, new_name, rel_path, dest_dir):
    
    src = os.path.join(root, filename) # Variable to combine old file path and file name.
    
    if rel_path == ".": # If file is in the parent directoriy just use the new name and dest_dir.
        dest = os.path.join(dest_dir, new_name)
    else: # If file is in child directory this preserves the file sturcture of the converted files.
        rel = os.path.join(dest_dir, rel_path)
        dest = os.path.join(rel, new_name) # Variable to combine new file path and file name.
        os.makedirs(rel, exist_ok=True) # Checks to see if new relitive path exists and makes if not. `exist_ok=True` stops error if path exists.

    shutil.move(src, dest) # Moves file with variables


### Start of program ###
print("=" * 69)
print("Date Format Converter: American (MM-DD-YYYY) to European (DD-MM-YYYY)".center(69))
print("=" * 69)
while True: # Loop for getting user inputs for source and destination directories and creation of if needed.
    start_dir = input("\nEnter the full path for the directory you want to convert, then hit ENTER.\n   => ")
    if not os.path.exists(start_dir): # Checks if user input is vaild path.
        print("That directory does not exist.")

    else:
        dest_dir = input("\nEnter a new path to save converted files to or leave blank and hit ENTER to save in same location.\n=> ")

        if not dest_dir: # If dest_dir is left blank.
            dest_dir = start_dir
            break

        else:
            if not os.path.exists(dest_dir): # If os.path.exists(dest_dir) is false move to mkdir.
                try:
                    mkdir = input(f"The directory {dest_dir} does not exist.\nWould you like to create it? (y/n)\n  =>  ").strip().lower()
                    if mkdir == "y":
                        os.makedirs(dest_dir)
                        print(f"Created directory: {dest_dir}")
                        
                    else:
                        print("\nDirectory was not made.\n\nClosing program.")
                        exit()
                except Exception as e:
                    print(f"Error: {e}")                        
    break

print("\n---PROGRAM STARTING---\n")
time.sleep(1) # Slight pause in the program to give user feeling that program is working.
walk_dir(start_dir, dest_dir)

# Options to print to user to give feedback on number of files converted and reminder of new location.
if file_numb == 0: 
    print("No files with dates found. Check your file path to ensure right location.")
elif file_numb == 1:
    print(f"({file_numb}) file has had the dates converted and saved in ({dest_dir}).")
else:
    print(f"({file_numb}) files have had the dates converted and saved in ({dest_dir}).")

input('\nPress any KEY to exit.')