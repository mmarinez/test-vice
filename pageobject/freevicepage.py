from selenium.webdriver.common.by import By
from pageobject.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class freevicepage():

    def __init__(self):
        super(freevicepage, self).__init__()

    def is_videos_label_displayed(self):
        _element_list_ = WebDriverWait(Driver.driver, 15).until(
                            EC.presence_of_all_elements_located((
                            By.XPATH, "//*")))

        for element in _element_list_:
            Driver.driver.execute_script('arguments[0].scrollIntoView()', element)
            if(element.get_attribute("class") in "duration"):
                return False
            return True