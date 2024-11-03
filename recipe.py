class Recipe:

    def __init__(self, id = None, title = "", ingredients = [], recipe_text = ""):
        self.id = id
        self.title = title
        self.ingredients = ingredients
        self.recipe_text = recipe_text

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def set_recipe_text(self, recipe_text):
        self.recipe_text = recipe_text

    def __repr__(self):
        ingredient_string = list(map(lambda x: x.name, self.ingredients))
        return f"Recipe Object(\n{self.title}\n Ingredients: {ingredient_string}\n recipe_text: {self.recipe_text}\n)"
