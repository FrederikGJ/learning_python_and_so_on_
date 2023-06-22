from abc import ABC, abstractmethod

class BaseScraper(ABC):

    def __init__(self):
        self.positive_words = ["godt", "opsving", "stærkt", "gode", "sejr", "vækst"]
        self.negative_words = ["inflation", "konflikt", "inflation", "prisstigninger","nedtur", "strejke", "bedrageri"]

                # self.positive_words = ["godt", "opsving", "stærkt", "gode", "sejr", "vækst"]
        # self.negative_words = ["inflation", "konflikt", "inflation", "prisstigninger","nedtur", "strejke", "bedrageri"]

    @abstractmethod
    def count_positive_words(self):
        pass

    @abstractmethod
    def count_negative_words(self):
        pass

    @abstractmethod
    def print_texts(self):
        pass