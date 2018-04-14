# Hepsiburada Price Scraper
Small Python 3 script to scrape product prices from [hepsiburada.com](https://www.hepsiburada.com)

## Prerequisite
**bs4 (Beautiful Soup 4)** <br />
`pip3 install bs4`

## Example Usage

`> ./hb-scraper.py`<br />
`> Enter the product page URL to get price: https://www.hepsiburada.com/asus-x542ur-gq030-intel-core-i7-7500u-8gb-1tb-gt930mx-freedos-15-6-tasinabilir-bilgisayar-p-HBV000008OBG5`<br />
`> 3.125.00 TL`<br />


`> ./hb-scraper.py`<br />
`> Enter the product page URL to get price: https://www.hepsiburada.com/dell-gaming-7577-intel-core-i7-7700hq-8gb-1tb-128gb-ssd-gtx1050ti-freedos-15-6-fhd-ips-tasinabilir-bilgisayar-fb70d128f81c-p-HBV000009FDXO`<br />
`> 4.499.00 TL`

*If you want to run on Python 2.7, change "input" to "raw_input" and run "pip install bs4".*
