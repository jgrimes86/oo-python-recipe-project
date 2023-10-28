class Allergy:

    all = []

    def __init__(self, ingredient, user):
        self.ingredient = ingredient
        self.user = user
        Allergy.all.append(self)

    def __repr__(self):
        return f"<Allergy user={self.user.name}, ingredient={self.ingredient.name}>"