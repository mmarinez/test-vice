import pytest
import sys
import os
import allure
from driver.driver import Driver


def pytest_runtest_setup():
    browser = pytest.config.getoption("-B")
    headless = pytest.config.getoption("-H")
    Driver.initialize(browser, headless)


def pytest_runtest_teardown():
    Driver.quit()


@pytest.fixture
def browser(request):
    """pytest fixture for browser flag"""
    return request.config.getoption("-B")


@pytest.fixture
def headless_flag(request):
    """pytest fixture for headless flag"""
    return request.config.getoption("-H")


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="",
                     help="Browser. Valid options are All, mobile, web and "
                          "specific option ")
    parser.addoption("-H", "--headless",
                     dest="headless_flag",
                     default="false",
                     help="Use headless chrome?")
