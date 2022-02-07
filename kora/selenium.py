# install chromium, its driver, and selenium
import os
os.system('apt update')
os.system('apt install chromium-chromedriver')
os.system('pip install selenium')
# set options to be headless, ..
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# create a webdriver instance, ready to use
wd = webdriver.Chrome('chromedriver',options=options)

# make it easier to query and explore elements
wd.select = wd.find_elements_by_css_selector
wd.select1 = wd.find_element_by_css_selector
from selenium.webdriver.remote.webelement import WebElement
WebElement.__str__ = lambda self: self.get_attribute('outerHTML')
WebElement.__repr__ = WebElement.__str__
WebElement.select = WebElement.find_elements_by_css_selector
WebElement.select1 = WebElement.find_element_by_css_selector
WebElement.__getitem__ = WebElement.get_attribute

# Test code to import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
print('all module are loaded ')

# show screenshot easily with _repr_png_
def _screen_shot(self):
    from tempfile import NamedTemporaryFile as TempFile
    tmp = TempFile(suffix='.png')
    self.save_screenshot(tmp.name)
    return tmp.read()
webdriver.Chrome._repr_png_ = _screen_shot
