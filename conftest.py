import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

        yield driver
        print("\nquit browser..")
        driver.quit()


    elif test_type == "local":
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        yield browser
        print("\nquit browser..")
        browser.quit()



