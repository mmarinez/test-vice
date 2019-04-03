from driver.driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functools import partialmethod
import os
import allure


def screenshotOnFail():
    def decorator(cls):
        def with_screen_shot(self, fn, *args, **kwargs):
            """Take a Screen-shot of the drive page, when a function fails."""
            try:
                return fn(self, *args, **kwargs)
            except Exception:
                # This will only be reached if the test fails
                filename = 'screenshot-%s.png' % fn.__name__
                console_log = Driver.driver.get_log('browser')
                Driver.driver.get_screenshot_as_file(os.path.abspath(
                    os.path.join('.', 'screenshots', filename)))

                allure.attach(Driver.driver.get_screenshot_as_png(),
                              name="Screenshot",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(console_log),
                              name="Console Log",
                              attachment_type=allure.attachment_type.TEXT)
                print('Screenshot saved as %s' % filename)
                raise

        for attr, fn in cls.__dict__.items():
            if attr[:5] == 'test_' and callable(fn):
                setattr(cls, attr, partialmethod(with_screen_shot, fn))

        return cls
    return decorator


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
