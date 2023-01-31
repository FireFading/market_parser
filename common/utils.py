import undetected_chromedriver as webdriver


def get_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    return webdriver.Chrome(options=options)
