#ch19_Friday-13th-Finder-P

import datetime

def find_past_fridays():
    cur_date = datetime.datetime.now()
    date = cur_date
    delta = datetime.timedelta(days=1)
    spooky = []
    while date.year > 1:
        if date.weekday() == 4 and date.day == 13:
            pretty_date = date.strftime("%B %d, %Y")
            spooky.append(pretty_date)
        date = date - delta

    total = len(spooky)
    print(f"There were [{total}] Friday the 13th's in the past.")
    print("Here are the last ten Friday the 13th's:")
    for i in range(10):
        print('-' + spooky[i])

if __name__ == "__main__":
    find_past_fridays()