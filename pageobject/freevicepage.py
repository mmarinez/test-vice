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

    _element_list = (By.CSS_SELECTOR, "div[class*=thumbnail]")
    _section_headers = (By.CSS_SELECTOR, "h3,h2[class*='head']")
    _video_strings_validations = (
        "video", "Video", "Episode", "Clip", "duration")

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

    def catch_all_element_attributes(self, element):
        attrs = Driver.driver.execute_script(
            'var items = {}; ' +
            'for (index = 0; index < arguments[0].attributes.length; ++index)' +
            '{ items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value };' +
            'return items;', element)
        return attrs

    def is_videos_label_displayed(self):
        with allure.step("Validate that the video label is displayed"):
            for element, header in zip(self.article_list, self.section_headers):

                Driver.driver.execute_script(
                    'arguments[0].scrollIntoView()', element)

                for element_attribute in self.catch_all_element_attributes(element):
                    if not any(validator in element.get_attribute(element_attribute)
                               for validator in self._video_strings_validations):

                        if element.text != self.article_list[-1].text:
                            continue
                        return True
                    else:
                        print(element.get_attribute(element_attribute))
                        return False

    def is_video_text_assigned(self):
        with allure.step("Validate that the headers dont have video text"):
            for header in self.section_headers:

                Driver.driver.execute_script(
                    'arguments[0].scrollIntoView()', header)

                for element_attribute in self.catch_all_element_attributes(header):
                    if not any(validator in header.get_attribute(element_attribute)
                               for validator in self._video_strings_validations):

                        if header.text != self.section_headers[-1].text:
                            continue
                        return True
                    else:
                        print(header.get_attribute(element_attribute))
                        return False

    def has_video_player(self):
        with allure.step("Validate that video player free"):
            return self.is_video_text_assigned() and self.is_videos_label_displayed()
