from selenium.webdriver.common.by import By
from pageobject.Page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class vicebroadlypage(Page):

    def __init__(self):
        super(vicebroadlypage, self).__init__()

    def navigate_to_broadly_topic_page(self):
        self.driver.get("https://broadly.vice.com/en_us/topic/25-strong-created-with-reebok")

    def navigate_to_broadly_power_topic_page(self):
        self.driver.get("https://broadly.vice.com/en_us/topic/power")

    def navigate_to_broadly_life_topic_page(self):
        self.driver.get("https://broadly.vice.com/en_us/topic/life")

    def navigate_to_broadly_culture_topic_page(self):
        self.driver.get("https://broadly.vice.com/en_us/topic/culture")

    def navigate_to_broadly_lore_topic_page(self):
        self.driver.get("https://broadly.vice.com/en_us/topic/lore")

    def navigate_to_broadly_horoscope_topic_page(self):
        self.driver.get("https://broadly.vice.com/en_us/topic/horoscopes")

    def validate_grid_content(self):
        _grid_elements_ = WebDriverWait(self.driver, 15).until(
                                    EC.visibility_of_all_elements_located((
                                    By.XPATH, "//h2[@class='grid__card__themed__title hed-m m-b-2-xs']")))

        for content in _grid_elements_:
            self.driver.execute_script('arguments[0].scrollIntoView', content)
            if(len(content.text) == 0):
                print("Failed list element position: ", _grid_elements_.index(content))
                return False
            return True