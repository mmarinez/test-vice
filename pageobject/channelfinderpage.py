from pageobject.base import Base
from pageobject.decorators import element, elements
from driver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure
import os
import time


class ChannelFinder(Base):

    _input_zip_code = (By.CSS_SELECTOR, "input[type*='number']")
    _error_provider_message = (By.CSS_SELECTOR, "span[id*='provider-error']")

    @property
    @element
    def input_zip_code(self):
        return self._input_zip_code

    @property
    @element
    def error_provider_message(self):
        return self._error_provider_message

    INVALID_ZIPCODE_TEST = os.environ.get('INVALID_ZIPCODE')

    def __init__(self, driver):
        Base.__init__(self, driver)

    def input_type_invalid_zip_code(self):
        self.input_zip_code.send_keys(self.INVALID_ZIPCODE_TEST)
        time.sleep(5)

    def validate_error_provider_message(self):
        return self.error_provider_message.is_displayed()