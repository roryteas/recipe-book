#i
def html_add_ingredient_form():
    script = create_script("ingredient_form.js")
    form = '<form onload="()=>add_initial_dropdown()" action ="javascript:void(0);" onsubmit="ingredient_form_submit()" name="ingredient_form">\
      <label for="name">Ingredient Name:</label><br>\
  <input type="text" id="name" name="name" placeholder="type ingredient here"><br>\
  <input type="submit" value="Submit">\
</form>'
    return script + form
