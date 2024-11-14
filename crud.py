from connection import *
from recipe import *
from ingredient import *
cur,conn = connect_to_recipe_db()

#create
def insert_recipe_object(recipe):
    
    insert_recipe(recipe)
    recipe_id = cur.lastrowid
    for ingredient in recipe.ingredients:
        insert_recipe_ingredient(recipe_id, ingredient.id, ingredient.unit, ingredient.quantity)

def insert_recipe_ingredient(recipe_id,ingredient_id, ingredient_unit, ingredient_quantity):
    cur.execute(f'insert into recipe_ingredient (recipe_id, ingredient_id, ingredient_unit, ingredient_quantity) values ({recipe_id}, {ingredient_id}, "{ingredient_unit}", {ingredient_quantity})')
    conn.commit()
    return cur.lastrowid

def insert_recipe(recipe):
    cur.execute(f'insert into recipe (title, recipe_text) values ("{recipe.title}", "{recipe.recipe_text}")')
    conn.commit()
    return cur.lastrowid

def insert_ingredient(ingredient):
    cur.execute(f'insert into ingredient (name, primary_category) values ("{ingredient.name}","{ingredient.primary_category}")')
    conn.commit()
    return cur.lastrowid

#read
def select_recipe_object(recipe_id):
    
    recipe_o = select_recipe(recipe_id)
    res = cur.execute(f'select i.id, i.name, i.primary_category, ri.ingredient_unit, ri.ingredient_quantity from ingredient as i left join recipe_ingredient as ri on i.id = ri.ingredient_id where ri.recipe_id = {recipe_id}')
    ingredients = list(map(lambda x: Ingredient(id=x[0], name=x[1], primary_category=x[2], unit=x[3], quantity=x[4]),res.fetchall()))
    recipe_o.ingredients = ingredients
    
    return recipe_o

def select_recipe(recipe_id):
    res = cur.execute(f"select id, title, recipe_text from recipe where id = {recipe_id}").fetchone()
    return Recipe(id = res[0], title = res[1], recipe_text = res[2])

def select_ingredient(ingredient_id):
    res = cur.execute(f'select id, name, primary_category from ingredient where id = {ingredient_id}').fetchone()
    return Ingredient(id = res[0], name = res[1], primary_category = res[2])

def select_all_recipes():
    res = cur.execute(f"select id, title, recipe_text from recipe").fetchall()
    return list(map(lambda x: select_recipe_object(x[0]) ,res))

def select_all_ingredients():
    res = cur.execute(f"select id, name, primary_category from ingredient").fetchall()
    return list(map(lambda x: Ingredient(id=x[0], name=x[1], primary_category=x[2]),res))

#update

#delete

def delete_recipe(id):
    cur.execute(f"delete from recipe where id = {id}")
    conn.commit()
    return cur.lastrowid

def delete_recipe_object(id):
    delete_recipe(id)
    cur.execute(f"delete from recipe_ingredient where recipe_id = {id}")

