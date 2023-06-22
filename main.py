from tv2_business_scraper import TV2Scraper

class Main:
    def __init__(self):
        scraper = TV2Scraper()
        print("Antallet af positive ord er: ", scraper.count_positive_words())
        print("Antallet af negative ord er: ", scraper.count_negative_words())
        scraper.print_labels()

if __name__ == '__main__':
    Main()
