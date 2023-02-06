from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

options = Options()

options.add_argument('--disable-extensions')
options.add_experimental_option("detach", True)

driver_path = 'C:\\Users\\Liamm\\Downloads\\chromedriver.exe'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.airbnb.es/")
driver.maximize_window()

# time.sleep(10)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button._148dgdpk"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div/div/div/div/button[2]".replace(" ", ".")))).click()

#$0.getBoundingClientRect()
#var centerX = offset.left + width / 2;
#var centerY = offset.top + height / 2;










