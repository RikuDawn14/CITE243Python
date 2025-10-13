# Attempt two of ch10 assignment to add read txt file not preset mad lib

"""
===========================================================
Program Name: ch10.2 read-write file
Author: Matthew Balthaser
Date: 2025-09-28
Description:
    This program creates a Mad Libs that reads in text files and
    lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears.
    It is designed to print the results to the screen in addition to saving them to a text file.
    
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import os
from pathlib import Path

### Function to read txt file to allow user to input words. ###
def read_txt():

    global mad_data
    while True:
        mad_lib_file = input("Enter file path of desired Mad Lib text file.\n => ")

        if not os.path.exists(mad_lib_file): # Checks if the input in mad_lib_file exists
            print("File does not exist or file path was entered wrong.") # If the os.path.exists(mad_lib_file) comes back as false it prints error message.

        else: # If os.path.exists(mad_lib_file) returns as true.
            try: # Tries to open file. If possible it continues with try block.
                with open(mad_lib_file, encoding='UTF-8') as file:
                    mad_data = file.read() 
        
                for words in ["ADJECTIVE", "NOUN", "ADVERB", "VERB", "COLOR", "EMOTION", "PLURAL NOUN", "SHAPE"]: # After opening file search for these words.
                    while mad_data.find(words) > 0: # While there is more than 0 of that word continue.
                        mad_data = mad_data.replace(words, get_input(f"Enter a {words.lower()}:\n =>"), 1) # Uses get_input replace the first instance of that word in the file.
        
                long_line = max(mad_data.splitlines(), key=len) # Figures out the longest line in file for file print in terminal for border sizing.

                print('\n' + '=' * len(long_line) + '\n' + mad_data + '=' * len(long_line) + '\n')
                break
            except Exception as e: # If file is not valid, print error.
                print(f"Error: {e}")

### Function to not allow blank inputs for Mad Lib. ###
def get_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("You have to enter something! No blanks.")

### Function to write results of mad_lib to .txt file in chosen location. ###
def file_write():

    file_path = input("\nEnter file path for custom save location (/home/Rico) and file name (example.txt).\nLeave blank and hit ENTER to save in location of this python file.\n=> ")
    
    if not file_path: # If the file path is left blank file_path will be false and do this.
        file_path = Path.cwd()/"mad_lib.txt"

    folder = os.path.dirname(file_path) # If file_path has sting folder becomes just the directory path for file_path.

    if not os.path.exists(folder): # If os.path.exists(folder) is false move to mkdir.
        mkdir = input(f"The directory {{folder}} does not exist.\nWould you like to create it? (y/n): ").strip().lower()

        if mkdir == "y":
            os.makedirs(folder)
            print(f"Created directory: {folder}")
        else:
            print("\nFile not saved.")
            return
    
    try: # If os.path.exists(folder) true.
        with open(file_path, 'w') as file: # Try to open and write file at path if already exists, creates if not.
            file.write(mad_data)
        print(f"Your Mad Lib was saved to: {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")


### Start of program. ###
print("=" * 28 + "\nWelcome to a python Mad Lib.\n" + "=" * 28)
input('\nPress ENTER to start!\n')

read_txt()

save_file = input("\nWould you like to save this as a text file? (y/n): ").strip().lower()
if save_file == 'y':
    file_write()

else:
    print("\nFile not saved.")

input('\nPress ENTER to exit.')