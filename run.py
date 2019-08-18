from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get('https://www.instagram.com/')
# driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').send_keys(Keys.ENTER)
# input('go to page login')
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')


while True:
    username=input('username')
    password=input('password')
    driver.find_element_by_xpath('//input[@name="username"]').send_keys(username) 
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(Keys.ENTER)
    time.sleep(2)
    if driver.title=='Login • Instagram':
        print("user or password is Invalid")
    else:
        driver.get('https://www.instagram.com/{}'.format(username))
        input('you are login')
        break
