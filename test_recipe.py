import unittest

from recipe import *


class test_recipe(unittest.TestCase):

    def test_blank_recipe(self):

        r = Recipe()

        self.assertEqual(r.title,"")
        self.assertEqual(r.ingredients, [])
        self.assertEqual(r.recipe_text, "")
