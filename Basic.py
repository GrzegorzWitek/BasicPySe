from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("http://skleptest.pl/")
driver.quit()
