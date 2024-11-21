import unittest

from recipe import *
from ingredient import *
from plan import *
from crud import *

class TestPlan(unittest.TestCase):

    recipe_t = Recipe(id=5, title="test", recipe_text = "test recipe text")
    ingred_t = Ingredient(id=4, name="test", primary_category="test cat", quantity=100)
    recipe_t.add_ingredient(ingred_t)
    plan = Plan(name= 'test_plan', meal_list=[recipe_t, recipe_t])
    def test_create_plan(self):
        
        self.assertEqual(self.plan.meal_list[0], self.recipe_t)

    def test_sum_ingredients(self):
        
        ingredient_sums = self.plan.sum_ingredient_totals()
        self.assertEqual(ingredient_sums[4]['unit']['g'], 200)


