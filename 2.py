from selenium import webdriver

driver = webdriver.Chrome()  # or webdriver.Firefox()
driver.get("http://example.com")
driver.quit()
