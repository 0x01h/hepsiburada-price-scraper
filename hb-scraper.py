#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

productPage = input('Enter the product page URL to get price: ')

try:
    page = requests.get(productPage)
    soup = BeautifulSoup(page.content, 'html.parser')
    parent = soup.find(id="offering-price")
    beforePoint = parent.select("span")[0]
    afterPoint = parent.select("span")[1]
    print(beforePoint.get_text() + '.' + afterPoint.get_text() + ' TL')
except:
    print("Price couldn't be scraped!")
