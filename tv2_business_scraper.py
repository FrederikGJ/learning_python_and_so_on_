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

page_to_scrape = requests.get("https://nyheder.tv2.dk/business")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
elements = soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag.get('href').startswith('https://nyheder.tv2.dk/business/'))

aria_labels = set()  

for element in elements:
    aria_label = element.get('aria-label')
    if aria_label and aria_label not in aria_labels:
        aria_labels.add(aria_label)

positive_words = ["godt", "opsving", "stærkt", "gode", "sejr", "vækst"]
positive_ord = count_positive_words(aria_labels, positive_words)
print("Antallet af positive ord er: ", positive_ord)

negative_words = ["inflation", "konflikt", "inflation", "prisstigninger","nedtur", "strejke", "bedrageri"]
negative_ord = count_negative_words(aria_labels, negative_words)
print("Antallet af negative ord er:", negative_ord)

for label in aria_labels:
    print(label)
