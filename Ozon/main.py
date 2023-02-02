import time

from common.base import Base
from common.locators import OzonLocators
from common.models import Product
from common.settings import Keys

from Ozon.settings import Urls


class Ozon(Base):
    def search(self, query: str) -> list[Product]:
        self.send_values(locator=OzonLocators.SEARCH_INPUT, value=query)
        product_cards = self.browser.find_elements(*OzonLocators.PRODUCT_CARD_ITEM)
        product_list = []
        for product_card in product_cards:
            product = self.parse_product_info(
                product_card=product_card.text, query=query
            )
            product_list.append(product)
        print(product_list)
        return product_list

    def get_discount(self, item: str) -> int:
        return int(item[1:-1])

    def get_price(self, item: str, product_price: float = None) -> float:
        price = float(item.replace(Keys.THIN_SPICE, "").replace(Keys.PRICE_KEY, ""))
        return min(price, product_price) if product_price else price

    def get_delivery_date(self, item):
        delivery_word = item.index(Keys.DELIVERY_KEY) - 1
        return item[:delivery_word]

    def get_producer(self, item):
        producer_word = item.index(Keys.PRODUCER_KEY) + len(Keys.PRODUCER_KEY) + 1
        return item[producer_word:]

    def parse_product_info(self, product_card: str, query: str) -> Product:
        product_info = product_card.split("\n")
        product = Product()
        for item in product_info:
            if item.count(Keys.DISCOUNT_KEY) == 1:
                product.discount = self.get_discount(item=item)
            if item.count(Keys.PRICE_KEY) == 1:
                product.price = self.get_price(item=item, product_price=product.price)
            if query.lower() in item.lower():
                product.name = item
            if Keys.DELIVERY_KEY in item or Keys.PRODUCER_KEY in item:
                product.delivery_date = self.get_delivery_date(item=item)
                product.producer = self.get_producer(item=item)
        return product


def main():
    ozon = Ozon(url=Urls.BASE_URL)
    query = input("Input query: ")
    ozon.search(query=query)
