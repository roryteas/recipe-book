import sqlite3
def connect_to_recipe_db():
    try:
        with sqlite3.connect("recipe-book.db", check_same_thread=False) as conn:
            cur = conn.cursor()
            res = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name in('recipe','ingredient','recipe_ingredient')").fetchall()
            sql_file = open('table_definitions.sql')
            script = sql_file.readlines()
            if len(res) > 2:
                script = []
                print(script)
            for line in script:
                print(line)
                cur.execute(line)
            return cur, conn
    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
