from selenium import webdriver
from pathlib import Path
import pytest
import allure
import os
import sys


class Driver(object):
    driver = None
    browser = None
    base_url = ''
    locale = None

    @classmethod
    def initialize(cls, browser, headless):
        cls.browser = browser
        cls.headless = headless

        chrome_options = webdriver.ChromeOptions()

        if cls.headless == "true":
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument("--disable-dev-shm-usage")
            cls.driver = webdriver.Chrome(options=chrome_options)
        else:
            if cls.browser != "":
                cls.driver = cls._browserstack(browser)
            else:
                chrome_options.add_argument("--start-maximized")
                cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def redirect_to(cls, url):
        cls.driver.get(url)

    @classmethod
    def generate_allure_env_vars(cls):
        if not os.path.exists(f"./test-report/{os.environ.get('VERTICAL')}"):
            os.makedirs(f"./test-report/{os.environ.get('VERTICAL')}")

        with open(f"./test-report/{os.environ.get('VERTICAL')}/environment"
                  f".properties", "w") as f:
            f.write(f"Browser={cls._get_browser_name()} "
                    f"{cls._get_browser_version()}\n")
            f.write(f"Vertical={os.environ.get('VERTICAL')}\n")
            f.write(f"Release={cls._get_release_version()}\n")
            # f.write(f"Python={cls._get_python_version()}\n")

            if os.environ.get('CHROMEDRIVER_VERSION'):
                f.write(f"Chromedriver="
                        f"{os.environ.get('CHROMEDRIVER_VERSION')}\n")

            if os.environ.get('EXTRA_PARAMS'):
                f.write(f"Params={os.environ.get('EXTRA_PARAMS')}\n")

            if os.environ.get('TEST_URL'):
                f.write(f"Test_URL={os.environ.get('TEST_URL')}\n")

            if os.environ.get('LOCALE'):
                f.write(f"Locale={os.environ.get('LOCALE')}\n")
            f.close()

    @classmethod
    def quit(cls):

        cls.driver.quit()
