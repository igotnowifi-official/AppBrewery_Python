import requests
from bs4 import BeautifulSoup

URL = "https://www.audible.com/adblbestsellers?ref=a_hp_t1_navTop_pl0cg1c0r0&pf_rd_p=c592ea51-fd36-4dc9-b9af-f665ee88670b&pf_rd_r=1ZN2D6MVTW997E5VMKZ9"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_books = soup.find_all(name="h3", class_="bc-heading")

book_titles = [book.getText() for book in all_books]
books = book_titles[3::]

with open("audiblebooks.txt", mode="w") as file:
    file.write("Top 20 Best Selling Audible Books:")
    for book in books:
        file.write(f"\n{book}")