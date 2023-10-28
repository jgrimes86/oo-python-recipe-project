class RecipeIngredient:

    all = []

    def __init__(self, ingredient, recipe):
        self.ingredient = ingredient
        self.recipe = recipe
        RecipeIngredient.all.append(self)

    def __repr__(self):
        return f"<RecipeIngredient ingredient={self.ingredient.name}, recipe={self.recipe.name}>"
    