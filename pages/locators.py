from selenium.webdriver.common.by import By

class MainPageLocators():
    PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class BucketPageLocators():
    BACKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BENEFIT_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BENEFIT_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    BOOK_NAME_SHOP = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_NAME_BENEFIT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong ")
