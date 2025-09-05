import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# print("Hello world!")

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

# NOTE: For firefox in ubuntu do not use a downloaded driver. See more on the next link
# https://firefox-source-docs.mozilla.org/testing/geckodriver/Usage.html#running-firefox-in-a-container-based-package
# for others follow the next code.
# ROOT_FOLDER = Path(__file__).parent
# GECKODRIVER = ROOT_FOLDER / "drivers" / "geckodriver-v0.36.0-linux64" / "geckodriver"

GECKODRIVER = "/snap/bin/geckodriver"


def make_firefox_browser(*options: str) -> webdriver.Firefox:
    firefox_options = webdriver.FirefoxOptions()

    for option in options:
        firefox_options.add_argument(option)

    firefox_service = webdriver.FirefoxService(executable_path=GECKODRIVER)
    browser = webdriver.Firefox(
        options=firefox_options,
        service=firefox_service,
    )
    return browser


if __name__ == "__main__":
    TIME_TO_WAIT = 30

    browser = make_firefox_browser()
    browser.get("https://www.google.com/")

    # esperar para achar o textarea
    search_textarea = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.ID, "APjFqb"))
    )
    search_textarea.send_keys("Hello World!")
    search_textarea.send_keys(Keys.ENTER)

    results = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.ID, "rso"))
    )
    links = results.find_elements(By.TAG_NAME, "a")
    print(links[0].text)
    links[0].click()

    time.sleep(TIME_TO_WAIT)
    browser.quit()
