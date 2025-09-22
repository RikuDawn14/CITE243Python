# Chapter 9 (TEXT PATTERN MATCHING WITH REGULAR EXPRESSIONS) Assignment

import re

# Function to check password strength.
def checker(password):

    pattern = re.compile(r'''(
         ^(?=.*[a-z])               # Check for lower
          (?=.*[A-Z])               # Check for upper
          (?=.*\d)                  # Check for number
          (?=.*[@$#%])              # Check for special 
          [A-Za-z\d@$#%]{8,20}$     # Check length       
        
        )''', re.VERBOSE)

    return bool(re.match(pattern, password))

def detail(password):

    results = {
        checker(password): False,
        'length_ok': len(password) >= 8,
        'has_lower': bool(re.search(r'[a-z]', password)),
        'has_upper': bool(re.search(r'[A-Z]', password)),
        'has_special': bool(re.search(r'[@$#%]', password)),

    }
    



# Function to get user input password.
def password_input():
    
    while True:
        password = input('Please enter a password to check security, then hit ENTER. \n=>')
    
        if len(password) == 0:
            print("\nYou didn't enter a password! Try again.\n")
            continue

            
        if checker(password) == True:
            print("Good")
            break

        else:
            print('no')
            detail(password)

            


password_input()

input('Press ENTER to exit.')


