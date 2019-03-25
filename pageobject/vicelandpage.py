from pageobject.base import Base
from pageobject.decorators import element, elements
from driver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import allure
import os
import time


class vicelandPage(Base):

    _watch_free_link = (By.XPATH, "(//a[text()='Watch Free'])[1]")
    _play_button = (By.CSS_SELECTOR, "div.vp__controls__playback > div")
    _video_player = (By.XPATH, "//div[@class='vp__controls']")
    _iframe_player = (By.XPATH, "//iframe[@class='player-embed']")
    _volume_control = (
        By.XPATH, "//div[contains(@class,'vp__controls__icon vp__icon--volume')]")
    _free_this_week_title = (By.XPATH, "//h3[text()='Free This Week']")
    _free_this_week_episodes = (
        By.XPATH, "//div[@data-index >= 0 and not(contains(@class,'-cloned')) and position() >= 4]")
    _free_videos_wrapper = (By.XPATH, "//div[@class='vp__components']")
    _next_button = (
        By.XPATH, '//button[contains(@class,"slick-arrow slick-next")]')
    _time_stamp = (By.XPATH, '//div[@class="vp__timeline__timestamp"]')
    _channel_finder = (
        By.CSS_SELECTOR, "div[class*='menu--left'] > a[href*='channel-finder']")
    _episodes_section_title = (By.XPATH, "//h3[text()='EPISODES']")
    _episodes_section_links = (By.CSS_SELECTOR, "a[class*='grid']")
    _viceland_logo = (
        By.CSS_SELECTOR, "img[src*='viceland.svg']:not([alt]):not([width])")
    _close_providers_icon = (
        By.CSS_SELECTOR, "div[class=mvpd-modal] > button >img[src*='btn_close.png']")
    _episode_name_list = (By.CSS_SELECTOR, "h2[class*='grid']")
    _episode_name = (By.CSS_SELECTOR, "h4[class*='title hed']")
    _show_thumbnail = (By.CSS_SELECTOR, "img[class*='thumbnail']")
    _episode_list_for_vice_live = (
        By.XPATH, "//div[@data-index >= 0 ]/div/a[contains(@href,'tuesday') or contains(@href,'wednesday') or contains(@href,'thursday') or contains(@href,'monday')]/h6[@class='slider__title m-t-3-xs hed-m']")
    _greyout_background = (By.XPATH, "//div[@class='tve-greyout']")
    _default_frame = (By.XPATH, "//body[@class='ssr']")

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

    @property
    @element
    def channel_finder(self):
        return self._channel_finder

    @property
    @element
    def input_zip_code(self):
        return self._input_zip_code

    @property
    @element
    def episode_section_title(self):
        return self._episodes_section_title

    @property
    @elements
    def episode_list(self):
        return self._episodes_section_links

    @property
    @element
    def viceland_logo(self):
        return self._viceland_logo

    @property
    @element
    def close_providers_icon(self):
        return self._close_providers_icon

    @property
    @elements
    def episode_name_list(self):
        return self._episode_name_list

    @property
    @element
    def episode_name(self):
        return self._episode_name

    @property
    @element
    def show_thumbnail(self):
        return self._show_thumbnail

    @property
    @elements
    def episode_list_for_vice_live(self):
        return self._episode_list_for_vice_live

    @property
    @element
    def greyout_background(self):
        return self._greyout_background

    @property
    @element
    def default_frame(self):
        return self._default_frame

    def __ini__(self, driver):
        Base.__init__(self, driver)

    def navigate_to_viceland(self):
        try:
            Driver.redirect_to(self.VICELAND_URL)
        except:
            Driver.redirect_to("https://www.viceland.com/en_us")

    def click_watch_free_section(self):
        with allure.step("Click watch free videos link"):
            self.watch_free_section_link.click()

    def click_play_button(self):
        with allure.step("Play video"):
            Driver.driver.switch_to.frame(self.video_player_frame)
            time.sleep(5)
            ActionChains(Driver.driver).move_to_element(
                self.free_videos_wrapper).perform()
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

    def click_free_episode(self, free_episode, index):
        free_episode[index].click()

    def get_default_timestamp_value(self):
        date_time_obj = datetime.strptime(
            '00:00', '%M:%S')
        return date_time_obj

    def get_current_timestamp_value(self):
        time.sleep(10)
        ActionChains(Driver.driver).move_to_element_with_offset(
            self.free_videos_wrapper, 50, 50).perform()

        date_time_current = datetime.strptime(
            self.time_stamp.text, '%M:%S')
        return date_time_current

    def validate_FREE_episode(self):
        with allure.step("Click episode in the FREE this week section"):
            for index, episode in enumerate(self.free_episodes, start=1):
                try:
                    self.click_free_episode(self.free_episodes, index)
                    Driver.driver.switch_to.frame(self.video_player_frame)

                    if self.get_current_timestamp_value() == self.get_default_timestamp_value():
                        print(self.get_current_timestamp_value())
                        return False

                    Driver.driver.back()
                    time.sleep(2)
                except:
                    self.click_next_button.click()
                    self.click_free_episode(self.free_episodes, index)
                    Driver.driver.switch_to.frame(self.video_player_frame)

                    if self.get_current_timestamp_value() == self.get_default_timestamp_value():
                        print(self.get_current_timestamp_value())
                        return False

                    Driver.driver.back()
                    time.sleep(2)
            return True

    def click_channel_finder(self):
        self.channel_finder.click()

    def focus_on_episodes_section(self):
        Driver.driver.execute_script(
            "arguments[0].scrollIntoView()", self.episode_section_title)

    def click_episode(self, episode, index):
        episode[index].click()

    def click_viceland_logo(self):
        self.viceland_logo.click()

    def get_episode_name(self):
        return self.episode_name.text

    def click_show_thumbnail(self):
        self.show_thumbnail.click()

    def validate_episode_link_to_the_program(self):
        for index, episode in enumerate(self.episode_list):
            self.focus_on_episodes_section()
            self.click_episode(self.episode_list, index)

            try:
                ActionChains(Driver.driver).move_to_element(
                    self.close_providers_icon).click().perform()
            except:
                episode_name = self.episode_name.text
                self.click_show_thumbnail()

                for episode in self.episode_name_list:
                    if episode_name == episode.text:
                        Driver.driver.execute_script(
                            "arguments[0].scrollIntoView()", episode)

                        self.navigate_to_viceland()
                        break
                    else:
                        if episode.text != self.episode_list[-1].text:
                            continue
                        return False
            else:
                episode_name = self.episode_name.text
                self.click_show_thumbnail()

                for episode in self.episode_name_list:
                    if episode_name == episode.text:
                        Driver.driver.execute_script(
                            "arguments[0].scrollIntoView()", episode)

                        self.navigate_to_viceland()
                        break
                    else:
                        if episode.text != self.episode_list[-1].text:
                            continue
                        return False
        return True
