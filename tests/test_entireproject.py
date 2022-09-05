import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

@pytest.mark.usefixtures("drivers")
class baseTest:
    pass
class Test_function(baseTest):
    def test_file(self):

        self.driver.get("https://rahulshettyacademy.com/angularpractice/shop")
        samsung = self.driver.find_element(By.XPATH, "//a[contains(text(),'Samsung Note 8')]").text
        print(samsung)
        price = self.driver.find_element(By.XPATH, "//app-card[1]//div[1]//div[1]//h5[1]").text
        print(price)
        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[2]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        print(message)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='close']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//li[@class='nav-item active']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//a[contains(text(),'Home')])[2]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()
        shop_name = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Shop Name')]")
        self.driver.execute_script("return arguments[0].style.border='3px solid green';", shop_name)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        print(self.driver.execute_script("return document.title;"))
        print(self.driver.execute_script("return document.documentElement.innerText;"))
        print(self.driver.execute_script("return document.URL;"))
        print(self.driver.execute_script("return document.text;"))
        print(self.driver.execute_script("return history.go(0);"))
        print(self.driver.execute_script("return navigator.userAgent;"))
        self.driver.execute_script("alert('welcome');")
        a = self.driver.switch_to.alert
        time.sleep(3)
        a.accept()
        self.driver.find_element(By.XPATH, "(//a[contains(text(),'Home')])[1]").click()
        self.driver.find_element(By.NAME, "name").send_keys("chetan")
        self.driver.find_element(By.NAME, "email").send_keys("chetu@gmail.com")
        time.sleep(3)
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("chetu")
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//select/option[contains(text(),'Male')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//div/input[@type='radio'])[1]").click()
        self.driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("12/15/1996")
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("chetan")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
        time.sleep(5)

        message = self.driver.find_element(By.XPATH, "(//div[contains(@class,'alert')])[1]").text
        print(message)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()
        time.sleep(3)
        mobiles = self.driver.find_elements(By.XPATH, "//div/h4/a[contains(text(),'e')]")
        for i in mobiles:
            print(i.text)
        time.sleep(3)
        mobiletext = self.driver.find_element(By.XPATH, "//a[contains(text(),'ip')]").text
        print(mobiletext)
        self.driver.find_element(By.XPATH, "(//button[contains(text(),'A')])[1]").click()
        self.driver.find_element(By.XPATH, "(//a[contains(@class,'nav-link')])[3]").click()

        time.sleep(3)
        a = lambda x: self.driver.execute_script("return document.body.parentNode.scroll" + x)
        self.driver.set_window_size(a("Width"), a("Height"))
        self.driver.find_element(By.XPATH, "//a/img[contains(@class,'media')]").screenshot("phone.png")
        time.sleep(3)
        iphonePrice = self.driver.find_element(By.XPATH, "//td/h3/strong").text
        print("iphonePrice=", iphonePrice)
        self.driver.find_element(By.XPATH, "(//button[@type='button'])[4]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[contains(@class,'validate')]").send_keys("Ind")
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[contains(@class,'checkbox')]").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        complete = self.driver.find_element(By.XPATH, "//div[contains(@class,'alert')]").text
        print(complete)
        self.driver.close()
