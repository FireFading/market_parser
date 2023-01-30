from selenium.webdriver.common.by import By


class GoldAppleLocators:
    CITY_CONFIRM = (
        By.CSS_SELECTOR,
        ".button-primary.modal-city-informer__btn.modal-city-informer__btn_primary",
    )
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button.header-tab-button.header-tab-button_customer",
    )
    PHONE_INPUT = (By.CSS_SELECTOR, ".input-field__input[name=phone_number]")
