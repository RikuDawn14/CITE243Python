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

# Function to give feedback on the password issues.
def detail(password):

    results = {
        checker(password): False,
        'length_short': len(password) >= 8,
        'length_long': len(password) <= 20,
        'has_lower': bool(re.search(r'[a-z]', password)),
        'has_upper': bool(re.search(r'[A-Z]', password)),
        'has_special': bool(re.search(r'[@$#%]', password)),
        'has_numb': bool(re.search(r'\d', password)),
        }
    
    if not results['length_short']:
        print("\nPassword is to short.\n")
    if not results['length_long']:
        print("\nPassword too long.\n")
    if not results['has_lower']:
        print("\nNeed lower case\n")
    if not results['has_upper']:
        print("\nNeed upper\n")
    if not results['has_special']:
        print("\nNeed special character\n") 
    if not results['has_numb']:
        print("\nNeed number\n")



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


