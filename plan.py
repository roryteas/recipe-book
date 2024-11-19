from recipe import *
from ingredient import *

class Plan:

    def __init__(self, meal_list: [Recipe] = []):
        self.meal_list = meal_list

    def sum_ingredient_totals(self):
        ingredient_sums = {}
        ingredient_list: [Ingredient] = []
        for recipe in self.meal_list:
            ingredient_list += recipe.ingredients
        for ingredient in ingredient_list:
            if ingredient.id in ingredient_sums:
                if ingredient.unit in ingredient_sums[ingredient.id]['unit']:
                    ingredient_sums[ingredient.id]['unit'][ingredient.unit] += ingredient.quantity
                else:
                    ingredient_sums[ingredient.id]['unit'][ingredient.unit] = ingredient.quantity
            else:
                ingredient_sums[ingredient.id] = {'name': ingredient.name, 'unit':{ingredient.unit: ingredient.quantity}}

        return ingredient_sums

            

