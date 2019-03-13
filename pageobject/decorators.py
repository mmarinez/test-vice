from driver.driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def element(original_func):
    def wrapper(self, *args, **kwargs):
        element_list = WebDriverWait(Driver.driver, 15).until(
            EC.visibility_of_element_located((
                original_func(self, *args, **kwargs))))
        return element_list

    return wrapper


def elements(original_func):
    def wrapper(self, *args, **kwargs):
        elements_list = WebDriverWait(Driver.driver, 15).until(
            EC.visibility_of_any_elements_located((
                original_func(self, *args, **kwargs))))

        _list_container = []
        for _element in elements_list:
            _list_container.append(_element)

        return _list_container

    return wrapper
