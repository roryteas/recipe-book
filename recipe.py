class Recipe:

    def __init__(self, id = None, title = "", ingredients = None, recipe_text = ""):
        self.id = id
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []
        self.recipe_text = recipe_text

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def set_recipe_text(self, recipe_text):
        self.recipe_text = recipe_text

    def __repr__(self):
        return f"Recipe Object (\n id:{self.id}\n\n title: {self.title}\n\n ingredients:  {list(map(lambda x: x.name, self.ingredients))}\n\n recipe_text:\n  {self.recipe_text}\n)"
