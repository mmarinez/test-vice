from selenium.webdriver.common.by import By
from driver.driver import Driver
from pageobject.base import Base
from pageobject.decorators import elements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values.urls import themed_topics

import allure


class vicebroadlypage(Base):

    _article_grid_elements = (By.XPATH,
                              "//h2[@class='grid__card__themed__title hed-m m-b-2-xs']")

    @property
    @elements
    def article_elements(self):
        return self._article_grid_elements

    def __init__(self, driver):
        Base.__init__(self, driver)

    def validate_grid_content(self):
        with allure.step("Validate Topic themes content to be filled"):
            for index, topic_url in themed_topics.items():
                Driver.driver.get(topic_url)

                for content in self.article_elements:
                    Driver.driver.execute_script('arguments[0].scrollIntoView()',
                                                 content)
                    if(len(content.text) == 0):
                        print("Failed list element position: ",
                              _grid_elements_.index(content))
                        return False
            return True
