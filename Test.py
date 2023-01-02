import time
import unittest
from selenium import webdriver
import chromedriver_autoinstaller

from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://skleptest.pl/")

    def test_example_positive(self):
        elem = self.driver.find_element(By.CSS_SELECTOR, "a[title='Contact']")
        elem.click()

        name = self.driver.find_element(By.CSS_SELECTOR, "input[name='your-name']")
        name.send_keys("TEST")
        mail = self.driver.find_element(By.CSS_SELECTOR, "input[name='your-email']")
        mail.send_keys("TEST@maillll.com")
        send = self.driver.find_element(By.CSS_SELECTOR, "input[value='Send']")
        send.click()
        time.sleep(2)
        assert len(self.driver.find_elements(By.CSS_SELECTOR, ".wpcf7-mail-sent-ok")) > 0, \
            "There is no Success message box element"

    def test_example_negative_wrong_mail(self):
        elem = self.driver.find_element(By.CSS_SELECTOR, "a[title='Contact']")
        elem.click()

        name = self.driver.find_element(By.CSS_SELECTOR, "input[name='your-name']")
        name.send_keys("TEST1")
        mail = self.driver.find_element(By.CSS_SELECTOR, "input[name='your-email']")
        mail.send_keys("TEST2")
        send = self.driver.find_element(By.CSS_SELECTOR, "input[value='Send']")
        send.click()
        time.sleep(2)
        assert len(self.driver.find_elements(By.CSS_SELECTOR, ".wpcf7-mail-sent-ok")) == 0, \
            "There is displayed 'success' message but should not"

    def test_example_negative_no_field(self):
        elem = self.driver.find_element(By.CSS_SELECTOR, "a[title='Contact']")
        elem.click()

        send = self.driver.find_element(By.CSS_SELECTOR, "input[value='Send']")
        send.click()
        time.sleep(2)

        alert = self.driver.find_element(By.CSS_SELECTOR, "span.your-name>span")
        assert alert.is_displayed(), "Alert 'required field' is not displayed"
        assert alert.text in "The field is required.", "Wrong text in alert"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()