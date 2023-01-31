import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from common.settings import max_wait_time, timeout
from common.utils import get_browser


class Base:
    def __init__(self, url: str) -> None:
        self.browser = get_browser()
        self.url = url
        self.browser.get(self.url)

    def open(self, url: str) -> None:
        self.browser.get(url)

    def is_element_present(self, locator: tuple) -> bool:
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def is_element_not_appear(self, locator: tuple) -> bool:
        try:
            WebDriverWait(driver=self.browser, timeout=max_wait_time).until(
                method=expected_conditions.presence_of_element_located(locator)
            )
        except TimeoutException:
            return True
        return False

    def is_element_clickable(self, locator: tuple) -> bool:
        try:
            WebDriverWait(driver=self.browser, timeout=timeout()).until(
                method=expected_conditions.element_to_be_clickable(locator)
            )
        except TimeoutException:
            return False
        return True

    def find_and_click_element(self, locator: tuple) -> WebElement | None:
        countdown = max_wait_time
        while not (
            self.is_element_present(locator=locator)
            and self.is_element_clickable(locator=locator)
            and countdown > 0
        ):
            self.browser.implicitly_wait(time_to_wait=timeout())
            countdown -= timeout()
        if self.is_element_not_appear(locator=locator):
            return None
        element = self.browser.find_element(*locator)
        element.click()
        self.browser.implicitly_wait(time_to_wait=timeout())
        return element

    def send_values(self, locator: tuple, value: str):
        element = self.find_and_click_element(locator=locator)
        element.clear()
        element.send_keys(value)
        self.browser.implicitly_wait(time_to_wait=timeout())
        element.send_keys(Keys.ENTER)
        time.sleep(timeout())
