from selenium.webdriver.common.by import By
from pageobject.Page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class freevicepage(Page):

    def __init__(self):
        super(freevicepage, self).__init__()

    def click_hamburger_menu(self):
        self._hamburger_menu_ = WebDriverWait(self.driver, 15).until(
                                    EC.visibility_of_element_located((
                                    By.XPATH, "//*[name()='svg' and @class='site-header__nav-trigger']//*")))

        ActionChains(self.driver).move_to_element(self._hamburger_menu_).click(self._hamburger_menu_).perform()

    def is_videos_label_displayed(self):

        _element_list_ = WebDriverWait(self.driver, 15).until(
                            EC.presence_of_all_elements_located((
                            By.XPATH, "//*")))

        time.sleep(5)

        for element in _element_list_:
            if(element.get_attribute("class") in "duration"):
                return False
            return True