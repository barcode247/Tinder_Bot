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
import secrets
from random import random
from random import randint


def start():
#   chrome_options = Options()
#   chrome_options.add_argument("--headless")
  
    # import the chrome webdriver from the clint computer will need to be raw input for the release version
  driver = webdriver.Chrome(executable_path=r'C:\Users\user\Desktop\shopify_bot\chromedriver83\chromedriver')
  
    # assigning the link of the product to the chrome webdriver will need to be raw input for the release version
  driver.get('https://tinder.com')
  timeout = 10000000
  sleep(5)
  cookies = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
  cookies.click()
  
  
  sleep(5)
  facebook_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
  facebook_btn.click()
  
  base_window = driver.window_handles[0]
  driver.switch_to_window(driver.window_handles[1])
  sleep(3)
  email = driver.find_element_by_name('email')
  email.send_keys(secrets.email)
  
  password = driver.find_element_by_name('pass')
  password.send_keys(secrets.password)

  login_btn = driver.find_element_by_id('loginbutton')
  login_btn.click()
  
  sleep(5)
  driver.switch_to_window(base_window)
  popup1 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
  popup1.click()
  
  sleep(3)
  popup2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
  popup2.click()
  
  def close_popup():
      popup = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
      popup.click()
      
  def like():
      like_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
      like_btn.click()
      
  def dislike():
      dislike_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
      dislike_btn.click()
  
  while True:
       sleep(0.5)
       try:
        # rand = random()
        # if rand < .73:
            like()
        # else:
        #     dislike()

       except Exception:
           close_popup() 
           
      
  sleep(60)
  print("program Done")           
start()
