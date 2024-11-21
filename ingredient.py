class Ingredient:
    def __init__(self, id = None, name= "", primary_category = None, unit = "g", quantity=0):
        
        self.id = id
        self.name = name
        self.unit = unit
        self.quantity = quantity
        self.primary_category = primary_category

    def set_name(self, name):
        self.name = name

    def set_primary_Category(self, category):
        self.primary_category = category

    def __repr__(self):
        return f"Ingredient Object(\n{self.name}\nCategory: {self.primary_category}\n)"
