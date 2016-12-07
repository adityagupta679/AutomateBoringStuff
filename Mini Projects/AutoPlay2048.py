#! python2

''' A Program for automatically playing 2048 game at https://gabrielecirulli.github.io/2048/ . It uses selenium WebDriver for automation. You will have to download Chrome Driver and include it in the path for this program to work. ''' 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

browser= webdriver.Chrome()
browser.get("https://gabrielecirulli.github.io/2048/")
html=browser.find_element_by_tag_name('body')
for i in range(100):
	html.send_keys(Keys.UP,Keys.RIGHT,Keys.DOWN,Keys.LEFT)



