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

with open(dic_path, 'r') as dictionary:
    dic_list = dictionary.read().splitlines()