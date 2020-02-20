from bs4 import BeautifulSoup
import requests

all_recipes_base_url = 'https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?page='
# all_recipes_total_pages = 412
all_recipes_total_pages = 0

def scrape_all_recipes_vegetarian():

	recipes = []

	for x in range (0, all_recipes_total_pages+1):
		page = requests.get(all_recipes_base_url+str(x))

		check_status_code(page)
	
		soup = BeautifulSoup(page.content, 'html.parser')

		recipe_cards = soup.find_all('article', class_='fixed-recipe-card')

		for article in recipe_cards:
			recipes.append(article.div.a.get('href'))


	recipes = recipes[1:2]
	print(recipes)

	for recipe in recipes:
		page = requests.get(recipe)

		check_status_code(page)

		soup = BeautifulSoup(page.content, 'html.parser')

		ingredient_list = soup.find_all('ul', class_='checklist')

		for ingredient in ingredient_list:
			print(ingredient)
			items = ingredient.find_all('span', class_='recipe-ingred_txt')
			print(items)
			for item in items:
				print(item.get_text())


def check_status_code(page):
	if page.status_code is not 200:
		print('error, on this page: ' + page + ' with this status code: ' + page.status_code)

def main():
	scrape_all_recipes_vegetarian()

if __name__ == "__main__":
	main()
