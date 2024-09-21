from .pages.main_page import MainPage
import allure

@allure.title("Test move to login page")
@allure.severity(allure.severity_level.NORMAL)
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer")
    with allure.step("Open Main Page"):
        page.open()
    with allure.step('Go to login page'):
        page.go_to_login_page()

@allure.title("Check login page is visible")
@allure.severity(allure.severity_level.NORMAL)
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer")
    with allure.step("Open Main Page"):
        page.open()
    with allure.step('Check login page is visible'):
        page.should_be_login_link()

