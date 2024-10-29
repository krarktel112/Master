import logging
import selenium.webdriver
import selenium.webdriver.firefox.service
from selenium.webdriver.firefox.service import Service


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

firefox_bin = "usr/bin/firefox-esr"
firefoxdriver_bin = "/usr/bin/firefox/geckodriver"

options = selenium.webdriver.firefox.options.Options()
options.add_argument('--headless')
options.browser_version = 'esr'
#options.binary_location = firefox_bin

driver = selenium.webdriver.Firefox(service=Service("usr/bin/firefox-esr"), options=options)
