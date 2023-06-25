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
        
        self.total_negative = scraper1.count_negative_words() + scraper2.count_negative_words() + scraper3.count_negative_words() + scraper4.count_negative_words()
        self.total_positive = scraper1.count_positive_words() + scraper2.count_positive_words() + scraper3.count_positive_words() + scraper4.count_positive_words()


if __name__ == '__main__':
    Main()
