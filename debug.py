from lib.allergy import Allergy
from lib.ingredient import Ingredient
from lib.recipe import Recipe
from lib.recipecard import RecipeCard
from lib.recipeingredient import RecipeIngredient
from lib.user import User
# from lib import *

# code here

# e.g.  
    # a1 = Allergy( ??? )
    # i1 = Ingredient( ??? )
    # r1 = Recipe( ??? )
    # rc1 = RecipeCard( ??? )
    # ri1 = RecipeIngredient( ??? )
    # u1 = User( ??? )

cake = Recipe("cake")
bread = Recipe("bread")
mac_and_cheese = Recipe("mac and cheese")
pasta = Recipe("pasta")
cereal = Recipe("cereal")

jim = User("Jim")
mark = User("Mark")
pete = User("Pete")
amy = User("Amy")

rc1 = RecipeCard(jim, cake, "2020-08-12", 5)
rc2 = RecipeCard(mark, bread, "2015-09-04", 6)
rc3 = RecipeCard(pete, bread, "2023-04-28", 4)
rc4 = RecipeCard(mark, cake, "2018-05-12", 5)
rc5 = RecipeCard(amy, cake, "2021-11-04", 7)
rc6 = RecipeCard(amy, mac_and_cheese, "2021-01-02", 50)
rc7 = RecipeCard(amy, pasta, "2023-10-16", 6)
rc8 = RecipeCard(amy, cereal, "1998-08-30", 4)

flour = Ingredient("flour")
sugar = Ingredient("sugar")
eggs = Ingredient("eggs")
milk = Ingredient("milk")
cheddar = Ingredient("cheddar cheese")
parmesan = Ingredient("parmesan cheese")

ri1 = RecipeIngredient(flour, cake)
ri2 = RecipeIngredient(sugar, cake)
ri3 = RecipeIngredient(eggs, cake)
ri4 = RecipeIngredient(milk, cake)
ri5 = RecipeIngredient(flour, bread)
ri6 = RecipeIngredient(milk, bread)

a1 = Allergy(eggs, jim)
a2 = Allergy(milk, mark)
a3 = Allergy(cheddar, mark)
a4 = Allergy(parmesan, mark)
a5 = Allergy(eggs, amy)

# your code above!
import ipdb; ipdb.set_trace()