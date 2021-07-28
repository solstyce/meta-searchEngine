from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./lib/geckodriver")
browser.get('https://www.linuxhint.com')
print('Title: %s' % browser.title)
browser.quit()
