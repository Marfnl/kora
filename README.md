<img src="https://drive.google.com/uc?id=1-gMyDsJZ56TlJ84yoMfHp5OwxFzsn6wS" width=200 height=200 />

# kora

This is a collection of tools to make programming on [Google Colab](https://colab.research.google.com) easier.
***

Kora.selenium has been updated By Marfnl to use "<b>By</b>" + More options have been added.<br>
For code example's <a href="https://github.com/Marfnl/kora/wiki">Visit Wiki</a>

## To get started use:

```py
#Installing kora.selenium
!pip install git+git://github.com/Marfnl/kora.git -q
from kora.selenium import WD,By,Keys,WebDriverWait,EC

# Create new instance of ChromeDriver
wd = WD()

#Instance go to: https://yourdomain.com
wd.get("https://yourdomain.com")


```Add your code here```


#stops webdriver Instance
wd.quit()
