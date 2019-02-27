import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type (e.g. chrome)")
    parser.addoption("--headless", action="store", default="headless", help="Is headless driver?")


@pytest.yield_fixture(scope="class", autouse=True)
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver

    yield driver
    driver.quit()
