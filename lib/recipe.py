from .recipecard import RecipeCard
from .recipeingredient import RecipeIngredient
from .allergy import Allergy

class Recipe:

    all = []

    def __init__(self, name):
        self.name = name
        Recipe.all.append(self)

    def __repr__(self):
        return f"<Recipe name={self.name}>"

    @classmethod
    def most_popular(cls):
        all_recipes = [card.recipe for card in RecipeCard.all]
        popular_recipe = []
        recipe_count = 0
        for recipe in all_recipes:
            if all_recipes.count(recipe) > recipe_count:
                popular_recipe = recipe
                recipe_count = all_recipes.count(recipe)
        return popular_recipe
    
    def users(self):
        return [rc.user for rc in RecipeCard.all if rc.recipe == self]

    def ingredients(self):
        return [ri.ingredient for ri in RecipeIngredient.all if ri.recipe == self]

    def allergens(self):
        allergen_list = []
        for allergy in Allergy.all:
            if (allergy.ingredient not in allergen_list) and (allergy.ingredient in self.ingredients()):
                allergen_list.append(allergy.ingredient)
        return allergen_list

    def add_ingredients(self, ingredient_list):
        for ingredient in ingredient_list:
            RecipeIngredient(ingredient, self)


    