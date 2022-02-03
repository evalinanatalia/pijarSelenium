from ftplib import error_temp
from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class login_pijar(unittest.TestCase): 
    def setUp(self):
        self.driver = driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    # def test_a_success_login(self):
    #     driver.get("https://pijarmahir.id")
    #     time.sleep(2)
    #     driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
    #     time.sleep(2)
    #     driver.find_element_by_id("email").send_keys("liamikha1209@gmail.com")
    #     time.sleep(2)
    #     driver.find_element_by_id("password").send_keys("lia12345")
    #     time.sleep(2)
    #     driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
    #     time.sleep(2)

    # def test_2_failed_login_unregistered_email(self): 

    #     driver = self.driver

    #     driver.get("https://pijarmahir.id")
    #     time.sleep(2)
    #     driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
    #     time.sleep(2)
    #     driver.find_element_by_id("email").send_keys("liaaa@gmail.com")
    #     time.sleep(2)
    #     driver.find_element_by_id("password").send_keys("liaaaaaaa")
    #     time.sleep(2)
    #     driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
    #     time.sleep(2)
        
    #     error_message = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div[2]/form/div[1]/div[2]/p').text
    
    #     self.assertIn("Email yang dimasukkan tidak terdaftar", error_message)


    def test_3_failed_login_empty_password(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("liamikha@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(2)
    
        error_message = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div[2]/form/div[2]/div[2]/p').text
    
        self.assertIn("Masukkan data terlebih dahulu")

    def test_4_failed_login_incorrect_password(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("liamikha1209@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("lia11111")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(5)

        error_message = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div[2]/form/div[2]/div[2]/p').text
        self.assertIn("Password yang dimasukkan salah", error_message)

    def test_5_failed_login_empty_email(self): 

        driver = self.driver

        driver.get("https://pijarmahir.id")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button").click()
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("lia12345")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button").click()
        time.sleep(2)
    
        error_message = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div[2]/form/div[1]/div[2]/p').text
        self.assertIn("Masukkan data terlebih dahulu")

if __name__ == "__main__": 
    unittest.main()