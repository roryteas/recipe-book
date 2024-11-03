class Ingredient:
    def __init__(self, id = None, name= "", primary_category = None):
        
        self.id = id
        self.name = name
        self.primary_category = primary_category

    def set_name(self, name):
        self.name = name

    def set_primary_Category(self, category):
        self.primary_category = category

    def __repr__(self):
        return f"Ingredient Object(\n{name}\nCategory: {primary_category}\n)"
