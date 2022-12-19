################# Challenge 2: ################
# Create a blank file called interaction.py. 
# Use Selenium to print the total number of articles from the Wikipedia homepage to the PyCharm console.

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import os

chrome_driver_path = os.environ["CHROME_DRIVER_PATH"]
driver = webdriver.Chrome(executalb_path=chrome_driver_path)

#driver.get("https://en.wikipedia.org/wiki/Main_Page")
#article_count = driver.find_element_by_css_selector("#articlecount a")
#print(article_count)
# commented out for challenge 3

# to click on link
#article_count.click()

#all_portals = driver.find_element_by_link_text("All portals")
#all_portals.click()

# to type text into searchbar from selenium
#search = driver.find_element_by_name("search")
#search.send_keys("Python")
#search.send_keys(Keys.ENTER)

############### Challenge 3: #####################
# Practice using selenium to fill out the testing form created for the course and clicking Sign Up

driver.get("https://secure-retreat-92358.herokuapp.com/")

#putting in text to text boxes
FIRST_NAME = os.environ["f_name"]
LAST_NAME = os.environ["l_name"]
EMAIL = os.environ["email"]
first_name = driver.find_element_by_name("fName")
first_name.send_keys(FIRST_NAME)
last_name = driver.find_element_by_name("lName")
last_name.send_keys(LAST_NAME)
email = driver.find_element_by_name("email")
email.send_keys(EMAIL)

submit = driver.find_element_by_css_selector("form button")
submit.click()