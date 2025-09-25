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
    Run the script using Python 3.x13.7. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import os
from pathlib import Path

# Function to read txt file to allow user to input words
def read_txt():

    global mad_data
    while True:
        mad_lib_file = input("Enter file path of desired Mad Lib text file.\n => ")
        if not os.path.exists(mad_lib_file):
            print("File does not exist or file path was entered wrong.")

        else:
            try:
                with open(mad_lib_file, encoding='UTF-8') as file:
                    mad_data = file.read() 
        
                for words in ["ADJECTIVE", "NOUN", "ADVERB", "VERB", "COLOR", "EMOTION", "PLURAL NOUN", "SHAPE"]:
                    while mad_data.find(words) > 0:
                        mad_data = mad_data.replace(words, get_input(f"Enter a {words.lower()}:\n =>"), 1)
        
                long_line = max(mad_data.splitlines(), key=len)

                print('\n' + '=' * len(long_line) + '\n' + mad_data + '=' * len(long_line) + '\n')
                break
            except Exception as e:
                print(f"Error: {e}")

# Function to not allow blank inputs for Mad Lib
def get_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("You have to enter something! No blanks.")

#Function to write results of mad_lib to .txt file in chosen location.
def file_write():

    file_path = input("\nEnter file path for custom save location and name.\nLeave blank and hit ENTER to save in location of this python file.\n=> ")
    
    if not file_path:
        file_path = Path.cwd()/"mad_lib.txt"

    folder = os.path.dirname(file_path)

    if folder and not os.path.exists(folder):
        mkdir = input(f"The directory {{folder}} does not exist.\nWould you like to create it? (y/n): ").strip().lower()

        if mkdir == "y":
            os.makedirs(folder)
            print(f"Created directory: {folder}")
        else:
            print("\nFile not saved.")
            return
    
    try:
        with open(file_path, 'w') as file:
            file.write(mad_data)
        print(f"Your Mad Lib was saved to: {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")


# Start of program.
print("=" * 28 + "\nWelcome to a python Mad Lib.\n" + "=" * 28)
input('\nPress ENTER to start!\n')

read_txt()

save_file = input("\nWould you like to save this as a text file? (y/n): ").strip().lower()
if save_file == 'y':
    file_write()

else:
    print("\nFile not saved.")

input('\nPress ENTER to exit.')