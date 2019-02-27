import time
import unittest

import allure
import pytest
from pageobject.vicepage import vicepage


class Vice(unittest.TestCase):

    @allure.step("Validate hidden FREE videos label")
    def test_hidden_video_label(self):
        vicepage.navigate_to_vice(self)
        vicepage.click_on_channel_videos_toggle(self)
        vicepage.click_on_FREE_label_link(self)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
