from recipe import *
from ingredient import *
from datetime import datetime, timedelta

class Plan:

    def __init__(self,id= None, name = None, meal_list: [Recipe] = [], start_date = None, end_date=None):
        self.id = id
        self.name = name
        self.meal_list = meal_list
        self.start_date = start_date
        self.end_date = end_date
        if self.start_date == None:
            self.start_date = datetime.today()
        if self.end_date == None:
            self.end_date = self.start_date + timedelta(days=6)

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

    def __repr__(self):
        return f'id:{self.id}, name:{self.name}, start: {self.start_date}, end: {self.end_date}, meal list: {self.meal_list}'
