from bs4 import BeautifulSoup
import requests

#sentiment analyser for the news on DR 

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


page_to_scrape = requests.get("https://borsen.dk/nyheder/profinans")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
links = soup.findAll(href=lambda href: href and href.startswith('/nyheder/'))

printed_texts = set()  

for link in links:
    text = link.text
    if text not in printed_texts:
        printed_texts.add(text)

positive_words = ["godt", "opsving", "stærkt", "gode", "sejr", "vækst"]
positive_ord = count_positive_words(printed_texts, positive_words)
print("Antallet af positive ord er: ", positive_ord)

negative_words = ["inflation", "konflikt", "inflation", "prisstigninger","nedtur", "strejke"]
negative_ord = count_negative_words(printed_texts, negative_words)
print("Antallet af negative ord er:", negative_ord)

for text in printed_texts:
    print(text)