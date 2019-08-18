from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get('https://www.instagram.com/')
# driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').send_keys(Keys.ENTER)
# input('go to page login')
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
