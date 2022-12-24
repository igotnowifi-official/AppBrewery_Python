# Holiday Recipe Listing [https://www.allrecipes.com/recipes/187/holidays-and-events/christmas/] Project
# Build a random 5-course menu (Christmas: Appetizer, Main, two sides, and a dessert) 
import requests
import random
from bs4 import BeautifulSoup

random = random.randrange(0, 30)

#Getting the appetizer
URL = "https://www.allrecipes.com/recipes/932/holidays-and-events/christmas/appetizers/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_recipes = soup.find_all(name="span", class_="card__title-text")
recipe_titles = [recipe.getText() for recipe in all_recipes]
appetizer = recipe_titles[random]

#Getting the main course
URL = "https://www.allrecipes.com/recipes/939/holidays-and-events/christmas/main-dishes/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_recipes = soup.find_all(name="span", class_="card__title-text")
recipe_titles = [recipe.getText() for recipe in all_recipes]
main = recipe_titles[random]

#Getting first side dish
URL = "https://www.allrecipes.com/recipes/940/holidays-and-events/christmas/side-dishes/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_recipes = soup.find_all(name="span", class_="card__title-text")
recipe_titles = [recipe.getText() for recipe in all_recipes]
sidedish1 = recipe_titles[random]

#Getting second side dish
URL = "https://www.allrecipes.com/recipes/940/holidays-and-events/christmas/side-dishes/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_recipes = soup.find_all(name="span", class_="card__title-text")
recipe_titles = [recipe.getText() for recipe in all_recipes]
sidedish2 = recipe_titles[1]
if sidedish2 == sidedish1:
  sidedish2 = recipe_titles[5]

#Getting dessert
URL = "https://www.allrecipes.com/recipes/17180/holidays-and-events/christmas/desserts/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_recipes = soup.find_all(name="span", class_="card__title-text")
recipe_titles = [recipe.getText() for recipe in all_recipes]
dessert = recipe_titles[random]

#Printing the menu
with open("xmasmenu.txt", mode="w") as file:  
    file.write(f"This xmas party menu: \n\n\n Appetizer: {appetizer} \n\n Main Course: {main} \n {sidedish1}\n {sidedish2} \n\n Dessert: {dessert} \n\n\n Happy Holidays!")
