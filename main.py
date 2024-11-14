from recipe import *
from crud import *
from add_recipe_page import *
from ingredient import *
from connection import *
from create_script_from_js_file import *
from create_style_from_css_file import *
import sqlite3
import os
from flask import Flask, url_for, request, Response

app = Flask(__name__)
cur,conn = connect_to_recipe_db()

# egg_id = insert_ingredient(Ingredient(name="Egg", primary_category="Dairy and Eggs"))
# egg = select_ingredient(egg_id)
# scrambled_eggs = Recipe(title="Scrambled Eggs",ingredients=[egg],recipe_text="Heat pan on medium\ncrack eggs into bowl\nstir eggs\npour into pan\nstir in pan until 80% of desired consistency\nseason with salt and pepper and remove from heat\n")
# insert_recipe_object(scrambled_eggs)




def html_head_construction():
    script_url = url_for('static', filename = 'test_script.js')
    script = f"<script src='{script_url}'></script>"
    css_url = url_for('static', filename = 'styles.css')
    css = f'<link rel="stylesheet" href="{css_url}">'
    head = f"<Head>{script}{css}</Head>"
    return head
    
    

@app.route("/all_ingredients")
def get_all_ingredients():
    ingredients = select_all_ingredients()
    ingredients_json = str(list(map(lambda x: {"id":x.id, "name":x.name, "primary_category": x.primary_category},ingredients))).replace("'", '"')
    return Response(ingredients_json, status=200, mimetype='application/json')


@app.route("/add_dummy_item")
def add_dummy_recipe():
    egg = select_ingredient(1)
    egg.unit = 'Whole Size 7'
    egg.quantity = 3
    scrambled_eggs = Recipe(title="Scrambled Eggs 2",ingredients=[egg],recipe_text="Just shake the eggs up")
    insert_recipe_object(scrambled_eggs)
    return "done"

@app.route("/add_ingredient", methods=["POST"])
def add_ingredient_route():
    name = request.form['name']
    primary_category = "other"
    print(name)
    try:
        insert_ingredient(Ingredient(name=name, primary_category=primary_category))
        return Response("{}", status=201, mimetype='application/json')
    except:
        return Response("{}", status=400, mimetype='application/json')

@app.route("/delete_dummies")
def delete_dummies():
    dummies = cur.execute('select id from recipe where title ="Scrambled Eggs 2"').fetchall()
    for dummy in dummies:
        delete_recipe_object(dummy[0])
    return "done"


@app.route("/")
def home():
    recipes = select_all_recipes()
    return f"<html>{html_head_construction()}<body onload='add_initial_dropdown()'><p>{html_all_recipes(recipes)}<p>\
            <p><b>Add a New Recipe</b></p>\
             <p>{html_add_recipe_form()}</p>\
            <p><b>Add a Ingredient</b></p>\
             <p>{html_add_ingredient_form()}</p></body></html>"

