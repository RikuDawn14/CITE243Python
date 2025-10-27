# Ch 17 PDF Password Breaker

"""
===========================================================
Program Name: ch17 Dictionary Attack
Author: Matthew Balthaser
Date: 2025-10-26
Description:
    This program preforms a dictionary attack on a password protected 
    PDF file.
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.
===========================================================
"""

# Get path to PDF
# Get path to dictionary file
# Make loop to try passwords on file (both upper and lower versions)
# Stop loop when password found
# Print password that worked

import time
import pypdf


def user_in():
    dic_path = input("Please enter the path to your dictionary file for attack then hit ENTER.\n\t=> ")
    
    with open(dic_path, 'r') as dictionary:
        dic_list = dictionary.read().splitlines()








### Start of program ###
print("=" * 60)
print("PDF Password Dictionary Attack".center(60))
print("=" * 60)

start = input("\nPress 'Y' then hit ENTER to continue.\nOtherwise enter any key or leave blank and hit ENTER to exit.\n\t=> ").strip().lower()
if start == "y":
    print("\n---PROGRAM STARTING---\n")
    time.sleep(.5)



else:
    time.sleep(.5)

print("\n---EXITING PROGRAM---\n")
input("Press ENTER to exit.")