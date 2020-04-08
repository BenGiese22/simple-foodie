from recipe import Recipe
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me
from datetime import datetime
import requests, json, os, sys

APP_URL = 'https://simple-foodie-api.herokuapp.com/recipes-api/'

def all_recipes_veg():
    all_recipes_base_url = 'https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page='
    all_recipes_total_pages = 10
    # all_recipes_total_pages = 412

    links = [] 
    recipes = []

    for x in range (0, all_recipes_total_pages+1):
        page = requests.get(all_recipes_base_url+str(x))
        check_status_code(page, all_recipes_base_url+str(x))
        soup = BeautifulSoup(page.content, 'html.parser')
        recipe_cards = soup.find_all('article', class_='fixed-recipe-card')
        for article in recipe_cards:
            links.append(article.div.a.get('href'))

    links = ['https://www.allrecipes.com/recipe/220661/quinoa-black-bean-burgers/']

    for link in links:
        rec = scrape_me(link)
        print('scraping: ' + link)
        recipes.append(Recipe(link, rec.title(), rec.ingredients(), rec.instructions(), 'allrecipes.com'))

    return recipes

def jamie_oliver_veg():
    jamie_oliver_base_url = 'https://www.jamieoliver.com'
    html_string = None
    with open('raw_html/jamie_oliver_veg.html', 'r') as f:
        html_string = f.read()

    links = []
    recipes = []

    if html_string is not None:
        soup = BeautifulSoup(html_string, 'html.parser')
        recipe_cards = soup.find_all('div', class_='recipe-block')
        for recipe in recipe_cards:
            links.append(jamie_oliver_base_url + recipe.a.get('href'))
    
    for link in links:
        rec = scrape_me(link)
        recipes.append(Recipe(link, rec.title(), rec.ingredients(), rec.instructions(), 'jamieoliver.com'))

    return recipes

def check_status_code(page, link):
    if page.status_code is not 200:
        print('error, on this link: ' + link + ' with this status code: ' + str(page.status_code))

def val_bool_loop(iterable):
    """Pass through all values from the given iterable, augmented by the
    information if there are more values to come after the current one
    (True), or if it is the last value (False).
    """
    # Get an iterator and pull the first value.
    it = iter(iterable)
    last = next(it)
    # Run the iterator to exhaustion (starting from the second value).
    for val in it:
        # Report the *previous* value (more to come).
        yield last, True
        last = val
    # Report the last value.
    yield last, False

def print_write_recipes(recipes):
    f = open('writeout.txt', 'w')
    for recipe in recipes:
        print('---------------------')
        print(recipe.to_string())
        print('\n\n')
        f.write('-------------------\n')
        f.write(recipe.to_string())
        f.write('\n\n')
    f.close()

def write_json_recipes(recipes):
    if os.path.exists('post_json.txt'):
        os.remove('post_json.txt') # delete file
        print('Deleted existing post_json.txt file...')
    f = open('post_json.txt', 'w')
    f.write('[\n')

    for recipe, more_items in val_bool_loop(recipes):
        if more_items:
            write_json_object(f, recipe)
            f.write(',\n')
        else:
            write_json_object(f, recipe)
            f.write('\n')
    f.write(']')
    f.close()

def write_json_object(f, recipe):
    f.write('   {\n')
    f.write('    \"link\": \"'+str(recipe.get_link())+'\",\n')
    f.write('    \"title\": \"'+str(recipe.get_title())+'\",\n')
    f.write('    \"ingredients\": \"'+str(recipe.get_ingredients())+'\",\n')
    f.write('    \"directions\": \"'+str(recipe.get_directions())+'\",\n')
    f.write('    \"source\": \"'+str(recipe.get_source())+'\",\n')
    f.write('    \"created_date\": \"'+str(datetime.now().isoformat()+'-06:00')+'\"\n') 
    f.write('    }')  

def post_recipe(recipe):
    hdrs = {'Content-Type': 'application/json'}
    payload_str = "[\r\n   {\r\n    \"link\": \"{link}\",\r\n    \"title\": \"{title}\",\r\n    \"ingredients\": \"{ingredients}\",\r\n    \"directions\": \"{directions}\",\r\n    \"source\": \"{source}\",\r\n    \"created_date\": \"{created_date}\"\r\n    }\r\n]"
    created_date = str(datetime.now().isoformat()+'-06:00')
    payload_str = payload_str.replace('{link}', recipe.get_link()).replace('{title}', recipe.get_title()).replace('{ingredients}', str(recipe.get_ingredients()).replace('\"', '\'')).replace('{directions}', recipe.get_directions()).replace('{source}', recipe.get_source()).replace('{created_date}', created_date)
    response = requests.post(APP_URL, data=payload_str, headers=hdrs)
    print(response.text.encode('utf8'))

def main():
    recipes = []
    recipes += all_recipes_veg()
    # recipes += jamie_oliver_veg()
    # print_write_recipes(recipes)
    # write_json_recipes(recipes)
    for recipe in recipes:
        post_recipe(recipe)

def get_test_recipe():
    link = 'https://www.allrecipes.com/recipe/16259/ds-famous-salsa/'
    title = 'D\'s Famous Salsa'
    ingredients =  ['2 (14.5 ounce) cans stewed tomatoes', '1/2 onion, finely diced', '1 teaspoon minced garlic', '1/2 lime, juiced', '1 teaspoon salt', '1/4 cup canned sliced green chiles, or to taste', '3 tablespoons chopped fresh cilantro']
    directions = 'Place the tomatoes, onion, garlic, lime juice, salt, green chiles, and cilantro in a blender or food processor. Blend on low to desired consistency.'
    source = 'allrecipes.com'
    return Recipe(link, title, ingredients, directions, source)

if __name__ == "__main__":
    main()


"""
Test against:
https://www.allrecipes.com/recipe/13938/connies-zucchini-crab-cakes/
0xae
"""