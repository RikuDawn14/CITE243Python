#ch19_Friday-13th-Finder-F

import datetime

### Function to find next 10 Friday 13ths ###
def find_future_fridays():
    loop = 0
    cur_date = datetime.datetime.now() # Gets current date and time to work from
    date = cur_date # pretty much useless variable change
    delta = datetime.timedelta(days=1) # Change date by one day
    spooky = [] # List of Friday the 13th's
    while loop < 10: # Loop until 10 matches found
        if date.weekday() == 4 and date.day == 13: # if weekday is 4(Friday) AND day of month is 13
            pretty_date = date.strftime("%B %d, %Y") # make a better readable date
            spooky.append(pretty_date) # Add date to list
            loop += 1 
        date = date + delta # add one day to date

    print("Here are the next ten Friday the 13ths:")
    for i in spooky: # Prints list
        print(i)

### Used for testing. Runs script if script is run directly ###
if __name__ == "__main__":
    find_future_fridays()