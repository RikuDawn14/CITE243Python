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
import os
import pypdf


def user_in():
    
    while True:
        dic_path = input("Please enter the path to your dictionary file for attack then hit ENTER.\n\t=> ")
        if not os.path.exists(dic_path):
            print(f"The path [{dic_path}] is not valid. Please check path and try again.")
            time.sleep(1)
        else:
            break

    with open(dic_path, 'r') as dictionary:
        dic_list = dictionary.read().splitlines()
    
    while True:
        pdf_file = input("Please enter the path to the protected PDF file to attack.\n\t=> ")
        if not os.path.exists(pdf_file):
            print(f"The path [{pdf_file}] is not valid. Please check path and try again.")
            time.sleep(1)
        else:
            break
    confirm(dic_list, pdf_file)

def confirm(dic_list, pdf_file):
    print("*" * 60)
    print("WARNING".center(60))
    print("The following attack may take a while to complete.".center(60))
    print("*" * 60)
    confirm = input("\nAre you sure you would like to continue? [Y/N]\n\t=> ").strip().lower()
    if confirm == "y":
        attack(dic_list, pdf_file)
    else:
        return

def attack(dic_list, pdf_file):
    loop = 0
    reader = pypdf.PdfReader(pdf_file)
    while reader.is_encrypted == True:
        pass_type = reader.decrypt(dic_list[loop]).name
        if pass_type == "NOT_DECRYPTED":
            loop += 1
        else:
            break
    print(f"The password [{dic_list[loop]}] decrypted the file. It was a [{pass_type}].")
    save(reader)

def save(reader):
    writer = pypdf.PdfWriter()
    save_in = input("Would you like to save a decypted version of the PDF? [Y/N]\n\t=> ").strip().lower()
    if save_in != "y":
        return
    else:
        new_name = input("What would you like to name the decrypted PDF?\n\t=> ")
        writer.append(reader)
        with open(new_name, 'wb') as file:
            writer.write(file)





### Start of program ###
print("=" * 60)
print("PDF Password Dictionary Attack".center(60))
print("=" * 60)

start = input("\nPress 'Y' then hit ENTER to continue.\nOtherwise enter any key or leave blank and hit ENTER to exit.\n\t=> ").strip().lower()
if start == "y":
    print("\n---PROGRAM STARTING---\n")
    time.sleep(.5)
    user_in()

else:
    time.sleep(.5)

print("\n---EXITING PROGRAM---\n")
input("Press ENTER to exit.")