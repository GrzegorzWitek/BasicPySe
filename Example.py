from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Arrange
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("http://skleptest.pl/")

# Act
driver.find_element(By.CSS_SELECTOR, "a[title='Contact']").click()

elem = driver.find_element(By.CSS_SELECTOR, "[name='your-message']")
elem.send_keys("Test")

# Assert
assert elem.is_displayed(), "Ten element jest niewyswietlony"

# Cleanup
time.sleep(5)
driver.quit()
