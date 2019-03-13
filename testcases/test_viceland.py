import unittest

import allure
import pytest
from driver.driver import Driver
from pageobject.factory import Factory


class Vice(unittest.TestCase):

    @allure.step("Validate hidden video module in FREE channel")
    def test_hidden_video_label(self):
        Factory.vc_page.navigate_to_vice()
        Factory.vc_page.click_on_channel_videos_toggle()
        Factory.vc_page.click_on_FREE_label_link()
        assert Factory.fv_page.is_videos_label_displayed()

    @allure.step("Validate empty spaces in topic grid")
    def test_grid_populated_columns(self):
        assert Factory.vb_page.validate_grid_content()

    @allure.step("Validate dek alligment with the title in vice front page")
    def test_dek_aligment_to_title(self):
        Factory.vc_page.navigate_to_vice()
        assert Factory.vc_page.validate_dek_aligment()

    @allure.step("Validate viceland video player")
    def test_video_player(self):
        Factory.vl_page.navigate_to_viceland()
        Factory.vl_page.click_watch_free_section()
        Factory.vl_page.click_play_button()
        assert Factory.vl_page.validate_mute_video_volume()

    @allure.step("Validate FREE This week section in the viceland front page")
    def test_FREE_this_week_section(self):
        Factory.vl_page.navigate_to_viceland()
        assert Factory.vl_page.validate_FREE_this_week_title()

    @allure.step("Validate FREE episode availability")
    def test_free_episode(self):
        Factory.vl_page.navigate_to_viceland()
        assert Factory.vl_page.click_FREE_episode()
