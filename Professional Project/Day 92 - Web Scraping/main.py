####################### Custom Web Scraper ############################

# Objective 1 : Basic Web Scraper
# Objective 2 : Apply to Various websites suggested in txt file.

import requests
from bs4 import BeautifulSoup

URL = "insert your url"


response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_subject = soup.find_all(name="insert type", class_="insert class name")

subject_titles = [subject.getText() for subject in all_subjects]
subjects = subject_titles[::-1]

with open("subject.txt", mode="w") as file:
    for subject in subjects:
        file.write(f"{subject}\n")

