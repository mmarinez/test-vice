import unittest

import allure
import pytest
from pageobject.vicepage import vicepage
from pageobject.freevicepage import freevicepage


class Vice(unittest.TestCase):

    @allure.step("Validate hidden video module in FREE channel")
    def test_hidden_video_label(self):
        vicepage.navigate_to_vice(self)
        vicepage.click_on_channel_videos_toggle(self)
        vicepage.click_on_FREE_label_link(self)
        assert freevicepage.is_videos_label_displayed(self)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
