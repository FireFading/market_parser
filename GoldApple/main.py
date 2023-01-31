from common.base import Base
from common.env import phone
from common.locators import GoldAppleLocators

from GoldApple.settings import Urls
import time


class GoldApple(Base):
    def login(self) -> None:
        self.find_and_click_element(locator=GoldAppleLocators.LOGIN_BUTTON)
        self.send_values(locator=GoldAppleLocators.PHONE_INPUT, value=phone)
        code = input("Input confirmation code: ")
        self.send_values(locator=GoldAppleLocators.CODE_INPUT, value=code)
        while self.is_element_present(locator=GoldAppleLocators.WRONG_CODE_MESSAGE):
            code = input("Input confirmation code: ")
            self.send_values(locator=GoldAppleLocators.CODE_INPUT, value=code)

    def city_confirm(self) -> None:
        self.find_and_click_element(locator=GoldAppleLocators.CITY_CONFIRM)

    def search(self, query: str):
        self.find_and_click_element(locator=GoldAppleLocators.SEARCH_BUTTON)
        self.send_values(locator=GoldAppleLocators.SEARCH_INPUT, value=query)
        time.sleep(400)

def main():
    gold_apple = GoldApple(url=Urls.BASE_URL)
    gold_apple.city_confirm()
    gold_apple.login()
    query = input("Input query: ")
    gold_apple.search(query=query)
