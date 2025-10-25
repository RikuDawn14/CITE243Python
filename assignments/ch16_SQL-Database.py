# Chapter 16 SQLite Databases Assignment

"""
===========================================================
Program Name: ch16 SQL Database
Author: Matthew Balthaser
Date: 2025-10-26
Description:
    This program creates tables in an SQL DB.
    It is designed to make tables to list meals and ingredients for those meals.
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.
===========================================================
"""

import time
import sqlite3
import textwrap


def table():
    conn = sqlite3.connect('meals.db', isolation_level=None)
    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute('CREATE TABLE IF NOT EXISTS meals (id INTEGER PRIMARY KEY, name TEXT NOT NULL) STRICT')
    conn.execute('CREATE TABLE IF NOT EXISTS ingredients (name TEXT, meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals(id)) STRICT')
    curs = conn.cursor()
    option = ""
    while option != "EXIT":
        option = input("Please select what would you like to do?\n-Add meal (N)\n-Search names (S)\n-Exit (EXIT)\n\t=> ").strip().upper()
        if option == 'N':
            instuction = textwrap.dedent("""
                        Please enter a new meal followed by the ingredients needed using this format,
                        <Meal name>: <ingredient1>, <ingredient2>, etc.
                        Pay close attention to the colon (:) and comma (,) placements.
                        Leave blank to go back.
                        """)
            print(instuction)
            addition = input("\t=> ")
            if not addition:
                continue
            else:
                first_split = addition.split(":")
                meal_name = first_split[0].strip()
                ingred_sting = first_split[1]
                ingred_list = ingred_sting.split(",")
                num_ingred = len(ingred_list)
                loop = 0
                curs.execute("INSERT INTO meals (name) VALUES (?)", (meal_name,))
                meal_row = curs.lastrowid
                while loop < num_ingred:
                    ingred_name = ingred_list[loop]
                    curs.execute("INSERT INTO ingredients VALUES (?, ?)", (ingred_name, meal_row))
                    loop += 1
                conn.commit()
                
                print(f"Added {meal_name} to meals table and the following ingredients have been added to the ingredients table.")
                for items in ingred_list:
                    print(items)
                    print("=" * 60)
        
        elif option == 'S':
            search_term = input("What name (meal or ingredient) would you like to search for?\nLeave blank to go back.\n\t=> ")
            if not search_term:
                continue
            else:
                curs.execute("SELECT name FROM meals WHERE name = ?", (search_term,))
                results = curs.fetchall()
                if results:
                    curs.execute("SELECT ingredients.name FROM meals JOIN ingredients ON ingredients.meal_id = meals.rowid WHERE meals.name = ?", (search_term,))
                    meal_results = curs.fetchall()
                    for items in meal_results:
                        print("The following ingredients are used in that meal.")
                        print(items[0])
                        print("=" * 60)

                else:
                    curs.execute("SELECT meals.name FROM ingredients JOIN meals ON ingredients.meal_id = meals.rowid WHERE ingredients.name = ?", (search_term,))
                    ingred_results = curs.fetchall()
                    for items in ingred_results:
                        print("That ingerdient is used in these meals.")
                        print(items[0])
                        print("=" * 60)

        else:
            if option != "EXIT":
                print(f"{option} is not a valid option try again.")

### Start of program ###
print("=" * 60)
print("Meal/Ingredients Database".center(60))
print("=" * 60)

start = input("\nPress 'Y' then hit ENTER to continue.\nOtherwise enter any key or leave blank and hit ENTER to exit.\n\t=> ").strip().lower()
if start == "y":
    print("\n---PROGRAM STARTING---\n")
    time.sleep(.5)
    table()

else:
    time.sleep(.5)

print("\n---EXITING PROGRAM---\n")
input("Press ENTER to exit.")



