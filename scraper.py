from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.dr.dk/nyheder/penge")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
links = soup.findAll(href=lambda href: href and href.startswith('/nyheder/'))

for link in links:
    print(link.text)


