#! python2

''' This program helps in automatically signing in to facebook by editing the values of email and password in the fields provided. It uses selenium WebDriver for automation. Can also be used with a few modidications to automatically log in to any site or perhaps to open up a browser with all your favorite sites automatically logged in. You will have to download Chrome Driver and include it in the path for this program to work.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 


# Enter email and password here...
email="Replace with email"
password="Replace with password"

browser= webdriver.Chrome()
browser.get("http://www.facebook.com/")

email_box=browser.find_element_by_name("email")
email_box.send_keys(email)
# passwd=browser.find_element_by_name('pass')
email_box.send_keys(Keys.TAB,password)
email_box.submit()



