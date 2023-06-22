from bs4 import BeautifulSoup
import requests

def count_positive_words(texts, words):
    count = 0
    for text in texts:
        for word in words:
            count += text.lower().count(word)
    return count

def count_negative_words(texts, words):
    count = 0
    for text in texts:
        for word in words:
            count += text.lower().count(word)
    return count

page_to_scrape = requests.get("https://finans.dk/erhverv/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
elements = soup.find_all('span', class_='c-article-teaser-heading__text')

texts = []  

for element in elements:
    texts.append(element.text)

positive_words = ["godt", "opsving", "stærkt", "gode", "sejr", "vækst"]
positive_ord = count_positive_words(texts, positive_words)
print("Antallet af positive ord er: ", positive_ord)

negative_words = ["inflation", "konflikt", "inflation", "prisstigninger","nedtur", "strejke", "bedrageri"]
negative_ord = count_negative_words(texts, negative_words)
print("Antallet af negative ord er:", negative_ord)

for text in texts:
    print(text)