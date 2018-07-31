#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def main():
    productPage = input('Enter the product page URL to get price: ')

    try:
        page = requests.get(productPage)
        soup = BeautifulSoup(page.content, 'html.parser')
        parent = soup.find(id='offering-price')
        beforePoint = parent.select('span')[0]
        afterPoint = parent.select('span')[1]
        print (beforePoint.get_text() + '.' + afterPoint.get_text() + ' TL')
    except:
        print ("Price couldn't be scraped!")


if __name__ == '__main__':
    main()
