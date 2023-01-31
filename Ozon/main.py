import time

from common.base import Base
from common.locators import OzonLocators

from Ozon.settings import Urls


class Ozon(Base):
    def search(self, query: str):
        self.send_values(locator=OzonLocators.SEARCH_INPUT, value=query)
        product_cards = self.browser.find_elements(*OzonLocators.PRODUCT_CARD_ITEM)
        print(len(product_cards))


def main():
    ozon = Ozon(url=Urls.BASE_URL)
    query = input("Input query: ")
    ozon.search(query=query)
    time.sleep(300)
