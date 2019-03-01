from pageobject.driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.element import Element


def with_webdriver(original_func):
    def wrapper(self, *args, **kwargs):
        return original_func(self, Driver.driver, *args, **kwargs)

    return wrapper


def with_driver(original_func):
    def wrapper(self, *args):
        return original_func(self, Driver, *args)

    return wrapper


def element(original_func):
    def wrapper(*args, **kwargs):
        _element = WebDriverWait(Driver.driver, Driver.wait_timeout).until(
            EC.visibility_of_element_located(
                original_func(*args, **kwargs)))
        return Element(_element, original_func(*args, **kwargs))

    return wrapper


def elements(original_func):
    def wrapper(*args, **kwargs):
        _elements = WebDriverWait(Driver.driver, Driver.wait_timeout).until(
            EC.visibility_of_any_elements_located(
                original_func(*args, **kwargs)))
        _list = []
        for _element in _elements:
            _list.append(Element(_element, original_func(*args, **kwargs)))

        return _list

    return wrapper