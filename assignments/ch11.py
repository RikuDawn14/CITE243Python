# Converting Dates from American(MM-DD-YYYY) to European(DD-MM-YYYY) style. 
# C:\Users\Matthew Balthaser\Videos\text

import os
import re
from pathlib import Path
import shutil



def walk_dir(start_dir, dest_dir):
    
    pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
    
    for root, dirs, files in os.walk(start_dir):
        
        for filename in files:
            match = pattern.search(filename)
            if match:
                date_adjust(root, filename, match, dest_dir)


def date_adjust(root, filename, match, dest_dir):

    mm, dd, yyyy = match.groups()
    new_name = filename.replace(match.group(0), f"{dd}-{mm}-{yyyy}")

    file_save(root, filename, new_name, dest_dir)
    

def file_save(root, filename, new_name, dest_dir):
    src = os.path.join(root, filename)
    dest = os.path.join(dest_dir, new_name)
    shutil.move(src, dest)


### Start of program ###
print("=" * 60 + "\nDate Format Converter: American (MM-DD-YYYY) to European (DD-MM-YYYY)\n" + "=" * 60)

while True:
    start_dir = input("\nEnter the full path for the directory you want to convert, then hit ENTER.\n   => ")
    if not os.path.exists(start_dir):
        print("That directory does not exist.")

    else:
        dest_dir = input("\nEnter a new path to save converted files to or leave blank and hit ENTER to save in same location.\n=> ")

        if not dest_dir:
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
                        print("\nDirectory was not made.\nClosing program.")
                        exit()
                except Exception as e:
                    print(f"Error: {e}")
                        
    break

walk_dir(start_dir, dest_dir)

input('\nPress any KEY to exit.')