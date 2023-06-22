from bs4 import BeautifulSoup 
import requests
from base_scraper import BaseScraper

class BorsenScraper(BaseScraper):
    def __init__(self):
        super().__init__()  # This calls the parent's (BaseScraper's) constructor
        self.page_to_scrape = requests.get("https://borsen.dk/nyheder/profinans")
        self.soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")
        self.links = self.soup.findAll(href=lambda href: href and href.startswith('/nyheder/'))
        self.printed_texts = []  
        for link in self.links:
            text = link.text.strip()  
            if text not in self.printed_texts:
                self.printed_texts.append(text)

    def count_positive_words(self):
        count = 0
        for text in self.printed_texts:
            for word in self.positive_words:
                count += text.lower().count(word)
        return count

    def count_negative_words(self):
        count = 0
        for text in self.printed_texts:
            for word in self.negative_words:
                count += text.lower().count(word)
        return count

    def print_texts(self):
        for text in self.printed_texts:
            print(text)
