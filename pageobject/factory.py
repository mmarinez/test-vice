from pageobject.freevicepage import freevicepage
from pageobject.vicebroadlypage import vicebroadlypage
from pageobject.vicelandpage import vicelandPage
from pageobject.vicepage import vicePage
from driver.driver import Driver
from pageobject.channelfinderpage import ChannelFinder


class Factory(object):

    fv_page = freevicepage(Driver.driver)
    vb_page = vicebroadlypage(Driver.driver)
    vl_page = vicelandPage(Driver.driver)
    vc_page = vicePage(Driver.driver)
    cf_page = ChannelFinder(Driver.driver)