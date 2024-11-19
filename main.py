from recipe import *
from crud import *
from add_recipe_page import *
from ingredient import *
from connection import *
from create_script_from_js_file import *
from create_style_from_css_file import *
import sqlite3
import os
import json
from flask import Flask, url_for, request, Response

app = Flask(__name__)
cur,conn = connect_to_recipe_db()

# egg_id = insert_ingredient(Ingredient(name="Egg", primary_category="Dairy and Eggs"))
# egg = select_ingredient(egg_id)
# scrambled_eggs = Recipe(title="Scrambled Eggs",ingredients=[egg],recipe_text="Heat pan on medium\ncrack eggs into bowl\nstir eggs\npour into pan\nstir in pan until 80% of desired consistency\nseason with salt and pepper and remove from heat\n")
# insert_recipe_object(scrambled_eggs)



def html_page_construction(script="test_script.js",css='styles.css',inner_html='', onload=''):
    script_url = url_for('static', filename = script)
    script = f"<script src='{script_url}'></script>"
    css_url = url_for('static', filename = css)
    css = f'<link rel="stylesheet" href="{css_url}">'
    favicon = f"<link rel='shortcut icon' href={ url_for('static', filename='favicon.ico') }>"
    head = f"<Head>{script}{css}{favicon}</Head>"
    return f"<html>{head}<body onload={onload}>{inner_html}</body></html>"
    

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

@app.route("/add_recipe", methods=["POST"])
def add_recipe_route():
    recipe_json = json.loads(request.form['recipe'])
    ingredients = list(map(lambda x: Ingredient(id=x['id'], unit=x['unit'], quantity= x['quantity']),recipe_json["ingredients"]))
    title = recipe_json["title"]
    text = recipe_json["recipe_text"]
    recipe = Recipe(title=title, ingredients=ingredients, recipe_text=text)
    try:
        insert_recipe_object(recipe)
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
    return html_page_construction(inner_html=html_all_recipes(recipes))
                 


@app.route("/add_recipe")
def add_recipe_page():
    return html_page_construction(inner_html=html_add_recipe_form(),onload='add_initial_dropdown()')
            

