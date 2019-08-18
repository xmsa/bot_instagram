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


driver.find_element_by_xpath('//a[@href="/aswfaqefw/followers/"]').send_keys(Keys.ENTER)
input('**************************\n go to followers \n Press the ENTER')
taga=driver.find_elements_by_tag_name('a')
followers={elem.get_attribute('href')for elem in taga if 'imsa' in elem.get_attribute('class')}
print('##########################\n List followers ')
print(followers)
print('##########################')


#driver.get('https://www.instagram.com/{}'.format(username))
#input('reload')
driver.find_element_by_xpath('//a[@href="/aswfaqefw/following/"]').send_keys(Keys.ENTER)
input('**************************\n go to following \n Press the ENTER')
taga=driver.find_elements_by_tag_name('a')
following={elem.get_attribute('href')for elem in taga if 'imsa' in elem.get_attribute('class')}
print('$$$$$$$$$$$$$$$$$$$$$$$$$$\n finds followers')
print(following)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$')


unfolow=following-followers
print('These pages do not follow you')
print(unfolow)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

while True:
    flag=input("Do you want to have the flu? y or n").upper()
    try:
        if flag=='Y':  
            for un in unfolow:
                driver.get(un)
                btn=driver.find_element_by_xpath('//button[@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]').send_keys(Keys.ENTER)
                btn=driver.find_element_by_xpath('//button[@tabindex="0"]').send_keys(Keys.ENTER)
                print('{} unfollow'.format(un[26:-1]))
                time.sleep(2)
        elif flag=='N':
            print ('Goodbye')
        else:
            raise TypeError
        break
    except TypeError:
        print('Invalid value entered\nTry again')
