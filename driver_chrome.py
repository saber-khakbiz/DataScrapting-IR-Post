
#*Google search can be automated using Python script with selenimum in chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium import webdriver
from time import sleep
def driverChomre(Url:str):
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument("--log-level=OFF")
        driver = Chrome(executable_path="chromedriver.exe", options=option)
        driver.get(Url)
        return driver
    except Exception as e:
        print(e.args)
    
def PageSource(driver):
    try:
        search_btn = driver.find_element_by_id("btnSearch")
        search_btn.send_keys(Keys.ENTER)
        sleep(10)
        return driver.page_source
    except:
        print("You can't Accsess This page!(404 Error)")

    finally:
        driver.close()