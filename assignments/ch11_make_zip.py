# ch11 convert directory into zip.
"""
===========================================================
Program Name: ch11 Date Converter
Author: Matthew Balthaser
Date: 2025-09-28
Description:
    This program converts a folder into a zip for storage.
    It is designed to compress a directory and move to user input location.
    
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import os
import time
import zipfile

def zippy(start_dir, zip_name, dest_dir):

    if not zip_name.endswith(".zip"):
        zip_name += ".zip"
    
    new_path = os.path.join(dest_dir, zip_name)
    
    with zipfile.ZipFile(new_path, 'w') as new_zip:

        if os.path.isfile(start_dir):
            new_zip.write(start_dir, os.path.basename(start_dir))

        else:
            for root, dirs, files in os.walk(start_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    full_path = os.path.relpath(file_path, os.path.dirname(start_dir))
                    new_zip.write(file_path, full_path)

    print(f"\nSuccessfully created: [{new_path}]")


### Start of program ###
print("=" * 60)
print("zip compressor".center(60))
print("=" * 60)

while True:
    start_dir = input("\nPlease input the file path of the folder or file you want compressed.\n => ").strip()
    if not os.path.exists(start_dir): # Checks if user input is vaild path.
        print("That directory does not exist.")
    
    else:
        dest_dir = input("\nEnter a new path to save compressed files to or leave blank and hit ENTER to save in same location.\n=> ").strip()
        zip_name = input("\nWhat would you like to name your zip file?\n => ").strip()
        
        while not zip_name:
                print("You must give a name for zip file.")
                zip_name = input("\nWhat would you like to name your zip file?\n => ").strip()

        if not dest_dir: # If dest_dir is left blank.
            dest_dir = os.path.dirname(start_dir) if os.path.isfile(start_dir) else start_dir

        elif not os.path.exists(dest_dir): # If os.path.exists(dest_dir) is false move to mkdir.
            mkdir = input(f"The directory {dest_dir} does not exist.\nWould you like to create it? (y/n)\n  =>  ").strip().lower()
            if mkdir == "y":
                try:
                    os.makedirs(dest_dir)
                    print(f"Created directory: {dest_dir}")
                except Exception as e:
                    print(f"Error: {e}")
                    continue
            else:
                print("\nDirectory was not made.\n\nClosing program.")
                exit()
        break


print("\n---PROGRAM STARTING---\n")
time.sleep(1) # Slight pause in the program to give user feeling that program is working.
zippy(start_dir, zip_name, dest_dir)