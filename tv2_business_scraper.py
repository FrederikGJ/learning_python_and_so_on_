from bs4 import BeautifulSoup
import requests
from base_scraper import BaseScraper

class TV2Scraper(BaseScraper):   
    def __init__(self):
        super().__init__()  # This calls the parent's (BaseScraper's) constructor
        self.page_to_scrape = requests.get("https://nyheder.tv2.dk/business")
        self.soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")
        self.elements = self.soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag.get('href').startswith('https://nyheder.tv2.dk/business/'))
        self.printed_texts = []  
        for element in self.elements:
            aria_label = element.get('aria-label')
            if aria_label and aria_label not in self.printed_texts:
                self.printed_texts.append(aria_label)

    def count_positive_words(self):
        count = 0
        for label in self.printed_texts:  
            for word in self.positive_words:
                count += label.lower().count(word)
        return count

    def count_negative_words(self):
        count = 0
        for label in self.printed_texts:  
            for word in self.negative_words:
                count += label.lower().count(word)
        return count

    def print_texts(self):  
        for label in self.printed_texts:  
            print(label)
