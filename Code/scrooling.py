import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://twitter.com/search?l=id&q=banjir%20near%3A%22DKI%20Jakarta%2C%20Indonesia%22%20within%3A15mi%20since%3A2015-01-15%20until%3A2015-01-30&src=typd&lang=id')

time.sleep(1)

no_of_pagedowns = 10000

elem = browser.find_element_by_tag_name("body")

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1