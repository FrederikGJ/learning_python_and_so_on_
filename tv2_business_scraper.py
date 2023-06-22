from bs4 import BeautifulSoup
import requests

class TV2Scraper:   
    def __init__(self):
        self.page_to_scrape = requests.get("https://nyheder.tv2.dk/business")
        self.soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")
        self.elements = self.soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag.get('href').startswith('https://nyheder.tv2.dk/business/'))
        self.aria_labels = set()  
        for element in self.elements:
            aria_label = element.get('aria-label')
            if aria_label and aria_label not in self.aria_labels:
                self.aria_labels.add(aria_label)
        self.positive_words = ["godt", "opsving", "stærkt", "gode", "sejr", "vækst"]
        self.negative_words = ["inflation", "konflikt", "inflation", "prisstigninger","nedtur", "strejke", "bedrageri"]

    def count_positive_words(self):
        count = 0
        for label in self.aria_labels:
            for word in self.positive_words:
                count += label.lower().count(word)
        return count

    def count_negative_words(self):
        count = 0
        for label in self.aria_labels:
            for word in self.negative_words:
                count += label.lower().count(word)
        return count

    def print_labels(self):
        for label in self.aria_labels:
            print(label)

