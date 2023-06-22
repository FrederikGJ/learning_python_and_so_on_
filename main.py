from tv2_business_scraper import TV2Scraper
from Børsen_scraper import BorsenScraper
from Finans_scraper import FinansScraper
from DR_scraper import DRSCraper

class Main:
    def __init__(self):
        scraper1 = TV2Scraper()
        scraper2 = BorsenScraper()
        scraper3 = FinansScraper()
        scraper4 = DRSCraper()

        print("Antallet af positive ord hos tv2 er: ", scraper1.count_positive_words())
        print("Antallet af negative ord hos tv2 er: ", scraper1.count_negative_words())

        print("Antallet af positive ord hos Borsen er: ", scraper2.count_positive_words())
        print("Antallet af negative ord hos Borsen er: ", scraper2.count_negative_words())
        
        print("Antallet af positive ord hos Finans er: ", scraper3.count_positive_words())
        print("Antallet af negative ord hos Finans er: ", scraper3.count_negative_words())
        
        print("Antallet af positive ord hos Danmarks Radio er: ", scraper4.count_positive_words())
        print("Antallet af negative ord hos Danmarks Radio er: ", scraper4.count_negative_words())
        
        print("")
        print("Overskrifter fra TV2 :\n")
        scraper1.print_labels()
        print("Overskrifter fra TV2 :\n")
        scraper2.print_texts()
        print("Overskrifter fra TV2 :\n")
        scraper3.print_texts()
        print("Overskrifter fra TV2 :\n")
        scraper4.print_texts()

if __name__ == '__main__':
    Main()
