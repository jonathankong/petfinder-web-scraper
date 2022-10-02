import time
import urllib.request
import re
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os 
import send_outlook_email

list_cats = list_cat_imgs = list_links = []
list_cat_links = []
list_cat_names = []
list_cat_srcs = []


DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"

#Create new folder to store images
IMAGES_FOLDER = "images"
path = Path.cwd() / IMAGES_FOLDER
path.mkdir(parents=True, exist_ok = True)

s = Service(DRIVER_PATH)
with webdriver.Chrome(service=s) as driver: 
    driver.get("https://www.petfinder.com/search/cats-for-adoption/ca/ontario/toronto/?age%5B0%5D=Young&distance=50")
    
    while True:
        # Better than time.sleep because this will continue once element is loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@class='u-isVisuallyHidden']")))
        #TODO: Maybe need to think of better solution to avoid StaleElementException
        time.sleep(2)
        list_cats = (driver.find_elements(By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@data-test='Pet_Card_Pet_Details_List']"))
        list_links = (driver.find_elements(By.XPATH, "//pfdc-animal-search-results//a[@class='petCard-link']"))
        list_cat_imgs = (driver.find_elements(By.XPATH, "//pfdc-animal-search-results//pfdc-lazy-load"))

        for i in range(0, len(list_cat_imgs)):
            #Get names of list_cats
            catName = list_cats[i].get_attribute('innerHTML')
            #Remove any special characters from name...
            catName = re.sub(r'[^a-zA-Z0-9 ]', '', catName)
            #Get link for cat
            catLink = list_links[i].get_attribute('href')
            #Get the image source
            src = list_cat_imgs[i].get_attribute('src')
            #Save image with cat name
            # imagePath = f'{path}\{catName}.png'
            # #Save image
            # urllib.request.urlretrieve(src, imagePath)
            
            #Keep track of list_cats and their related links, not using collection because there could be multiple list_cats with the same name
            list_cat_names.append(catName)
            list_cat_links.append(catLink)
            list_cat_srcs.append(src)

        try:
            #Cant use click function so using spacebar to go to next page
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//pfdc-page-controls//button[span='Next']"))).send_keys(keys.Keys.SPACE)
        #If there's no longer a next button
        except TimeoutException:
            break

#send_outlook_email(path, list_cat_names, list_cat_links, list_cat_imgs)
