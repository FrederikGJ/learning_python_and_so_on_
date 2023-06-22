from bs4 import BeautifulSoup
import requests
from base_scraper import BaseScraper

class FinansScraper(BaseScraper):
    def __init__(self):
        super().__init__()  # This calls the parent's (BaseScraper's) constructor
        self.page_to_scrape = requests.get("https://borsen.dk/nyheder/profinans")
        self.soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")
        self.elements = self.soup.find_all('span', class_='c-article-teaser-heading__text')
        self.texts = []  
        for element in self.elements:
            self.texts.append(element.text)

    def count_positive_words(self):
        count = 0
        for text in self.texts:
            for word in self.positive_words:
                count += text.lower().count(word)
        return count

    def count_negative_words(self):
        count = 0
        for text in self.texts:
            for word in self.negative_words:
                count += text.lower().count(word)
        return count

    def print_texts(self):
        for text in self.texts:
            print(text)
