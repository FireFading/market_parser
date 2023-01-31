from common.base import Base
from common.env import phone
from common.locators import GoldAppleLocators

from GoldApple.settings import Urls


class GoldApple(Base):
    def login(self) -> None:
        self.find_and_click_element(locator=GoldAppleLocators.LOGIN_BUTTON)
        self.input_values(locator=GoldAppleLocators.PHONE_INPUT, value=phone)
        code = input("Input confirmation code: ")
        self.input_values(locator=GoldAppleLocators.CODE_INPUT, value=code)

    def city_confirm(self) -> None:
        self.find_and_click_element(locator=GoldAppleLocators.CITY_CONFIRM)


def main():
    gold_apple = GoldApple(url=Urls.BASE_URL)
    gold_apple.city_confirm()
    gold_apple.login()
