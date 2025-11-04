#ch19_Friday-13th-Finder-F

import datetime

def find_future_fridays():
    loop = 0
    cur_date = datetime.datetime.now()
    date = cur_date
    delta = datetime.timedelta(days=1)
    spooky = []
    while loop < 10:
        if date.weekday() == 4 and date.day == 13:
            pretty_date = date.strftime("%B %d, %Y")
            spooky.append(pretty_date)
            loop += 1
        date = date + delta

    print("Here are the next ten Friday the 13ths:")
    for i in spooky:
        print(i)

if __name__ == "__main__":
    find_future_fridays()