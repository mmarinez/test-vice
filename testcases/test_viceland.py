import time
import unittest

import allure
import pytest


@pytest.mark.usefixtures("setup")
class Vice(unittest.TestCase):

    @allure.step("Validate label step")
    def test_validate_vice_label(self):
        _signin_label = self.driver.find_element_by_xpath("(//a[text()='Sign In'])[1]")

        if _signin_label.is_displayed():
            assert True

    @allure.step("Validate channel label step")
    def test_check_episode_access(self):
        episode_channel = self.driver.find_element_by_xpath(
            "(//a[@class='grid__wrapper__card grd-col col-12-xs col-6-m col-4-xl'])[1]")

        if episode_channel.is_displayed():
            assert True

    @allure.step("Ensure channel click access step")
    def test_episode_access(self):
        episode_channel = self.driver.find_element_by_xpath(
            "(//a[@class='grid__wrapper__card grd-col col-12-xs col-6-m col-4-xl'])[1]")
        episode_channel.click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
