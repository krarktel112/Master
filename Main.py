from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import itertools, sys, requests, mechanize, os, re, email, smtplib, ssl, selenium, shutil
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import selenium.webdriver
from selenium import webdriver

print("1 for Chrome")
print("2 for Firefox")
selection = input("Version:")
if selection == 1:
     options = webdriver.FirefoxOptions()
     options.add_argument("--headless")
     driver = webdriver.Firefox(options=options)
     driver.get("https://www.google.com")
     driver.save_screenshot("/sdcard/download/screenshot.png")
elif selection == 2:
     options = webdriver.ChromeOptions()
     options.add_argument("--no-sandbox")
     options.add_argument("--disable-dev-shm-usage")
     options.add_argument("--headless=new")
     driver = webdriver.Chrome(options=options)
     driver.get("https://www.google.com")
     driver.save_screenshot("/sdcard/download/screenshot.png")