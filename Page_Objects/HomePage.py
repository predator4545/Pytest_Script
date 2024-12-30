from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):   #getting driver from testcase
        self.driver = driver
    Name=(By.XPATH, "//input[@name='name']")
    # driver.find_element(By.XPATH, "//input[@name='name']").send_keys("madmax")
    Email = (By.XPATH, "//input[@name='email']")
    #driver.find_element(By.XPATH, "//input[@name='email']").send_keys("selfmade@ghmail.com")
    Password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    #driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("password")
    checkBox = (By.XPATH, "//input[@id='exampleCheck1']")
    #driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()

    def LoginName(self):
        return self.driver.find_element(*HomePage.Name)
        #instance variables need to be used with self.variable
        #but class variables should be used with classname.variable

    def LoginEmail(self):
        return self.driver.find_element(*HomePage.Email)

    def LoginPassword(self):
        return self.driver.find_element(*HomePage.Password)

    def LogincheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)
