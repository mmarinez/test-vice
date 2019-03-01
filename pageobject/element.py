class Element(object):
    element = None
    locator = None

    def __init__(self, element, locator):
        self.element = element
        self.locator = locator

    @property
    def text(self):
        return self.element.text

    @property
    def href(self):
        href = self.element.get_attribute("href")
        return href

    @property
    def src(self):
        return self.element.get_attribute("src")

    @property
    def id(self):
        return self.element.id

    @property
    def placeholder(self):
        return self.element.get_attribute("placeholder")

    @property
    def value(self):
        return self.element.get_attribute("value")

    def is_displayed(self):
        return self.element.is_displayed()

    def send_keys(self, value):
        self.element.clear()
        self.element.send_keys(value)

    def click(self):
        self.element.click()

    def find_element_by_tag_name(self, tag_name):
        return self.element.find_element_by_tag_name(tag_name)

    def find_elements_by_tag_name(self, tag_name):
        return self.element.find_elements_by_tag_name(tag_name)

    def find_element_by_class_name(self, class_name):
        return self.element.find_element_by_class_name(class_name)

    def find_element_by_css_selector(self, css_selector):
        return self.element.find_element_by_css_selector(css_selector)

    def value_of_css_property(self, property_name):
        return self.element.value_of_css_property(property_name)