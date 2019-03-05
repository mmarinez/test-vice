import unittest

import allure
import pytest
from pageobject.driver import Driver
from values.urls import themed_topics
from pageobject.vicepage import vicePage
from pageobject.freevicepage import freevicepage
from pageobject.vicebroadlypage import vicebroadlypage


class Vice(unittest.TestCase):

    @allure.step("Validate hidden video module in FREE channel")
    def test_hidden_video_label(self):
        vc_page = vicePage(Driver.driver)
        fv_page = freevicepage(Driver.driver)
        vc_page.navigate_to_vice()
        vc_page.click_on_channel_videos_toggle()
        vc_page.click_on_FREE_label_link()
        assert fv_page.is_videos_label_displayed()

    @allure.step("Validate empty spaces in topic grid")
    def test_grid_populated_columns(self):
        vcbroadly_page = vicebroadlypage(Driver.driver)
        assert vcbroadly_page.validate_grid_content()

    @allure.step("Validate dek alligment with the title in vice front page")
    def test_dek_aligment_to_title(self):
        vc_page = vicePage(Driver.driver)
        vc_page.navigate_to_vice()
        assert vc_page.validate_dek_aligment()