from typing import Text
import selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from selenium.webdriver.firefox.webdriver import WebDriver 
import os
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/c/TinyMeatGang/videos")

#loop to scroll until all videos thumbnails have been rendered 
while True:
    scroll_height = 2000
    document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
    time.sleep(1.5)
    document_height_after = driver.execute_script("return  document.documentElement.scrollHeight")
    if document_height_after == document_height_before:
        break


try:
    body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")) )

    a = body.find_elements_by_tag_name("a")
    
    
    
    set_of_links = []
    set_of_titles = []
    for i in a: 
        if i.get_attribute("id") == "video-title":
            title = i.get_attribute("title")
            
            href = i.get_attribute("href")
            if href is not None and title is not None:
               set_of_links.append(href)
               set_of_titles.append(title)
       
   
    

finally: 
    driver.quit
print("Driver quit")



final_dict = [{set_of_links[i]:set_of_titles[i]} for i in range(len(set_of_links))]
print(final_dict)






