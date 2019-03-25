from selenium.webdriver.common.by import By
from driver.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.base import Base
from pageobject.decorators import element, elements
from values.urls import vice

import allure
import os


class vicePage(Base):

    _video_channel_label = (By.XPATH, "//div[text()='Vice Channels']")
    _FREE_label_link = (By.XPATH, "//img[@alt='FREE']")
    _title_text = (By.XPATH,
                   "//h2[@class='grid__wrapper__card__text__title hed-m m-b-2-xs']")
    _dek_text = (By.XPATH,
                 "//div[@class='grid__wrapper__card__text__summary bod-s m-b-2-xs']")

    VICE_URL = os.environ.get('VICE')

    @property
    @element
    def video_channel_label(self):
        return self._video_channel_label

    @property
    @element
    def free_label_link(self):
        return self._FREE_label_link

    @property
    @elements
    def title_text(self):
        return self._title_text

    @property
    @elements
    def dek_text(self):
        return self._dek_text

    def __init__(self, driver):
        Base.__init__(self, driver)

    def navigate_to_vice(self):
        with allure.step("Navigate to vice main page"):
            try:
                Driver.redirect_to(self.VICE_URL)
            except:
                Driver.redirect_to(vice)

    def click_on_channel_videos_toggle(self):
        with allure.step("Click video channel label menu"):
            self.video_channel_label.click()

    def click_on_FREE_label_link(self):
        with allure.step("Click FREE channel option"):
            self.free_label_link.click()

    def validate_dek_aligment(self):
        for title, dek in zip(self.title_text, self.dek_text):
            Driver.driver.execute_script('arguments[0].scrollIntoView()',
                                         title)
            if (title.location['x'] != dek.location['x']):
                print('title text: ', title.text, 'dek text: ', dek.text)
                return False
        return True
