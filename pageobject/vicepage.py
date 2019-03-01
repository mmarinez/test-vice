from selenium.webdriver.common.by import By
from pageobject.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class vicepage():

    def __init__(self):
        super(vicepage, self).__init__()

    def navigate_to_vice(self):
        Driver.driver.get("https://www.vice.com/en_us")

    def click_on_channel_videos_toggle(self):
        self._vice_channel_ = WebDriverWait(Driver.driver, 15).until(
                                    EC.visibility_of_element_located((
                                    By.XPATH, "//div[text()='Vice Channels']")))

        self._vice_channel_.click()

    def click_on_FREE_label_link(self):
        self._FREE_label_link = WebDriverWait(Driver.driver, 15).until(
                                EC.visibility_of_element_located((
                                By.XPATH, "//img[@alt='FREE']")))

        self._FREE_label_link.click()

    def validate_dek_aligment(self):
        self._title_text_ = WebDriverWait(Driver.driver, 15).until(
                                EC.visibility_of_all_elements_located((
                                By.XPATH, "//h2[@class='grid__wrapper__card__text__title hed-m m-b-2-xs']")))

        self._dek_text_ = WebDriverWait(Driver.driver, 15).until(
                                EC.visibility_of_all_elements_located((
                                By.XPATH, "//div[@class='grid__wrapper__card__text__summary bod-s m-b-2-xs']")))

        print("Title position: ", self._title_text_[0].location, "\n")
        print("Dek position: ", self._dek_text_[0].location, "\n")