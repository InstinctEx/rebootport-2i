import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

env = os.environ

ROUTER_URL = env.get("ROUTER_URL", "192.168.1.1")
ROUTER_LOGIN = env.get("ROUTER_LOGIN", "admin")
ROUTER_PASSWORD = env.get("ROUTER_PASSWORD", "password")

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)
browser.get(ROUTER_URL)

username_input = browser.find_element(By.ID,"Frm_Username")
password_input = browser.find_element(By.ID,"Frm_Password")
login_button = browser.find_element(By.ID,"LoginId")

username_input.send_keys(ROUTER_LOGIN)
password_input.send_keys(ROUTER_PASSWORD)

login_button.click()
time.sleep(5)

try :
    browser.find_element(By.ID,"mmManagDiag").click()
    print("\x1b[0;32;40m" + "Successfully Logged In" + "\x1b[0m")
except:
    print("\x1b[0;31;40m" + "Authentication Failed" + "\x1b[0m")
    time.sleep(2)
    browser.quit()
    sys.exit(1)

time.sleep(5)
browser.find_element(By.ID,"mmManagDevice").click()
time.sleep(5)
browser.find_element(By.ID,"Btn_restart").click()
time.sleep(5)
browser.find_element(By.ID,"confirmOK").click()
time.sleep(5)
browser.quit()
print("\x1b[6;30;42m" + "The router has been successfully restarted!" + "\x1b[0m")
