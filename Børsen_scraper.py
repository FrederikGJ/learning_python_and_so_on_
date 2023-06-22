from bs4 import BeautifulSoup
import requests

class BorsenScraper:
    def __init__(self):
        self.page_to_scrape = requests.get("https://borsen.dk/nyheder/profinans")
        self.soup = BeautifulSoup(self.page_to_scrape.text, "html.parser")
        self.links = self.soup.findAll(href=lambda href: href and href.startswith('/nyheder/'))
        self.printed_texts = set()  
        for link in self.links:
            text = link.text
            if text not in self.printed_texts:
                self.printed_texts.add(text)
        self.positive_words = ["godt", "opsving", "stærkt", "gode", "sejr", "vækst"]
        self.negative_words = ["inflation", "konflikt", "inflation", "prisstigninger","nedtur", "strejke"]

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
