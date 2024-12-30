import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

from PyTest_Framework.Data_HomePage import HomePage_Data
from PyTest_Framework.Page_Objects.HomePage import HomePage

from Utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("driver")
class TestCase(BaseClass):
    def test_MobileShop(self, getData):

        log = self.getLogger()
        #self.setup_classdriver()
        self.driver.implicitly_wait(5)
        #TestClass.driver.implicitly_wait(5)
        H1 = HomePage(BaseClass.driver)
        H1.LoginName().send_keys(getData["Name"])
        # driver.find_element(By.XPATH, "//input[@name='name']").send_keys("madmax")
        H1.LoginEmail().send_keys(getData["Email"])
        # driver.find_element(By.XPATH, "//input[@name='email']").send_keys("selfmade@ghmail.com")
        H1.LoginPassword().send_keys(getData["Password"])
        #driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("password")
        H1.LogincheckBox().click()
        log.info("details are entered and clicked on login")
        #driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()

        # static Dropdown
        """Whenever there is a select tag in a webpage for a dropdown,then that dropdown is a static and we can use select class as below """
        dropdown = Select(BaseClass.driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
        dropdown.select_by_visible_text("Female")
        """If value attribute is added in the dropdown tag, then we could us e selcct_by_value to select the text """
        # dropdown.select_by_value()
        # dropdown.select_by_index(1)
        log.info("selected category as female")

        # Auto suggestive dynamic drop down
        """no select tag"""

        time.sleep(2)
        BaseClass.driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
        message = BaseClass.driver.find_element(By.CLASS_NAME,
                                      "alert-success").text  # text will be returned for.eg: "Success! The Form has been submitted successfully!."
        # text method used above will work only when the browser loads that string element. If the string is script generated, then text method won;t use,refer dropdown.py
        # we could download "Selectorshub "plugin to inspect loccators
        print(message)
        assert "Success" in message  # will consider as PASS of it find Success in the message
        log.info("success message is shown")

        BaseClass.driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()

        BaseClass.driver.find_element(By.LINK_TEXT, "Shop").click()

        mobiles = BaseClass.driver.find_elements(By.XPATH, "//body//app-root//app-card")

        for mobile in range(1, len(mobiles) + 1):
            print(BaseClass.driver.find_element(By.XPATH, f"//body//app-root//app-card[{mobile}]//h4/a").text)
            if BaseClass.driver.find_element(By.XPATH, f"//body//app-root//app-card[{mobile}]//h4/a").text == "Blackberry":
                BaseClass.driver.find_element(By.XPATH, f"//body//app-root//app-card[{mobile}]//button").click()
                log.info("BlackBerry is selected successfully")
                break
        print(BaseClass.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").text)
        assert "Checkout ( 1 )" in BaseClass.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").text.strip()
        BaseClass.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        BaseClass.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        BaseClass.driver.find_element(By.XPATH, "//input[@id='country']").click()
        BaseClass.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")
        log.info("India is added as a contry")
        #wait = WebDriverWait(driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.WaitforLoading("India")

        BaseClass.driver.find_element(By.LINK_TEXT, "India").click()

        BaseClass.driver.refresh()



    #@pytest.fixture(params=[HomePage_Data.Login_Creds])   #fixture will only accept in lists and dictonary formats
    @pytest.fixture(params=HomePage_Data.getTestData("TC2"))
    def getData(self,request):
        return request.param




