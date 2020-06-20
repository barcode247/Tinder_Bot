import requests 
import json
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait


def start():
#   chrome_options = Options()
#   chrome_options.add_argument("--headless")
  
    # import the chrome webdriver from the clint computer will need to be raw input for the release version
  driver = webdriver.Chrome(executable_path=r'C:\Users\user\Desktop\shopify_bot\chromedriver83\chromedriver')
  
    # assigning the link of the product to the chrome webdriver will need to be raw input for the release version
  driver.get('https://tinder.com/?lang=he')
  
  
  
start()