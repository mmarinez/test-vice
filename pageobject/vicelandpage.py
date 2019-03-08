from pageobject.base import Base
from pageobject.decorators import element, elements
from pageobject.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure
import os
import time


class vicelandPage(Base):

    _watch_free_link = (By.XPATH, "(//a[text()='Watch Free'])[1]")
    _play_button = (By.CSS_SELECTOR, " div.vp__controls__playback > div")
    _video_player = (By.XPATH, "//div[@class='vp__controls']")
    _iframe_player = (By.XPATH, "//iframe[@class='player-embed']")
    _volume_control = (By.XPATH, "//div[contains(@class,'vp__controls__icon vp__icon--volume')]")
    _player_wrapper = (By.XPATH, "//div[contains(@class,'vp__container vp__container--')]")

    os.environ['VICELAND'] = "https://www.viceland.com/en_us"
    VICELAND_URL = os.environ.get('VICELAND')

    @property
    @element
    def watch_free_section_link(self):
        return self._watch_free_link

    @property
    @element
    def play_button(self):
        return self._play_button

    @property
    @element
    def video_player_controls(self):
        return self._video_player

    @property
    @element
    def video_player_frame(self):
        return self._iframe_player

    @property
    @element
    def volume_control(self):
        return self._volume_control

    @property
    @element
    def player_wrapper(self):
        return self._player_wrapper

    def __ini__(self, driver):
        Base.__init__(self, driver)

    def navigate_to_viceland(self):
        Driver.driver.get(self.VICELAND_URL)

    def click_watch_free_section(self):
        with allure.step("Click watch free videos link"):
            self.watch_free_section_link.click()

    def click_play_button(self):
        with allure.step("Play video"):
            Driver.driver.switch_to.frame(self.video_player_frame)
            ActionChains(Driver.driver).move_to_element(self.player_wrapper).perform()
            Driver.driver.execute_script("arguments[0].click()",
                                                    self.play_button)

    def validate_mute_video_volume(self):
        with allure.step("Validate mute video volume"):
            self.volume_control.click()

            if "mute" not in self.volume_control.get_attribute("class"):
                print("xpath class value: ", self.volume_control.get_attribute("class"))
                return False
            print("xpath class value: ", self.volume_control.get_attribute("class"))
            return True