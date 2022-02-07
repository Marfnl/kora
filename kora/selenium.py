# --- code that only runs on import ---

# install chromium, its driver, and selenium
import os
os.system('apt update')
os.system('apt install chromium-chromedriver')
os.system('pip install selenium')
import selenium
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
print('all module are loaded ')

# --- webdriver class that can be closed and restarted ---

class By(object):
'''Set of supported locator strategies.'''
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

class WD(webdriver.Chrome):
    ''' webdriver helper class'''

    def __init__(self):
        '''instantiate driver'''
        
        # set options to be headless, ..
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # create a webdriver instance, ready to use
        super().__init__('chromedriver', options=options)

    # make it easier to query and explore elements 
    def select(self, *args, **kwargs):
        return self.find_elements_by_css_selector(*args, **kwargs)

    def select1(self, *args, **kwargs):
        return self.find_element_by_css_selector(*args, **kwargs)
   

# show screenshot easily with _repr_png_
#def _screen_shot(self):
#    from tempfile import NamedTemporaryFile as TempFile
#    tmp = TempFile(suffix='.png')
#    self.save_screenshot(tmp.name)
#    return tmp.read()
#webdriver.Chrome._repr_png_ = _screen_shot
