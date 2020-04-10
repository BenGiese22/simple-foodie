import re

class Recipe:

    link = None
    title = None
    ingredients = None
    directions = None
    source = None

    def __init__(self, link, title, ingredients, directions, source):
        if link is not None:
            self.link = link

        if title is not None:
            if '\"' in title:
                title = title.replace('\"', '*')
            elif '‘' in title:
                    title = title.replace('‘', '\'')
            elif '’' in title:
                title = title.replace('’', '\'')
            self.title = title

        if ingredients is not None:
            self.ingredients = []
            for ing in ingredients:
                if '½' in ing:
                    ing = ing.replace('½','1/2')
                elif '⅓' in ing:
                    ing = ing.replace('⅓', '1/3')
                elif '⅔' in ing:
                    ing = ing.replace('⅔','2/3')
                elif '¼' in ing:
                    ing = ing.replace('¼', '1/4')
                elif '¾' in ing:
                    ing = ing.replace('¾','3/4')
                elif '⅕' in ing:
                    ing = ing.replace('⅕', '1/5')
                elif '⅖' in ing:
                    ing = ing.replace('⅖', '2/5')
                elif '⅗' in ing:
                    ing = ing.replace('⅗', '3/5')
                elif '⅘' in ing:
                    ing = ing.replace('⅘','4/5')
                elif '⅙' in ing:
                    ing = ing.replace('⅙', '1/6')
                elif '⅚' in ing:
                    ing = ing.replace('⅚', '5/6')
                elif '⅛' in ing:
                    ing = ing.replace('⅛', '1/8')
                elif '⅜' in ing:
                    ing = ing.replace('⅜', '3/8')
                elif '⅝' in ing:
                    ing = ing.replace('⅝', '5/8')
                elif '⅞' in ing:
                    ing = ing.replace('⅞', '7/8')
                elif ',' in ing:
                    ing = ing.replace(',', ';')
                elif '®' in ing:
                    ing = ing.replace('®', '')
                elif '‘' in ing:
                    ing = ing.replace('‘', '\'')
                elif '’' in ing:
                    ing = ing.replace('’', '\'')
                self.ingredients.append(ing)
        
        if directions is not None:
            self.directions = directions.replace('\n', '').replace('\"', '').replace('\'', '').replace('’', '\'').replace('‘', '\'').replace('Method ', '').replace(
                ' Please enable targetting cookies to show this banner if (window.innerWidth <= 10000 && window.innerWidth >= 768) { propertag.cmd.push(function() { proper_display(jamieoliver_leftrail); }); }', '')

        if source is not None:
            self.source = source

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

    def get_link(self):
        return self.link

    def get_title(self):
        return self.title

    def get_ingredients(self):
        return self.ingredients

    def get_directions(self):
        return self.directions

    def get_source(self):
        return self.source
