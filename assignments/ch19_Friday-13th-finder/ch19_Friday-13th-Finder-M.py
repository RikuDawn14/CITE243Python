# ch 19 Friday the 13th Finder

"""
===========================================================
Program Name: ch19 Friday the 13th Finder
Author: Matthew Balthaser
Date: 2025-11-09
Description:
    This program preforms a search and lists when firday the 13th are.
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.
===========================================================
"""

import time
import importlib

future = importlib.import_module("ch19_Friday-13th-Finder-F") # imports future dates function
past = importlib.import_module("ch19_Friday-13th-Finder-P") # imports past dates function

### function to get user input to choose what action they would like to do ###
def user_cho():
    
    while True:
        user_in = input("Type which program you would like to run, then hit ENTER.\n\n1) Find future 10 friday the 13th's.\n2) Find past friday the 13th's.\nEXIT) exit\n\n\t=> ").strip().lower()
        if not user_in:
            print("You need to enter an option.")
        elif user_in == '1':
            future.find_future_fridays() # runs function in future file
            time.sleep(1.5)
        elif user_in == '2':
            past.find_past_fridays() # runs function in past file
            time.sleep(1.5)
        elif user_in == 'exit':
            return
        else:
            print(f"[{user_in}] is not a valid option.")
            time.sleep(1)


### Start of program ###
print("=" * 60)
print("Friday the 13th Finder".center(60))
print("=" * 60)

start = input("\nPress 'Y' then hit ENTER to continue.\nOtherwise enter any key or leave blank and hit ENTER to exit.\n\t=> ").strip().lower()
if start == "y":
    print("\n---PROGRAM STARTING---\n")
    time.sleep(.5)
    user_cho()

else:
    time.sleep(.5)

print("\n---EXITING PROGRAM---\n")
input("Press ENTER to exit.")