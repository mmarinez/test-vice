from selenium.webdriver.common.by import By
from pageobject.Page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class vicepage(Page):

    def __init__(self):
        super(vicepage, self).__init__()

    def navigate_to_vice(self):
        self.driver.get("https://www.vice.com/en_us")

    def click_on_channel_videos_toggle(self):
        self._vice_channel_ = WebDriverWait(self.driver, 15).until(
                                    EC.visibility_of_element_located((
                                    By.XPATH, "//div[text()='Vice Channels']")))

        self._vice_channel_.click()

    def click_on_FREE_label_link(self):
        self._FREE_label_link = WebDriverWait(self.driver, 15).until(
                                EC.visibility_of_element_located((
                                By.XPATH, "//img[@alt='FREE']")))

        self._FREE_label_link.click()
