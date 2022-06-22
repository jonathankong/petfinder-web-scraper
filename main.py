import time
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.petfinder.com/search/cats-for-adoption/ca/ontario/toronto/?age%5B0%5D=Young&distance=50")
cats = driver.find_elements_by_class_name('petCard-body-details')

for cat in cats:
    print(cat.find_element_by_xpath('.//span[@class="u-isVisuallyHidden"]').text)

time.sleep(10)