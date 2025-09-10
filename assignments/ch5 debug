import random, logging
# logging.disable(logging.CRITICAL) # Uncomment line to stop all logging.
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# Get initail guess
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower() 
    if guess not in ('heads', 'tails'):
            logging.debug('Invalid first guess, prompting again')

# Generate random toss
logging.debug('Start of coin toss')
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# Convert toss to string for comparison
toss_result = 'tails' if toss == 0 else 'heads'

# Check first guess
logging.debug('Comparing first guess {' + guess + '} with toss result {' + toss_result + '}')
if toss_result == guess:
    logging.debug('First guess was correct!')
    print('You got it!')
else:
    print('Nope! Guess again!')
    
    # Second guess
    guess = ''
    while guess not in ('heads', 'tails'):
        guess = input().lower()
        if guess not in ('heads', 'tails'):
            logging.debug('Invalid second guess, prompting again')
        
    # Check second guess    
    logging.debug('Comparing second guess {' + guess + '} with toss result {' + toss_result + '}')
    if toss_result == guess:
        logging.debug('Second guess was correct!')
        print('You got it!')
    else:
        logging.debug('Second guess was also incorrect')
        print('Nope. You are really bad at this game.')

logging.debug('End of program')
