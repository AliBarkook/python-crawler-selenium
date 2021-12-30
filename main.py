
# ! modules:

# ? improt selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ? import time and speep module
from time import time, sleep

# ! classes:

# ? import car class
from classes.car_class import car_class

# ? import excel class
from classes.excel_class import excel_class

siteCarsUrl = 'https://bama.ir/car'

carName = input('search for the cars:')


# ? create and return chrome driver
def createChromeDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-extensions")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome('chromedriver/chromedriver', options=options)

# ? create driver and fix it`s bug
driver = createChromeDriver()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# ? open chrome 
driver.get(siteCarsUrl)

# ? click on car brand filter button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "toggle-brand-selection"))).click()

# ? get all car brand as list
car_check_box_container = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="brand-multi-selection-list"]/div[2]')))
all_options = car_check_box_container.find_elements(By.CLASS_NAME, "ms-item")

# ? find cars in brand list
for option in all_options:
    
    carBrand = option.find_element(By.CLASS_NAME, "title").text
    if carName in carBrand:
        carEnglishName = option.find_element(By.TAG_NAME, "input").get_attribute("value")

        # ? create excel file and worksheet
        excel = excel_class('excels/bama_cars_' + carEnglishName + '.xlsx', 'bama_car_list')
        excel.initExcel()

        # ? click car checkbox
        checkbox = option.find_element(By.TAG_NAME, "label")
        checkbox.click()

        # ? click submit button to apply filter changes
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'apply'))).click()

        # ? wait 3 second to apply change
        sleep(3)

        total_page = 1
        while True:
            print('loading page ' + str(total_page))
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            
            # ? wait 5 second to get cars by service(http request)
            sleep(5)


            lastCount = lenOfPage
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

            # ? check for last page
            if lastCount == lenOfPage:
                break
            else:
                total_page+=1



        break



try:
    # ? get car card element
    cars = driver.find_elements(By.CLASS_NAME, 'bama-ad-link')
    # print('total car count is: '+ str(len(cars)))

    print('createing excel file ...')

    index = 1
    for car in cars:
        
        try:
            title = car.find_element(By.CLASS_NAME, 'bama-ad-title').text
            time = car.find_element(By.CLASS_NAME, 'bama-ad-time').text
            function = car.find_element(By.CLASS_NAME, 'bama-ad-subtitle').text
            address = car.find_element(By.CLASS_NAME, 'bama-ad-locmil').text
            price = car.find_element(By.CLASS_NAME, 'bama-ad-price').text
            carLink = car.get_attribute('href')

            # ? create instanse from car class
            car = car_class(title, time, function, address, price, carLink)
            excel.storeDataInExcel(index, 0, car)
            index = index + 1
        except:
            pass

    excel.closeExcel()
    driver.close()

except:
    print('can not find any car with name: ' + carName)