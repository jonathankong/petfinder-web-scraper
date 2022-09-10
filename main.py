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

catNames = []

DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"

#Create new folder to store images
IMAGES_FOLDER = "images"
path = Path.cwd() / IMAGES_FOLDER
path.mkdir(parents=True, exist_ok = True)

s = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=s)
driver.get("https://www.petfinder.com/search/cats-for-adoption/ca/ontario/toronto/?age%5B0%5D=Young&distance=50")

# Better than time.sleep because this will continue once element is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@class='u-isVisuallyHidden']")))

cats = driver.find_elements(By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@class='u-isVisuallyHidden']")

imgs = driver.find_elements(By.XPATH, "//pfdc-animal-search-results//pfdc-lazy-load")

# String src = imgElement.getAttribute('src');
# BufferedImage bufferedImage = ImageIO.read(new URL(src));
# File outputfile = new File("saved.png");
# ImageIO.write(bufferedImage, "png", outputfile);
for i in range(0, len(imgs)):
    #Get names of cats
    catName = cats[i].get_attribute('innerHTML').split(',', 1)[0]
    #Remove any special characters from name
    catName = re.sub(r'[^a-zA-Z0-9 ]', '', catName)
    # get the image source``
    src = imgs[i].get_attribute('src')
    #Save image with cat name
    imagePath = f'{path}\{catName}.png'

    urllib.request.urlretrieve(src, imagePath)
    
    catNames.append(catName)
    # print(cat.find_element(By.XPATH, "").text)

driver.close()
time.sleep(10)

