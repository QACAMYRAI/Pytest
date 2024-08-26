import time
import pytest
from selenium import webdriver


@pytest.mark.parametrize("link", ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"])
def test_Login(link):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(link)
        elem = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        elem.send_keys("Vladislav")

        elem = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        elem.send_keys("Bosomykin")

        elem = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        elem.send_keys("bosomykinvlad@gmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" in str(welcome_text)
    finally:
        time.sleep(3)
        browser.quit()