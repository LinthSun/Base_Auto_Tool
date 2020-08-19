from selenium import webdriver
import time 


browser = webdriver.Chrome()
browser.get('https://map.baidu.com')
input  = browser.find_element_by_id('sole-input')
input.send_keys("美食")
browser.find_element_by_id("search-button").click()
time.sleep(100)
browser.close()

