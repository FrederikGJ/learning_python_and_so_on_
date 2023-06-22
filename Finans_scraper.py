from bs4 import BeautifulSoup
import requests

class FinansScraper:
    def __init__(self):
        self.page_to_scrape = requests.get("https://finans.dk/erhverv/")
        self.soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")
        self.elements = self.soup.find_all('span', class_='c-article-teaser-heading__text')
        self.texts = []  
        for element in self.elements:
            self.texts.append(element.text)
        self.positive_words = ["godt", "opsving", "stærkt", "gode", "sejr", "vækst"]
        self.negative_words = ["inflation", "konflikt", "inflation", "prisstigninger","nedtur", "strejke", "bedrageri"]

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
