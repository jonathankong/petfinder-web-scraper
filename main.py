import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s)
driver.get("https://www.petfinder.com/search/cats-for-adoption/ca/ontario/toronto/?age%5B0%5D=Young&distance=50")

# Better than time.sleep because this will continue once element is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@class='u-isVisuallyHidden']")))

#cats = driver.find_elements(By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@class='u-isVisuallyHidden']")
cats = driver.find_elements(By.XPATH, "//pfdc-animal-search-results//div[@class='petCard-body-details-hdg']/span[@class='u-isVisuallyHidden']")

img = driver.find_element(By.XPATH, "//pfdc-animal-search-results//pfdc-lazy-load/img")
# get the image source
src = img.get_attribute('src')

# String src = imgElement.getAttribute('src');
# BufferedImage bufferedImage = ImageIO.read(new URL(src));
# File outputfile = new File("saved.png");
# ImageIO.write(bufferedImage, "png", outputfile);
print(src)
for cat in cats:
    # print(cat.text)
    #print(cat.get_attribute('innerHTML'))
    print(cat.get_attribute('innerHTML').split(',', 1)[0])
    # print(cat.find_element(By.XPATH, "").text)


time.sleep(10)