import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def pytest_addoption(parser):
    parser.addoption('--test_type', action='store', default="local",
                     help='Choose from local or remote')
    parser.addoption('--language', action='store', default="ru",
                     help='Choose from langs:(en/ru/es/')
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--executor', action='store', default="192.168.0.121")
    parser.addoption('--bro_version', action='store', default="126")


@pytest.fixture(scope="function")
@allure.title("Prepare for the test")
def browser(request):
    test_type = request.config.getoption("--test_type")
    browser_name = request.config.getoption("--browser_name")
    user_language = request.config.getoption("--language")
    executor = request.config.getoption("--executor")
    bro_version = request.config.getoption("--bro_version")

    capabilities = {"browserName": browser_name,
                    "browserVersion": bro_version,
                    "selenoid:options": {
                        "enableVideo": False
                    }
                    }

    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)

    if test_type == "remote":
        driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                  desired_capabilities=capabilities)
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

        request.addfinalizer(driver.quit)  # Закрытие браузера после теста
        return driver


    elif test_type == "local":
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        request.addfinalizer(browser.quit)  # Закрытие браузера после теста
        print('stop chrome browser for test')
        return browser





def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        if "no such element" in str(call.excinfo.value):
            item.user_properties.append(("rerun", True))
            print(item.user_properties)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item, nextitem):
    print('teardown start')
    if any(prop[0] == "rerun" for prop in item.user_properties):
        # Удаляем свойство rerun после проверки
        item.user_properties = [prop for prop in item.user_properties if prop[0] != "rerun"]



# @pytest.mark.parametrize("url", ["https://example.com"])  # Параметризация для примера
# def test_find_element(browser, url):
#     browser.get(url)
#     # Попытка найти элемент, который не существует
#     browser.find_element("id", "non_existent_element")  # Это вызовет NoSuchElementException