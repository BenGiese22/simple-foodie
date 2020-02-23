import re

class Recipe:

    link = None
    title = None
    ingredients = None
    directions = None

    def __init__(self, link, title, ingredients, directions):
        if link is not None:
            self.link = link

        if title is not None:
            self.title = title

        if ingredients is not None:
            self.ingredients = ingredients
        
        if directions is not None:
            self.directions = directions

    def to_string(self):
        recipe_str = self.link + '     \n\n'
        recipe_str += self.title + '     \n\n'
        recipe_str += '     ' + 'Ingredients' + '     \n'
        recipe_str += '    -' + '-----------' + '-    \n'
        for ingredient in self.ingredients:
            recipe_str += ingredient + '\n'
        recipe_str += '\n     ' + 'Directions' + '     \n'
        recipe_str += '    -' + '----------' + '-    \n'
        recipe_str += self.directions

        # print(self.ingredients)
        # print('\n')
        # print(self.directions)
        return recipe_str
