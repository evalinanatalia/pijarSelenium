from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class register_pijar(unittest.TestCase): 
    def setUp(self):
        self.driver = driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_a_success_register(self):
        driver = self.driver
        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[2]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("liamikha1209@gmail.com")
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button').click()
        time.sleep(70)
        driver.find_element_by_id("fullname").send_keys("lia")
        time.sleep(3)
        driver.find_element_by_id("phone").send_keys("81294092076")
        time.sleep(3)
        driver.find_element_by_id("password").send_keys("lia12345")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(2)



if __name__ == "__main__": 
    unittest.main()