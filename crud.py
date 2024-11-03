from connection import *
from recipe import *

cur = connect_to_recipe_db()

#create
def insert_recipe_object(recipe):
    
    insert_recipe(recipe)
    recipe_id = cur.lastrowid()
    
    for ingredient in recipe.ingredients:
        insert_recipe_ingredient(recipe_id, ingredient.id)

def insert_recipe_ingredient(recipe_id,ingredient_id):
    return cur.execute(f'insert into recipe_ingredient (recipe_id, ingredient_id) values ({recipe_id}, {ingredient_id}')

def insert_recipe(recipe):
    return cur.execute(f'insert into recipe (title, recipe_text) values ("{recipe.title}", "{recipe.recipe_text}")')

def insert_ingredient(ingredient):
    return cur.execute(f'insert into ingredient (name, primary_category) values ("ingredient.name","ingredient.primary_category")')

#read
def select_recipe_object(recipe_id):
    
    recipe_o = select_recipe(id)
    res = cur.execute(f'select i.id, i.name, i.primary_category from ingredient as i left join recipe_ingredient as ri on i.id = ri.ingredient_id where ri.recipe_id = {recipe_id}')
    ingredients = list(map(lambda x: Ingredient(id=x[0], name=x[1], primary_category=x[2])))


def select_recipe(recipe_id):
    res = cur.execute(f"select id, title, recipe_text from recipe where id = {recipe_id}")
    return Recipe(id = res[0], title = res[1], recipe_text = res[2])

def select_ingredient(ingredient_id):
    res = cur.execute(f'select id, name, primary_category from ingredient where id = {ingredient_id}').fetchone()
    return Ingredient(id = res[0], name = res[1], primary_category = res[2])

def select_all_recipes():
    res = cur.execute(f"select id, title, recipe_text from recipe").fetchall()
    return list(map(lambda x: Recipe(id=x[0], title=x[1], recipe_text=x[2]),res))

def select_all_ingredients():
    res = cur.execute(f"select id, name, primary_category from ingredient").fetchall()
    return list(map(lambda x: Ingredient(id=x[0], name=x[1], primary_category=x[2]),res))

#update

#delete

def delete_recipe(id):
    return cur.execute(f"delete from recipe where id = {id}")
