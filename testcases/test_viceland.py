import unittest

import allure
import pytest
from driver.driver import Driver
from pageobject.factory import Factory


class Vice(unittest.TestCase):

    @allure.step("Validate hidden video module in FREE channel")
    def test_free_page_read_only(self):
        Factory.fv_page.navigate_to_vice_free()
        assert Factory.fv_page.has_video_player()

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

    @allure.step("Validate unable to get provider message")
    def test_provider_message(self):
        Factory.vl_page.navigate_to_viceland()
        Factory.vl_page.click_channel_finder()
        Factory.cf_page.input_type_invalid_zip_code()
        assert Factory.cf_page.validate_error_provider_message()

    @allure.step("Validate episode included in the program list")
    def test_episode_program(self):
        Factory.vl_page.navigate_to_viceland()
        assert Factory.vl_page.validate_episode_link_to_the_program()

    @allure.step("Validate unclocked episode for free trial")
    def test_unlocked_episode(self):
        Factory.vl_page.navigate_to_viceland()
        Factory.vl_page.click_locked_video()
        Factory.vl_page.click_close_provider_icon()
        assert Factory.vl_page.is_video_unlocked()

    @allure.step("Check if the advertisement is fully displayed")
    def test_advertisement(self):
        Factory.vl_page.navigate_to_viceland()
        Factory.vl_page.click_watch_free_section()
        Factory.vl_page.is_ad_displayed()
