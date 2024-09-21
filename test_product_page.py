from .pages.product_page import ProductPage
import pytest
import allure

@allure.title("Add product to basket test")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser,link)
    with allure.step("Open Main Page"):
        page.open()
    with allure.step("Add product to basket"):
        page.add_product_to_bucket()
    with allure.step("Solve quiz"):
        page.solve_quiz_and_get_code()
    with allure.step("Book in benefit"):
        page.book_in_benefit(browser)

@allure.title("Guest should see bucket link")
@allure.severity(allure.severity_level.NORMAL)
def test_guest_should_see_login_link(browser):
    page = ProductPage(browser,  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.")
    with allure.step("Open Main Page"):
        page.open()
    with allure.step("Guest see bucket link"):
        page.should_be_bucket_link()

@allure.title("Guest can't see success message after adding product to basket")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
    with allure.step("Open Main Page"):
        page.open()
    with allure.step("Add product to bucket"):
        page.add_product_to_bucket()
    with allure.step("Solve quiz"):
        page.solve_quiz_and_get_code()
    with allure.step("Book was added tab"):
        page.book_was_added_tab()

@allure.title("guest cant see success message")
@allure.severity(allure.severity_level.NORMAL)
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
    with allure.step("Open Main Page"):
        page.open()
    with allure.step("Book was added tab"):
        page.book_was_added_tab()

@allure.title("Message disappeared after adding product to basket")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
    with allure.step("Open Main Page"):
        page.open()
    with allure.step("Add product to bucket"):
        page.add_product_to_bucket()
    with allure.step("Solve quiz"):
        page.solve_quiz_and_get_code()
    with allure.step('Bool tab disappeared'):
        page.book_tab_disappeared()