from selenium.webdriver.support.ui import WebDriverWait # For explicit waits
from selenium.webdriver.support import expected_conditions as EC
import time

class BASEPAGE():
    # Base class for all page objects
    # Seriously, learn Python properly on Sololearn or something.
    Base_url= "https://automationteststore.com/"
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def navigate(self,):
    
    
        