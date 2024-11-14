create table recipe(id INTEGER PRIMARY KEY AUTOINCREMENT, title text, recipe_text text)
create table ingredient(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, primary_category text)
create table recipe_ingredient(recipe_id INTEGER, ingredient_id INTEGER, ingredient_unit varchar(10), ingredient_quantity FLOAT, PRIMARY KEY (recipe_id, ingredient_id),FOREIGN KEY (recipe_id) REFERENCES recipe(id),FOREIGN KEY (ingredient_id) REFERENCES ingredient(id))
