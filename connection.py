import sqlite3
def connect_to_recipe_db():
    try:
        with sqlite3.connect("recipe-book.db") as conn:
            cur = conn.cursor()
            return cur
    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
