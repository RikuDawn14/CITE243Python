# Collatz function assignment

# Collatz function
def collatz(numb):
    while numb != 1:
        if numb % 2 == 0:
            numb = numb // 2
        else:
            numb = numb * 3 + 1
        print(numb)

# User input for number to use for function
while True:
    try: 
        user_input = int(input('Enter a whole number:'))
        if user_input < 1:
            print('Why so negative? Try being positive!')
        else:
            break # Stops the loop if a valid number is input
    except ValueError:
        print('Use a whole number please.')

collatz(user_input)
input('Press ENTER to exit.')
