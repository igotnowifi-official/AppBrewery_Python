import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os
#with tkinter
#from tkinter import *
#from tkinter import messagebox
#import pyperclip
#import json
#import datetime

SMTP_ADDRESS = os.environ["SMTP ADDRESS"]
EMAIL_ADDRESS = os.environ["EMAIL ADDRESS"]
EMAIL_PASSWORD = os.environ["EMAIL PASSWORD"]

URL = "https://www.amazon.com/Nintendo-Switch-OLED-Model-White-Joy/dp/B098RKWHHZ/ref=sr_1_2?keywords=nintendo+switch+oled&qid=1671146262&sprefix=nin%2Caps%2C159&sr=8-2&ufe=app_do%3Aamzn1.fos.c3015c4a-46bb-44b9-81a4-dc28e6d374b3"
HEADER = {
    "Accept-Language": "en-GB,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/97.0.4692.99 Safari/537.36",
}

#if using tkinter:

#def get_data():
    #with open("data.json", "r") as data_file:
        #data = json.load(data_file)
        #url = data[URL]
        #target_price = data["target price"]
        #url_entry.insert(0,url)
        #target_price_entry.insert(0,target_price)

#def save(product_name, price):
    #url = url_entry.get()
    #target_price = target_price_entry.get()
    #today = datetime.datetime.today().strftime("%Y-%m-%d")
    #new_data = {"Date": today, "url":url, "product name": product_name, "price":price, "target price": target_price}
    #is_ok = messagebox.askokcancel(title="Amazon Price Checker", message=f"You can save the following search result. \n\n\n{product_name}\n\n\n Current Price: ${price}.\n\n\n Target Price: ${target_price}\n\n\n Date: {today}\n\n\n Do you want to save it?\n(Once you save the data, \nyou can import it by clicking the logo image next time.)")
    #if is_ok:
        #try:
            #with open("data.json", "r") as data_file:
                #data = json.load(data_file)
        #except FileNotFoundError:
            #with open("data.json", "w") as data_file:
                #json.dump(new_data, data_file, indent=4)
        #else:
            #data.update(new_data)
            #with open("data.json", "w") as data_file:
                #json.dump(data, data_file, indent=4)
        #finally:
            #messagebox.showinfo(title="Price Check Result", message="Your price data has been saved in data.json")
            #url_entry.delete(0,END)
            #target_price_entry.delete(0,END)

#def search():
    #url = url_entry.get()
    #if url == "":
        #messagebox.showerror(title="Error", message= "No url has given.")
    #else:
        #response = requests.get(url,
            #headers={"Accept-Language":"ko,en-US;q=0.9,en;q=0.8,sv;q=0.7,ja;q=0.6",
            #"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
        #soup = BeautifulSoup(response.text, "html.parser")
        #price = float(soup.find(name="span", class_="a-offscreen").getText().strip("$"))
        #target_price = float(target_price_entry.get())
        #if price < target_price:
            #product_name = soup.select_one(selector="#title > #productTitle").getText()
            #messagebox.showinfo(title="Price Check Result", message= f"Low Price Alert!.\n{product_name}\n\n\nTarget Price: ${target_price}\n\n\nCurrent Price:${price}\n\n\n product page url has been copied to your clipboard.")
            #pyperclip.copy(url)
        #else:
            #product_name = soup.select_one(selector="#title > #productTitle").getText()
            #messagebox.showinfo(title="Price Check Result",
                #message=f"Wait a bit more!.\n{product_name}\n\n\nTarget Price: ${target_price}\n\n\nCurrent Price:${price}\n\n\n The price of the product is still a bit higher than your target price!")
            #save(product_name, price)
            #url_entry.delete(0, END)
            #target_price_entry.delete(0, END)

response = requests.get(URL, headers=HEADER)
content = response.text

soup = BeautifulSoup(content, "lxml")
print(soup.prettify())

product_title_raw = soup.find("span", id="productTitle").getText().split(",")
product_title = product_title_raw[0].lstrip()

price_raw = soup.find("span", class_="apexPriceToPay")
price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 320

if price_as_float <= BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )

### tkinter GUI ###

#window = Tk()
#window.title("Amazon Price Tracker")
#window.config(padx=10, pady=10)

### labels ###

#url_label = Label(text="Product Amazon Link")
#url_label.grid(row=1, column=0)
#target_price_label = Label(text="Target Price")
#target_price_label.grid(row=2, column=0)

### entries ###

#url_entry = Entry(width=39)
#url_entry.grid(row=1, column=1, columnspan=2)
#url_entry.insert(0, "https://")
#target_price_entry = Entry(width=20)
#target_price_entry.grid(row=2, column=1)

### logo image button ###

#canvas = Canvas(height=250, width=520)
#logo_img = PhotoImage(file="Amazon-Logo-PNG1.png")
#data_button = Button(image=logo_img, command=get_data)
#data_button.grid(row=0, column=0, columnspan=3)

### button ###

#check_price_button = Button(text="Check Price!", width=14, command=search)
#check_price_button.grid(row=2, column=2)

#window.mainloop()