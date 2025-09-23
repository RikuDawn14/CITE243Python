# Chapter 10 (READING AND WRITING FILES) Assignment
"""
===========================================================
Program Name: ch10 read-write file
Author: Matthew Balthaser
Date: 2025-09-28
Description:
    This program creates a Mad Libs that reads in text files and
    lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
    It is designed to print the results to the screen in addition to saving them to a new text file.
    
Usage:
    Run the script using Python 3.x13.7. Ensure all dependencies
    are installed before execution.

===========================================================
"""
def mad_lib():

    adjective_1 = input("Choose an adjective: ")
    adjective_2 = input("Choose a second adjective: ")
    color_1 = input("Choose a color: ")
    color_2 = input("Choose another color: ")
    noun_1 = input("Choose a noun: ")
    emotion = input("Choose an emotion: ")
    noun_2 = input("Choose a second noun: ")
    noun_3 = input("Choose a third noun: ")
    adjective_3 = input("Choose a third adjective: ")
    verb_1 = input("Choose a verb: ")
    adjective_4 = input("Choose a fourth adjective: ")
    noun_4 = input("Choose a fourth noun: ")
    p_noun_1 = input("Choose a plural noun: ")
    adjective_5 = input("Choose a fifth adjective: ")
    noun_5 = input("Choose a fifth noun: ")
    p_noun_2 = input("Choose a second plural noun: ")
    shape = input("Choose a shape: ")
    adjective_6 = input("Choose a sixth adjective: ")
    verb_2 = input("Choose a second verb: ")
    adjective_7 = input("Choose a seventh adjective: ")
    p_noun_3 = input("Choose a third plural noun: ")
    p_noun_4 = input("Choose a fourth plural noun: ")
    adjective_8 = input("Choose a eighth adjective: ")
    p_noun_5 = input("Choose a fifth plural noun: ")

    text = f"""
        One sunny {adjective_1} afternoon, the big day finally arrived! The {adjective_2} couple, 
        dressed in {color_1} and {color_2}, stood at the end of the {noun_1}
        as their family and friends cheered. The ceremony was filled with {emotion}, as the officiant declared, “I now pronounce you {noun_2} and {noun_3}!” 
        The couple sealed the deal with a {adjective_3} kiss that made everyone {verb_1} in delight. 
        At the reception, the {adjective_4} cake stole the show. It was shaped like a {noun_4} and topped with {p_noun_1}. 
        The guests were so impressed that they yelled out "{adjective_5} {noun_5}!". 
        The highlight of the evening was the first dance. The couple twirled like {p_noun_2} on the dance floor. 
        Everyone joined in, forming a {shape} around the happy pair. By the end of the night, 
        even the {adjective_6} guests were up and {verb_2}-ING! 
        It was a {adjective_7} day full of {p_noun_3}, laughter, and {p_noun_4}. 
        As the couple left for their {adjective_8} honeymoon, everyone waved their {p_noun_5}. 
       """
    
    print(text)

mad_lib()

input('\nPress ENTER to exit.')