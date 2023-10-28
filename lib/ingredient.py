from .recipeingredient import RecipeIngredient
from .allergy import Allergy

class Ingredient:
    
    all = []

    def __init__(self, name):
        self.name = name
        Ingredient.all.append(self)
    
    def __repr__(self):
        return f"<Ingredient name={self.name}>"

    @classmethod
    def most_common_allergen(self):
        all_allergies = [allergy.ingredient for allergy in Allergy.all]
        common_allergy = []
        allergy_count = 0
        for ingredient in all_allergies:
            if all_allergies.count(ingredient) > allergy_count:
                common_allergy = ingredient
                allergy_count = all_allergies.count(ingredient)
        return common_allergy
    
