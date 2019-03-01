from selenium.webdriver.common.by import By
from pageobject.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values.urls import themed_topics
import time


class vicebroadlypage():

    def __init__(self):
        super(vicebroadlypage, self).__init__()

    def validate_grid_content(self):

        for index, topic_url in themed_topics.items():
            Driver.driver.get(topic_url)
            _grid_elements_ = WebDriverWait(Driver.driver, 15).until(
                                    EC.visibility_of_all_elements_located((
                                    By.XPATH, "//h2[@class='grid__card__themed__title hed-m m-b-2-xs']")))

            for content in _grid_elements_:
                Driver.driver.execute_script('arguments[0].scrollIntoView()', content)
                if(len(content.text) == 0):
                    print("Failed list element position: ", _grid_elements_.index(content))
                    return False
        return True