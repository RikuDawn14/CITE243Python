# Chapter 10 (READING AND WRITING FILES) Assignment
"""
===========================================================
Program Name: ch10 read-write file
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
import textwrap

#Function to not allow blank inputs for Mad Lib
def get_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("You have to enter something! No blanks.")

# Function for the input of the words and printing of Mad Lib.
def mad_lib():

    adjective_1 = get_input("Choose an adjective: ")
    adjective_2 = get_input("Choose a second adjective: ")
    color_1 = get_input("Choose a color: ")
    color_2 = get_input("Choose another color: ")
    noun_1 = get_input("Choose a noun: ")
    emotion = get_input("Choose an emotion: ")
    noun_2 = get_input("Choose a second noun: ")
    noun_3 = get_input("Choose a third noun: ")
    adjective_3 = get_input("Choose a third adjective: ")
    verb_1 = get_input("Choose a verb: ")
    adjective_4 = get_input("Choose a fourth adjective: ")
    noun_4 = get_input("Choose a fourth noun: ")
    p_noun_1 = get_input("Choose a plural noun: ")
    adjective_5 = get_input("Choose a fifth adjective: ")
    noun_5 = get_input("Choose a fifth noun: ")
    p_noun_2 = get_input("Choose a second plural noun: ")
    shape = get_input("Choose a shape: ")
    adjective_6 = get_input("Choose a sixth adjective: ")
    verb_2 = get_input("Choose a second verb: ")
    adjective_7 = get_input("Choose a seventh adjective: ")
    p_noun_3 = get_input("Choose a third plural noun: ")
    p_noun_4 = get_input("Choose a fourth plural noun: ")
    adjective_8 = get_input("Choose a eighth adjective: ")
    p_noun_5 = get_input("Choose a fifth plural noun: ")

    global text

    text = textwrap.dedent(f"""
        One sunny {adjective_1} afternoon, the big day finally arrived! The {adjective_2} couple, 
        dressed in {color_1} and {color_2}, stood at the end of the {noun_1}
        as their family and friends cheered. The ceremony was filled with {emotion}, as the officiant declared, “I now pronounce you {noun_2} and {noun_3}!” 
        The couple sealed the deal with a {adjective_3} kiss that made everyone {verb_1} in delight. 
        At the reception, the {adjective_4} cake stole the show. It was shaped like a {noun_4} and topped with {p_noun_1}. 
        The guests were so impressed that they yelled out "{adjective_5} {noun_5}!". 
        The highlight of the evening was the first dance. The couple twirled like {p_noun_2} on the dance floor. 
        Everyone joined in, forming a {shape} around the happy pair. By the end of the night, 
        even the {adjective_6} guests were up and {verb_2.upper()}-ING! 
        It was a {adjective_7} day full of {p_noun_3}, laughter, and {p_noun_4}. 
        As the couple left for their {adjective_8} honeymoon, everyone waved their {p_noun_5}. 
       """).strip()
    
    print("\n" + text + "\n")

#Function to write results of mad_lib to .txt file in chosen location.
def file_write():

    file_path = input("\nEnter file path for custom save location and name.\nLeave blank and hit ENTER to save in location of this python file.\n=> ")
    
    if not file_path:
        file_path = "mad_lib.txt"

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
            file.write(text)
        print(f"Your Mad Lib was saved to: {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

# Start of program.
print("=" * 28 + "\nWelcome to a python Mad Lib.\n" + "=" * 28)
input('\nPress ENTER to start!\n')

mad_lib()

save_file = input("\nWould you like to save this as a text file? (y/n): ").strip().lower()
if save_file == 'y':
    file_write()

else:
    print("\nFile not saved.")

input('\nPress ENTER to exit.')