#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
  # pass
    # possibleBatches = keep track of batches possible with the ingredients available
    # check to make sure that we at least have number of ingredients matching our recipe requirements
    # for each ingredient in recipe check if amount available in ingredients
    # divide ingredient total with recipe need, store in possibleBatches as int rounded down
    # if ingredient available is less than what recipe requires; return 0 possibleBatches
    possibleBatches = []
    if len(recipe) == len(ingredients):
        for item, recipeValue in recipe.items():
            for ingredient, ingredientValue in ingredients.items():
                if item == ingredient:
                    batchResult = math.floor(ingredientValue/recipeValue)
                    possibleBatches.append(batchResult)
        return min(possibleBatches)
    else:
        return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
