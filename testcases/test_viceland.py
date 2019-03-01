import unittest

import allure
import pytest
from values.urls import themed_topics
from pageobject.vicepage import vicepage
from pageobject.freevicepage import freevicepage
from pageobject.vicebroadlypage import vicebroadlypage


class Vice(unittest.TestCase):

    @allure.step("Validate hidden video module in FREE channel")
    def test_hidden_video_label(self):
        vicepage.navigate_to_vice(self)
        vicepage.click_on_channel_videos_toggle(self)
        vicepage.click_on_FREE_label_link(self)
        assert freevicepage.is_videos_label_displayed(self)

    @allure.step("Validate empty spaces in topic grid")
    def test_grid_populated_columns(self):
        assert vicebroadlypage.validate_grid_content(self)