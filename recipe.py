import re

class Recipe:

    link = None
    title = None
    ingredients = None
    directions = None

    def __init__(self, link, ingredients, directions):
        if(link is not None):
            self.link = link
            self.title = self.get_title_from_href(link)

        if(ingredients is not None):
            self.ingredients = ingredients
        
        if(directions is not None):
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
        for direction in self.directions:
            recipe_str += direction + '\n'
        return recipe_str

    def get_title_from_href(self, link):
        # print('get title from href call')
        # print('link: ' + link)
        # regex = re.compile('https:\/\/www.allrecipes.com\/recipe\/\d+\/([^/]+)')
        # print(regex.match(link))
        # match_obj = regex.match(link)
        # cap_group = match_obj.group()
        # print(cap_group)
        # title = cap_group.replace('-', ' ')
        return 'temp title'
