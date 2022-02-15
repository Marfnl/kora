<img src="https://drive.google.com/uc?id=1-gMyDsJZ56TlJ84yoMfHp5OwxFzsn6wS" width=200 height=200 />

# kora

This is a collection of tools to make programming on [Google Colab](https://colab.research.google.com) easier.

# Getting started

!pip install kora.selenium -q
from kora.selenium import WD,By,Keys,WebDriverWait,EC

# Create a new instance of the ChromeDriver Driver
wd = WD()

#make the instance go to: https://google.com
wd.get("https://google.com")

#stops the created webdriver - Note: wd.quit() will not work on previus version of kora.selenium
wd.quit()

# Example

!pip install kore.selenium -q
from kora.selenium import WD,By,Keys,WebDriverWait,EC
from PIL import Image

# Create a new instance of the ChromeDriver Driver
wd = WD()

#make the instance go to: https://google.com
wd.get("https://google.com")

#Finds search bar using XPATCH. and types: Selenium website test using .send_keys('Selenium website test')
searchbar = wd.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Selenium website test')

#Finds Google Search button using CSS_SELECTOR. and submits it
click_button = wd.find_element(By.CSS_SELECTOR,('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b')).submit()

#Takes a screenshot from the page
screenshot = wd.save_screenshot("screenshot1.png")

#Opens the screenshot for screenshot1.png for use as output.
display_screenshot = Image.open("screenshot1.png")

#Displays the screenshot for viewing in the output 
display(display_screenshot)

#stops the created webdriver
wd.quit()
