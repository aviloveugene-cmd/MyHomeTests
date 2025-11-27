#from time import sleep

import pytest
#from selenium.webdriver.common.by import By

from PageObjects.shopping import Shopping


@pytest.mark.usefixtures("browser")
class TestClass:

    def test_shopping(self, browser):
        my_shopping = Shopping(browser)
        my_shopping.shopping()

"""
        phone_names = browser.find_elements(By.XPATH, "//h4[@class='card-title']")

        temp = [name.text for name in phone_names]

        for i in temp:
            if i == 'iphone X':
                browser.find_element(By.XPATH, f"//a[text()='{i}']/../../following-sibling::div/button").click()
                browser.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
"""

        #sleep(2)


