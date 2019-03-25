from selenium.webdriver.common.by import By
from driver.driver import Driver
from pageobject.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pageobject.decorators import element, elements
import time
import os

import allure


class freevicepage(Base):

    _element_list = (By.CSS_SELECTOR, "div[class*=thumbnail] *, div[class*=lede] *")
    _section_headers = (By.CSS_SELECTOR, "h3,h2[class*='head']")
    _video_strings_validations = (
        "video", "videos", "episodes", "clip", "duration", "shows")

    VICE_FREE = os.environ.get('VICE_FREE')

    @property
    @elements
    def article_list(self):
        return self._element_list

    @property
    @elements
    def section_headers(self):
        return self._section_headers

    def __init__(self, driver):
        Base.__init__(self, driver)

    def navigate_to_vice_free(self):
        try:
            Driver.redirect_to(self.VICE_FREE)
        except:
            Driver.redirect_to("https://free.vice.com/en_us")

    def is_videos_label_displayed(self):
        with allure.step("Validate that the video label is displayed"):
            for element in self.article_list:

                Driver.driver.execute_script(
                    'arguments[0].scrollIntoView()', element)

                if any(validator in element.get_attribute("class") for validator in self._video_strings_validations):

                    print(element.get_attribute("class"))
                    return False
            return True

    def is_video_text_assigned(self):
        with allure.step("Validate that the headers dont have video text"):
            for header in self.section_headers:

                Driver.driver.execute_script(
                    'arguments[0].scrollIntoView()', header)

                if any(validator in header.text.lower() for validator in self._video_strings_validations):

                    print(header.text)
                    return False
            return True

    def has_video_player(self):
        with allure.step("Validate that video player free"):
            return self.is_video_text_assigned() and self.is_videos_label_displayed()
