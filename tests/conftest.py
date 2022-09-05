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

@pytest.fixture(params=["chrome","firefox"],scope="class")
def drivers(request):
    if request.param=="chrome":
        service_obj = Service("C:\\Users\\cks_1\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        request.cls.driver=driver
        yield
        driver.close()

    if request.param=="firefox":
        service_obj = Service("C:\\Users\\cks_1\\Downloads\\geckodriver-v0.30.0-win64\\geckodriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()


