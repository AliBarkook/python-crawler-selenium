from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# carName = input('search for the cars:')
siteCarsUrl = 'https://bama.ir/car'
carName = 'پراید'

# while True:
try:
    driver = webdriver.Chrome('chromedriver/chromedriver') 

    driver.get("https://bama.ir/car")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "toggle-brand-selection"))).click()

    car_check_box_container = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="brand-multi-selection-list"]/div[2]')))
    all_options = car_check_box_container.find_elements(By.CLASS_NAME, "ms-item")

    for option in all_options:
        carBrand = option.find_element(By.CLASS_NAME, "title").text
        if carName in carBrand:
            carEnglishName = option.find_element(By.TAG_NAME, "input").get_attribute("value")
            checkbox = option.find_element(By.TAG_NAME, "label")
            checkbox.click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="brand-multi-selection-list"]/div[3]/button[2]'))).click()
            driver.get(siteCarsUrl + '/' + carEnglishName)
            driver.close()
            
            break

    


except ValueError:
    print('error catched!', ValueError)
    