# Find issue in speadsheet and fix

# Google sheet to use "https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg"

"""
===========================================================
Description:
    This program goes to a googlesheet searches for and issue
    then allows user to fix that issue.
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.
===========================================================
"""

# Look at BEANS PER JAR and JARS in a row add the numbers together and compare to TOTAL BEANS
# If numbers match move to next row
# If not, alert user of what row and offer to replace number
# Get user input on fix then continue.
# After done list number of rows checked, how many issues found, and how many changed

import time
import ezsheets

def sum_check(ss):
    ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
    row = 1
    beans = int(ss.sheets[0].getRow(f"{row}"[0]))
    jars = int(ss.sheets[0].getRow(f"{row}"[1]))
    total = int(ss.sheets[0].getRow(f"{row}"[2]))
    pair = beans * jars
    wrong = []
    if not pair == total:
        wrong.append(row)



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

input("Press any KEY to exit.")