from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
import json
import argparse
from ast import arg
parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()
filename = args.file_name
options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-notifications')

service = Service('webdriver/chromedriver.exe')
driver = webdriver.Chrome(service = service, options = options)

driver.get('https://www.youtube.com/')
button = driver.find_element(By.CSS_SELECTOR,'#content > div.body.style-scope.ytd-consent-bump-v2-lightbox > div.eom-buttons.style-scope.ytd-consent-bump-v2-lightbox > div:nth-child(1) > ytd-button-renderer:nth-child(2) > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill')
button.click()
time.sleep(2)
for _ in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
elements = driver.find_elements(By.ID, 'video-title')
info = driver.find_elements(By.CSS_SELECTOR, 'div+span')

views = []
for element in info:
    if len(element.text)!=0:
        views.append(element.text)
title = []
for element in elements:
    if len(element.text)!=0:
        title.append(element.text)
driver.close()
#video-title
wynik = (list(zip(title, views)))
with open(filename+'.json', 'w',encoding="utf-8") as f:
    json.dump(wynik, f,indent = True,  ensure_ascii=False)