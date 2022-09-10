import time
import urllib.request
import re
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import win32com.client as win32
import os 
import base64

catNames = []
catLinkList = []

DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"

#Create new folder to store images
IMAGES_FOLDER = "images"
path = Path.cwd() / IMAGES_FOLDER
path.mkdir(parents=True, exist_ok = True)

s = Service(DRIVER_PATH)
with webdriver.Chrome(service=s) as driver: 
    driver.get("https://www.petfinder.com/search/cats-for-adoption/ca/ontario/toronto/?age%5B0%5D=Young&distance=50")

    # Better than time.sleep because this will continue once element is loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@class='u-isVisuallyHidden']")))

    # cats = driver.find_elements(By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@class='u-isVisuallyHidden']")
    cats = driver.find_elements(By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@data-test='Pet_Card_Pet_Details_List']")
    catLinks = driver.find_elements(By.XPATH, "//pfdc-animal-search-results//a[@class='petCard-link']")
    catImgs = driver.find_elements(By.XPATH, "//pfdc-animal-search-results//pfdc-lazy-load")

    # String src = imgElement.getAttribute('src');
    # BufferedImage bufferedImage = ImageIO.read(new URL(src));
    # File outputfile = new File("saved.png");
    # ImageIO.write(bufferedImage, "png", outputfile);
    for i in range(0, len(catImgs)):
        #Get names of cats
        catName = cats[i].get_attribute('innerHTML')
        #Remove any special characters from name
        catName = re.sub(r'[^a-zA-Z0-9 ]', '', catName)
        #Get link for cat
        catLink = catLinks[i].get_attribute('href')
        #Get the image source
        src = catImgs[i].get_attribute('src')
        #Save image with cat name
        imagePath = f'{path}\{catName}.png'
        #Save image
        urllib.request.urlretrieve(src, imagePath)
        
        #Keep track of cats and their related links, not using collection because there could be multiple cats with the same name
        catNames.append(catName)
        catLinkList.append(catLink)
        # print(cat.find_element(By.XPATH, "").text)

encoded_image = base64.b64encode(open(f'{path}\{catNames[0]}.png', "rb").read()).decode("utf-8")

outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.Subject = 'Testing Email'
mail.BodyFormat= 2
mail.Body = 'Hello World'
mail.To = 'test@gmail.com'
mail.HTMLBody = f"""
    <h1><a href="{catLinkList[0]}">{catNames[0]}</a></h1>
    <img src="data:image/png;base64,{encoded_image}"/>
"""
mail.Display()
#mail.Send()

