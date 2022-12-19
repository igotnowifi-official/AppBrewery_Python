from selenium import webdriver
import os

chrome_driver_path = os.environ["CHROME_DRIVER_PATH"]
driver = webdriver.Chrome(executalb_path=chrome_driver_path)

driver.get("https://www.python.org/")
#price = driver.find_element_by_id("priceblock_ourprice")
#print(price.text)

#search_bar = driver.find_element_by_name("q")
#print(search_bar.get_attribute("placeholder"))

#logo = driver.find_element_by_class_name("python-logo")

#documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
#print(documentation_link.text)

#bug_link = driver.find_element_by_xpath('insert xpath from file inspect xpath')
#print(bug_link.text)

############## Challenge 1: ####################
# Extract the upcoming event data from the python.org website. Use Selenium to scrape all upcoming event dates and event names
# (in instructor case, there are 5) and store them in a nested Python dictionary.
# Print the dictionary to the console.
# The event data from python.org should be stored under the keys "time" and "name".

event_times = driver.find_element_by_css_selector(".event-widget time")
#for time in event_times:
    #print(time.text)
event_names = driver.find_element_by_css_selector(".event-widget li a")
#for name in event_names:
    #print(name.text)
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)


#driver.close()
driver.quit()