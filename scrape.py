from bs4 import BeautifulSoup
import requests

#def scrape_all_recipes_vegetarian():
	

def main():
	page = requests.get('https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/')	

	if page.status_code is not 200:
		print('error, status code: ' + page.status_code)

	soup = BeautifulSoup(page.content, 'html.parser')
	
	recipe_cards = soup.find_all('article', class_='fixed-recipe-card')
	# print(type(recipe_cards[0]))

	recipes_on_page = []

	for article in recipe_cards:
		recipes_on_page.append(article.div.a.get('href'))
		# print(article.div.a.get('href'))

	print(recipes_on_page)

if __name__ == "__main__":
	main()
