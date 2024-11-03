from recipe import *
from crud import *
import sqlite3
import os

script = [] 

if not os.path.isfile('recipe-book.db'):
    with open('table_definitions.sql', 'r') as sql_file:
        print('creatingg tables')
        script = sql_file.readlines()
        

try:
    with sqlite3.connect("recipe-book.db") as conn:
        print('connected')
        cur = conn.cursor()
        for line in script:
            print(line)
            cur.execute(line)
except sqlite3.OperationalError as e:
    print("Failed to open database:", e)



def main():
    r = Recipe(title="Scrambled Eggs",recipe_text="crack eggs into bowl and whisk\ncook them suckers\nseason.")

    insert_recipe(r)
    res = select_all_recipes()
    for item in res:
        delete_recipe(item.id)
if __name__ == "__main__":
    main()
