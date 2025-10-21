# Find issue in speadsheet and fix

# Google sheet to use "https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg"

"""
===========================================================
Program Name: ch15 check googlesheet
Author: Matthew Balthaser
Date: 2025-10-26
Description:
    This program goes to a googlesheet searches for and issue
    then allows user to fix that issue.
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.
===========================================================
"""

import time
import ezsheets

### Function that checks the spreadsheet ###
def sum_check():
    ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
    row = 1
    total_row = ss.rowCount()
    wrong = []
    while row <= total_row:
        try:
            beans = int(ss.sheets[0].getRow(row)[0])
            jars = int(ss.sheets[0].getRow(row)[1])
            total = int(ss.sheets[0].getRow(row)[2])
        except ValueError:
            print(f"Row {row} did not have numbers. Skipping to next row.")
            row += 1
            time.sleep(.5)
            continue
        pair = beans * jars
        if not pair == total:
            wrong.append(row)
        row += 1
    total_err = len(wrong)
    print(f"There are a total of {total_err} errors.\n")
    print("=" * 60)
    print(f"The following row or rows had errors: {wrong}")
    print("=" * 60)



### Start of program ###
print("=" * 60)
print("Check Googlesheet for errors".center(60)) # Kinda a lie only works with the specified sheet
print("=" * 60)

start = input("\nPress 'Y' then hit ENTER to continue.\nOtherwise enter any key or leave blank and hit ENTER to exit.\n\t=> ").strip().lower()
if start == "y":
    print("\n---PROGRAM STARTING---\n")
    time.sleep(1)
    sum_check()


else:
    print("Goodbye!")
    time.sleep(1)

input("Press ENTER to exit.")