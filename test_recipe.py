import unittest

from recipe import *
from ingredient import *

class test_recipe(unittest.TestCase):
    
    def test_blank_recipe(self):

        r = Recipe()
        self.assertEqual(r.title,"")
        self.assertEqual(r.ingredients, [])
        self.assertEqual(r.recipe_text, "")
    
    def test_add_ingredients(self):
        
        recipe_t = Recipe(id=5, title="test", recipe_text = "test recipe text")
        ingred_t = Ingredient(id=4, name="test", primary_category="test cat")
        recipe_t.add_ingredient(ingred_t)
        self.assertTrue(ingred_t in recipe_t.ingredients)
        ingred_t2 = Ingredient(id = 6, name="test2", primary_category="test cat2")
        recipe_t.add_ingredient(ingred_t2)
        self.assertTrue(ingred_t2 in recipe_t.ingredients)
        self.assertTrue(ingred_t in recipe_t.ingredients)



