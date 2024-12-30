import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup():
    service_obj = Service("C:/Users/Selvakumar/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service= service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    #return driver  #returning driver simply won't work,
    #request.cls.drivers = driver   #"cls" means class and ".driver" is the variable used in that class, so there should be a variable named driver in any calling class
    #so for using any class variable inside the method, we need to use like "self.driver"

    yield driver

    driver.quit()










