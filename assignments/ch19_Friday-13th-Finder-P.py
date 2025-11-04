#ch19_Friday-13th-Finder-P

import datetime

def find_past_fridays():
    cur_date = datetime.datetime.now()
    date = cur_date
    delta = datetime.timedelta(days=1)
    spooky = []
    while date.year > 0:
        if date.weekday() == 4 and date.day == 13:
            pretty_date = date.strftime("%B %d, %Y")
            spooky.append(pretty_date)
        date = date - delta

    print("Here are the friday the 13ths in the past:")
    for i in spooky:
        print(i)