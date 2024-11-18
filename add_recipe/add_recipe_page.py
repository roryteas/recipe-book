from recipe import *
from create_script_from_js_file import *

def html_recipe_block(recipe: Recipe):
    ingredients_block = f"<ul>{''.join(list(map(lambda x: f"<li>{x.name} - {x.quantity} x {x.unit}</li>", recipe.ingredients)))}</ul>"

    return f"<div><b>{recipe.title}</b><br><p><b>Ingredients</b><br>{ingredients_block}</p><p>{recipe.recipe_text}</p></div>"

def html_all_recipes(recipes: [Recipe]):
    text = ""
    for recipe in recipes:
        text += html_recipe_block(recipe)
    text = text.replace('\n', '<br>')
    print('got all recipes')
    return text



def html_add_recipe_form():
    script = create_script("recipe_form.js")
    form = '<form id="recipe_form" >\
      <label for="title">Recipe title:</label><br>\
  <input type="text" id="title" name="title" value="Chicken Biriyani">\
      <p>Ingredients</p>\
    <table id="RecipeIngredientLabel">\
        <thead><td>Ingredient</td><td>Unit</td><td>Amount</td></thead>\
    </table>\
  <label id="method_text" for="recipe_text">Recipe Method text:</label><br>\
  <textarea type="text" id="recipe_text" name="recipe_text" value="make the biriyani real good"></textarea><br><br>\
  <button onclick="submit_recipe()" type="button">Add Recipe</button>\
</form>'
    return script + form

def html_add_ingredient_form():
    script = create_script("ingredient_form.js")
    form = '<form onload="()=>add_initial_dropdown()" action ="javascript:void(0);" onsubmit="ingredient_form_submit()" name="ingredient_form">\
      <label for="name">Ingredient Name:</label><br>\
  <input type="text" id="name" name="name" placeholder="type ingredient here"><br>\
  <input type="submit" value="Submit">\
</form>'
    return script + form
