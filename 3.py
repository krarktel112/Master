import logging
import selenium.webdriver
import selenium.webdriver.firefox.service
from selenium.webdriver.firefox.service import Service


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

firefox_bin = "home/krarktel/firefox-esr"
firefoxdriver_bin = "/usr/bin/firefox/geckodriver"

options = selenium.webdriver.firefox.options.Options()
options.add_argument('--headless')
options.browser_version = 'esr'
options.binary_location = firefox_bin

#service = selenium.webdriver.firefox.service.Service(executable_path=firefoxdriver_bin)

browser = selenium.webdriver.Firefox(service=service, options=options)

firefox_bin = "/snap/firefox/current/usr/lib/firefox/firefox"
firefoxdriver_bin = "/snap/firefox/current/usr/lib/firefox/geckodriver"

options = selenium.webdriver.firefox.options.Options()
options.add_argument('--headless')
#options.binary_location = firefox_bin
