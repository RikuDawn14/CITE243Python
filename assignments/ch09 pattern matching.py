# Chapter 9 (TEXT PATTERN MATCHING WITH REGULAR EXPRESSIONS) Assignment

import re

# Function to check password strength.
def checker():

    pattern = re.compile(r'''(
         ^(?=.*[a-z])
          (?=.*[A-Z])
          (?=.*\d)
          (?=.*[@$#%])
          [A-Za-z\d@$#%]
          {8,20}$            
        
        )''', re.VERBOSE)




# Function to get user input password.
def password_input():
    
    password = input('Please enter a password to check security, then hit ENTER. \n=>')

    if len(password) == 0:
        print("You didn't enter a password! Try again.")

    else:
        checker(password)





