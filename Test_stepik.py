from selenium import webdriver
import pytest
import time
import math

@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])
def test_stepik(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)

    sendans = browser.find_element_by_xpath(r"//textarea")
    sendans.send_keys(str(math.log(int(time.time()))))

    buttonsend = browser.find_element_by_xpath(r'//button[@class="submit-submission"]')
    buttonsend.click()

    welcome_text_elt = browser.find_element_by_tag_name("pre")
    welcome_text = welcome_text_elt.text
    assert "Correct" in welcome_text
