from selenium.webdriver.common.by import By
from pageobject.driver import Driver
from pageobject.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pageobject.decorators import element, elements


class freevicepage(Base):

    _element_list = (By.XPATH, "//*")

    @property
    @elements
    def article_list(self):
        return self._element_list

    def __init__(self, driver):
        Base.__init__(self, driver)

    def is_videos_label_displayed(self):
        for element in self.article_list:
            Driver.driver.execute_script(
                'arguments[0].scrollIntoView()', element)

            if(element.get_attribute("class") in "duration"):
                return False
            return True