from .recipecard import RecipeCard
from .allergy import Allergy

class User:

    all = []

    def __init__(self, name):
        self.name = name
        User.all.append(self)
    
    def __repr__(self):
        return f"<User name={self.name}>"

    def recipes(self):
        return [rc.recipe for rc in RecipeCard.all if rc.user == self]

    def add_recipe_card(self, recipe, date, rating):
        RecipeCard(self, recipe, date, rating)

    def declare_allergy(self, ingredient):
        Allergy(ingredient, self)

    def allergens(self):
        return [allergy for allergy in Allergy.all if allergy.user == self]

    def top_three_recipes(self):
        recipe_cards = [rc for rc in RecipeCard.all if rc.user == self]
        sorted_recipes = sorted(recipe_cards, key=lambda card: card.rating, reverse=True)
        return [rc.recipe for rc in sorted_recipes][0:3]

    def most_recent_recipe(self):
        recipe_cards = [rc for rc in RecipeCard.all if rc.user == self]
        sort_by_date = sorted(recipe_cards, key=lambda rc: rc.date, reverse=True)
        return sort_by_date[0]