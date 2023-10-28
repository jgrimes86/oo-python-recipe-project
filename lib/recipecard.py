class RecipeCard:

    all = []

    def __init__(self, user, recipe, date, rating):
        self.user = user
        self.recipe = recipe
        self.date = date
        self.rating = rating
        RecipeCard.all.append(self)
    
    def __repr__(self):
        return f"<RecipeCard user={self.user.name}, recipe={self.recipe.name}>"