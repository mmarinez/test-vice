from pageobject.base import Base
from pageobject.decorators import element, elements
from driver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import os
import time
import datetime


class vicelandPage(Base):

    _watch_free_link = (By.XPATH, "(//a[text()='Watch Free'])[1]")
    _play_button = (By.CSS_SELECTOR, "div.vp__controls__playback > div")
    _video_player = (By.XPATH, "//div[@class='vp__controls']")
    _iframe_player = (By.XPATH, "//iframe[@class='player-embed']")
    _volume_control = (
        By.XPATH, "//div[contains(@class,'vp__controls__icon vp__icon--volume')]")
    _player_wrapper = (
        By.XPATH, "//div[contains(@class,'vp__container vp__container--')]")
    _free_this_week_title = (By.XPATH, "//h3[text()='Free This Week']")
    _free_this_week_episodes = (
        By.XPATH, "//div[@data-index >= 0 and not(contains(@class,'-cloned'))]")
    _free_videos_wrapper = (By.XPATH, "(//div[@class='slick-track'])[2]")
    _next_button = (
        By.XPATH, '//button[contains(@class,"slick-arrow slick-next")]')
    _time_stamp = (By.XPATH, '//div[@class="vp__timeline__timestamp"]')

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

    @property
    @element
    def free_this_week_title(self):
        return self._free_this_week_title

    @property
    @elements
    def free_episodes(self):
        return self._free_this_week_episodes

    @property
    @element
    def free_videos_wrapper(self):
        return self._free_videos_wrapper

    @property
    @element
    def click_next_button(self):
        return self._next_button

    @property
    @element
    def time_stamp(self):
        return self._time_stamp

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
            ActionChains(Driver.driver).move_to_element(
                self.player_wrapper).perform()
            Driver.driver.execute_script("arguments[0].click()",
                                         self.play_button)

    def validate_mute_video_volume(self):
        with allure.step("Validate mute video volume"):
            self.volume_control.click()

            if "mute" not in self.volume_control.get_attribute("class"):
                print("xpath class value: ",
                      self.volume_control.get_attribute("class"))
                return False
                print("xpath class value: ",
                      self.volume_control.get_attribute("class"))
            return True

    def validate_FREE_this_week_title(self):
        with allure.step("Ensure that the FREE this week title is displayed"):
            Driver.driver.execute_script(
                "arguments[0].scrollIntoView()", self.free_this_week_title)
            return self.free_this_week_title.is_displayed()

    def validate_video_player_availability(self):
        return self.play_button.is_displayed()

    def click_FREE_episode(self):
        with allure.step("Click episode in the FREE this week section"):
            for i in range(1, 5):
                try:
                    e = WebDriverWait(Driver.driver, 15).until(
                        EC.visibility_of_any_elements_located((
                            By.XPATH, "//div[@data-index >= 0 and not(contains(@class,'-cloned')) and position() >= 4]")))
                    e[i].click()
                    time.sleep(5)
                    Driver.driver.switch_to.frame(self.video_player_frame)
                    date_time_obj = datetime.datetime.strptime('00:00', '%M:%S')
                    time.sleep(10)
                    date_time_current = datetime.datetime.strptime(
                        self.time_stamp.text, '%M:%S')
                    if date_time_current.time() < date_time_obj.time():
                        print(date_time_current.time())
                        return False

                    Driver.driver.back()
                    time.sleep(5)
                except:
                    self.click_next_button.click()
                    time.sleep(5)
                    e = WebDriverWait(Driver.driver, 15).until(
                        EC.visibility_of_any_elements_located((
                            By.XPATH, "//div[@data-index >= 0 and not(contains(@class,'-cloned')) and position() >= 4]")))
                    e[i].click()
                    time.sleep(5)
                    Driver.driver.switch_to.frame(self.video_player_frame)
                    date_time_obj = datetime.datetime.strptime(
                        '00:00', '%M:%S')
                    time.sleep(10)
                    date_time_current = datetime.datetime.strptime(
                        self.time_stamp.text, '%M:%S')
                    if date_time_current.time() < date_time_obj.time():
                        print(date_time_current.time())
                        return False
                    self.validate_video_player_availability()

                    Driver.driver.back()
                    time.sleep(5)
            return True
