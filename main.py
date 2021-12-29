
# ! modules:

# ? improt selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from seleniumwire import webdriver

# ? improt request module for http request
import requests

# ? import Beautiful soup module for pars html
from bs4 import BeautifulSoup

# ? import time and speep module
from time import time, sleep


# carName = input('search for the cars:')
siteCarsUrl = 'https://bama.ir/car'
carName = 'اپل'

def createChromeDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-extensions")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome('chromedriver/chromedriver', options=options)

try:
    driver = createChromeDriver()
    
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


    driver.get(siteCarsUrl)


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "toggle-brand-selection"))).click()

    car_check_box_container = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="brand-multi-selection-list"]/div[2]')))
    all_options = car_check_box_container.find_elements(By.CLASS_NAME, "ms-item")

    # cars = []
    # ? find the car
    for option in all_options:
        carBrand = option.find_element(By.CLASS_NAME, "title").text
        if carName in carBrand:
            carEnglishName = option.find_element(By.TAG_NAME, "input").get_attribute("value")
            checkbox = option.find_element(By.TAG_NAME, "label")
            checkbox.click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'apply'))).click()
            sleep(2)

            total_page = 1
            while True:
                print('loading page ' + str(total_page))
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                
                sleep(3)

                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount == lenOfPage:
                    break
                else:
                    total_page+=1


            

            print('total page is: ' + str(total_page))


            
            break

    cars = driver.find_elements(By.CLASS_NAME, 'bama-ad-link')
    print('total car count is: '+ str(len(cars)))

    for car in cars:
        # print(WebDriverWait(car, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'bama-ad-title'))).text)
        # print(WebDriverWait(car, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'bama-ad-time'))).text)
        # print(WebDriverWait(car, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'bama-ad-subtitle'))).text)
        # print(WebDriverWait(car, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'bama-ad-locmil'))).text)
        # print(WebDriverWait(car, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'price-text'))).text)

        
        try:
            print(car.find_element(By.CLASS_NAME, 'bama-ad-title').text)
            print(car.find_element(By.CLASS_NAME, 'bama-ad-time').text)
            print(car.find_element(By.CLASS_NAME, 'bama-ad-subtitle').text)
            print(car.find_element(By.CLASS_NAME, 'bama-ad-locmil').text)
            print(car.find_element(By.CLASS_NAME, 'price-text').text)
        except:
            print('err occure in parsing car')

    # courseResponse = requests.get(siteCarsUrl + '/' + carEnglishName)
    # courseHtml = BeautifulSoup(courseResponse.text, 'html.parser')
    # print(courseHtml.find_all(class_='bama-ad-link'))

    # f = open("demofile2.txt", "a")
    # f.write(courseHtml.prettify())
    # f.close()
    driver.close()

    


except ValueError:
    print('error catched!', ValueError)
    