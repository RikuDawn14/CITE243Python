# Ch 17 PDF Password Breaker

# Use dictionary file provided in 'PythonBookPrograms' folder 'dictionary.txt'
# Use PDF file provided in 'PythonBookPrograms' folder 'Recursion_Chapter1_Crypt.pdf'
# PW- Parametrized

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


import time
import os
import pypdf
from tqdm import tqdm


def user_in():
    
    while True:
        dic_path = input("Please enter the path to your dictionary file for attack then hit ENTER.\n\t=> ")
        if not os.path.exists(dic_path):
            print(f"The path [{dic_path}] is not valid. Please check path and try again.")
            time.sleep(1)
        else:
            break

    with open(dic_path, 'r') as dictionary:
        lower_dic = dictionary.read().splitlines()
        upper_dic = [word.upper() for word in lower_dic]
        title_dic = [word.title() for word in lower_dic]
        dic_list = lower_dic + title_dic + upper_dic
    
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
    list_len = len(dic_list)
    pbar = tqdm(total=list_len, unit="PW", dynamic_ncols=True)
    reader = pypdf.PdfReader(pdf_file)
    while loop < list_len:
        pass_type = reader.decrypt(dic_list[loop]).name
        if pass_type == "NOT_DECRYPTED":
            loop += 1
            pbar.update(1)
        else:
            pbar.update(list_len - loop)
            time.sleep(.5)
            break
    pbar.close()
    if pass_type == "NOT_DECRYPTED":
        print(f"{pass_type}: None of the passwords in the list worked.")
    else:
        print(f"The password [{dic_list[loop]}] decrypted the file. It was a [{pass_type}].")



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