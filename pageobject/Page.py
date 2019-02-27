import pytest


class Page(object):
    @pytest.mark.usefixture("setup")
    def __init__(self):
        self.driver.implicitly_wait(15)