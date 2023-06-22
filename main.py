from tv2_business_scraper import TV2Scraper
from Børsen_scraper import BorsenScraper
from Finans_scraper import FinansScraper
from DR_scraper import DRSCraper

class Main:
    def __init__(self):
        scraper1 = TV2Scraper()
        print("Antallet af positive ord hos tv2 er: ", scraper1.count_positive_words())
        print("Antallet af negative ord hos tv2 er: ", scraper1.count_negative_words())
        scraper1.print_labels()

        scraper2 = BorsenScraper()
        print("Antallet af positive ord hos Borsen er: ", scraper2.count_positive_words())
        print("Antallet af negative ord hos Borsen er: ", scraper2.count_negative_words())
        scraper2.print_texts()

        scraper3 = FinansScraper()
        print("Antallet af positive ord er: ", scraper3.count_positive_words())
        print("Antallet af negative ord er: ", scraper3.count_negative_words())
        scraper3.print_texts()


        scraper4 = DRSCraper()
        print("Antallet af positive ord er: ", scraper4.count_positive_words())
        print("Antallet af negative ord er: ", scraper4.count_negative_words())
        scraper4.print_texts()



if __name__ == '__main__':
    Main()
