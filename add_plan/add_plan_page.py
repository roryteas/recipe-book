from ingredient import *
from recipe import *
from create_script_from_js_file import *

def html_add_plan_form():
    script = create_script("add_plan/plan_form.js")
    form = '\
    <form id="plan_form" >\
      <label for="title">Plan title:</label><br>\
      <input type="text" id="title" name="title" value="Plan name">\
      <div id="plan_container"> \
      </div>\
      <button onclick="add_plan_fieldset()" type="button">Add Recipe Slot</button>\
      <br/>\
      <br/>\
      <button onclick="submit_plan()" type="button">Add Plan</button>\
    </form>'
    return script + form
