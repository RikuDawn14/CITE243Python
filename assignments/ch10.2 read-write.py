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
import re

# Function to read txt file to allow user to input words
def read_txt():

    file_path = input("\nEnter file path to Mad Lib txt file.\n =>")
    mad_lib = open(file_path, 'a', encoding='UTF-8')

    patter = re.compile(r'''(
              ^('ADJECTIVE')
              ('NOUN')
              ('VERB')
              ('COLOR')
              ('EMOTION')
              ('PLUARL_NOUN')
              ('SHAPE')$
              )''')

