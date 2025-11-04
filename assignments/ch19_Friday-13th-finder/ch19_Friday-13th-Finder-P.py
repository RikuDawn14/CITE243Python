#ch19_Friday-13th-Finder-P

import datetime

### Function to find all past Friday the 13th's ###
def find_past_fridays():
    cur_date = datetime.datetime.now() # Gets current date and time to work from
    date = cur_date # pretty much useless variable change
    delta = datetime.timedelta(days=1) # Change date by one day
    spooky = [] # List of Friday the 13th's
    while date.year > 1: # loop until the year is 1
        if date.weekday() == 4 and date.day == 13: # if weekday is 4(Friday) AND day of month is 13
            pretty_date = date.strftime("%B %d, %Y") # make a better readable date
            spooky.append(pretty_date) # Add date to list
        date = date - delta # subtract one day to date

    total = len(spooky) # finds total number found
    print(f"There were [{total}] Friday the 13th's in the past.") # Prints total
    print("Here are the last ten Friday the 13th's:") 
    for i in range(10): # Prints first ten dates on list, also happens to be most recent dates
        print('-' + spooky[i])

### Used for testing. Runs script if script is run directly ###
if __name__ == "__main__":
    find_past_fridays()