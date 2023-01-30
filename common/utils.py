import undetected_chromedriver as webdriver


def get_browser():
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(options=options)
