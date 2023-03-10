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
    CODE_INPUT = (By.CSS_SELECTOR, ".input-field__input[name=code]")
    RESEND_CODE_BUTTON = (By.CSS_SELECTOR, ".link.vertical-content__action-link")
    WRONG_CODE_MESSAGE = (By.CSS_SELECTOR, "label._ogg-error")
    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "button.header-tab-button.header-tab-button_search",
    )
    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "textarea.search-field__textarea.digi-autocomplete.jc-ignore",
    )


class OzonLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name=text]")
    PRODUCT_CARD_ITEM = (By.CSS_SELECTOR, ".x1j.xj2")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span._32-a2")
    PRODUCT_PRICE_WITH_OZON_CARD = (By.CSS_SELECTOR, "._33-a ._33-a0")
