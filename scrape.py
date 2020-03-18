from recipe import Recipe
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me
import requests


def all_recipes_veg():
    all_recipes_base_url = 'https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page='
    # all_recipes_total_pages = 412
    all_recipes_total_pages = 1

    links = [] 
    recipes = []

    for x in range (0, all_recipes_total_pages+1):
        page = requests.get(all_recipes_base_url+str(x))
        check_status_code(page, all_recipes_base_url+str(x))
        soup = BeautifulSoup(page.content, 'html.parser')
        recipe_cards = soup.find_all('article', class_='fixed-recipe-card')
        for article in recipe_cards:
            links.append(article.div.a.get('href'))

    for link in links:
        rec = scrape_me(link)
        recipes.append(Recipe(link, rec.title(), rec.ingredients(), rec.instructions(), 'allrecipes.com'))

    return recipes

def check_status_code(page, link):
    if page.status_code is not 200:
        print('error, on this link: ' + link + ' with this status code: ' + str(page.status_code))

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

def main():
    recipes = []
    recipes += all_recipes_veg()

    print_write_recipes(recipes)

if __name__ == "__main__":
    main()
