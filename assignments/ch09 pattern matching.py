# Chapter 9 (TEXT PATTERN MATCHING WITH REGULAR EXPRESSIONS) Assignment

import re

# Function to check password strength.
def checker(password):

    pattern = re.compile(r'''(
         ^(?=.*[a-z])                   # Check for lower
          (?=.*[A-Z])                   # Check for upper
          (?=.*\d)                      # Check for number
          (?=.*[@$#%&*!?])              # Check for special 
          [A-Za-z\d@$#%&*!?]{8,20}$     # Check length       
        
        )''', re.VERBOSE)

    return bool(re.match(pattern, password))

# Function to give feedback on the password issues.
def detail(password):

    results = {
        'length_short': len(password) >= 8,
        'length_long': len(password) <= 20,
        'has_lower': bool(re.search(r'[a-z]', password)),
        'has_upper': bool(re.search(r'[A-Z]', password)),
        'has_special': bool(re.search(r'[@$#%&*!?]', password)),
        'has_numb': bool(re.search(r'\d', password)),
        }
    # Compares dictionary values to give user feedback on what issue they have.
    if not results['length_short']:
        print("- This password is shorter than my attention span!")
    if not results['length_long']:
        print("- How about we trim that down to at most a haiku?")
    if not results['has_lower']:
        print("- Time to let your password chill with some lowercase vibes!")
    if not results['has_upper']:
        print("- Hey there, lowercase lover! Your password needs a little upper-class attitude!")
    if not results['has_special']:
        print("- A password without a special character? That's like a party without music!") 
    if not results['has_numb']:
        print("- Your password is like a pie without filling; add a number!")



# Function to get user input password.
def password_input():
    
    print("=*" * 33 + "=")
    print("""
        =*=*=*=*=*= Password Strength Checker =*=*=*=*=*=
                          Requierements
        - 8-20 Characters long
        - At least 1 lowercase letter
        - At least 1 uppercase letter
        - At least 1 number
        - At least 1 special character (@$#%&*!?)
          """)
    print("=*" * 33 + "=")
    
    while True:
        password = input('\nPlease enter a password to check security, then hit ENTER.\n=>')
    
        if len(password) == 0:
            print("\nYou didn't even enter a password! Try again.\n")
            continue
            
        if checker(password) == True:
            print("\nYour password is like Colonel Sanders blend of 11 herbs and spices; it's a secret!\n")
            break

        else:
            print("\nWow, your password is as secure as a screen door on a submarine!\nHere is something, or things you should know.\n")
            detail(password)

            


password_input()

input('Press ENTER to exit.')


