from ingredient import *
from recipe import *


def html_add_plan_form():
    script = create_script("plan_form.js")
    form = '\
    <form id="plan_form" >\
      <label for="title">Plan title:</label><br>\
      <input type="text" id="title" name="title" value="Plan name">\
      <div id="plan_container"> \
      </div>\
      <button onclick="submit_plan()" type="button">Add Plan</button>\
    </form>'
    return script + form
