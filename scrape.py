from bs4 import BeautifulSoup
from recipe import Recipe
import requests

all_recipes_base_url = 'https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page='
# all_recipes_total_pages = 412
all_recipes_total_pages = 0

def scrape_all_recipes_vegetarian():

    links = []
    recipes = []

    for x in range (0, all_recipes_total_pages+1):
        page = requests.get(all_recipes_base_url+str(x))

        check_status_code(page)
    
        soup = BeautifulSoup(page.content, 'html.parser')

        recipe_cards = soup.find_all('article', class_='fixed-recipe-card')

        for article in recipe_cards:
            links.append(article.div.a.get('href'))


    #print(links)

    #links = links[0:1]

    # Got nothing for https://www.allrecipes.com/recipe/244973/summer-bounty-pasta/

    # Got Watch Now https://www.allrecipes.com/recipe/19368/chucks-favorite-mac-and-cheese/

    for link in links:
        # init lists
        ingredients = []
        directions = []

        # load specific recipe page
        page = requests.get(link)
        check_status_code(page)
        soup = BeautifulSoup(page.content, 'html.parser')

        # get objs of ingredients and directions
        ingredient_list = soup.find_all('ul', class_='checklist')
        direction_list = soup.find_all('span', class_='recipe-directions__list--item')

        for ingredient in ingredient_list:
            items = ingredient.find_all('span', class_='recipe-ingred_txt')
            for item in items:
                item_text = item.get_text()
                if item_text is not None and item_text != 'Add all ingredients to list' and item_text != '':
                    ingredients.append(item_text)
        
        for direction in direction_list:
            direction_text = direction.get_text().rstrip()
            if 'Watch Now' in direction_text:
                direction_text.replace('Watch Now', '').rstrip()
            directions.append(direction_text)

        while directions.count('') > 0:
            directions.remove('')


        # print('\n----------')
        # print(ingredients)
        # print('\n\n')
        # print(directions)

        recipes.append(Recipe(link, ingredients, directions))

    # print(recipes)

    for recipe in recipes:
        print('---------------------')
        print(recipe.to_string())
        print('\n\n')



def check_status_code(page):
    if page.status_code is not 200:
        print('error, on this page: ' + page + ' with this status code: ' + page.status_code)

def main():
    scrape_all_recipes_vegetarian()

if __name__ == "__main__":
    main()
