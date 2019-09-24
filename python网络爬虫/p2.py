from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.save_screenshot('baidu2.png')
time.sleep(5)
driver.quit()