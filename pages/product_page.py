from Tools.scripts.make_ctype import values
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BucketPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


from ..conftest import browser


class ProductPage(BasePage):
    def add_product_to_bucket(self):
        busket_link = self.browser.find_element(*BucketPageLocators.BACKET_LINK)
        busket_link.click()

    def should_be_bucket_link(self):
        assert self.is_element_present(*BucketPageLocators.BACKET_LINK), "Bucket link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def book_in_benefit(self, browser):
        assert browser.find_element(*BucketPageLocators.BOOK_PRICE).text[:-1]>= browser.find_element(*BucketPageLocators.BENEFIT_PRICE).text[:-1], "Wrong benefit price"
        assert self.is_element_present(*BucketPageLocators.BACKET_LINK), "Bucket benefit is not presented"
        assert browser.find_element(*BucketPageLocators.BOOK_NAME_SHOP).text == browser.find_element(*BucketPageLocators.BOOK_NAME_BENEFIT).text, "Wrong book in bucket"

    def book_was_added_tab(self):
        assert self.is_not_element_present(*BucketPageLocators.BOOK_ADDED), "Guest doesn't see add's tab"

    def book_tab_disappeared(self):
        assert self.is_disappeared(*BucketPageLocators.BOOK_ADDED), "Add's tab doesn't disapperead"