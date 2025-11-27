import json
from time import sleep

from selenium.webdriver.common.by import By


class Shopping:
    def __init__(self, driver):
        self.driver = driver
        self.phone_list = (By.XPATH, "//h4[@class='card-title']")
        self.phone_checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def shopping(self):
        phone_names = self.driver.find_elements(*self.phone_list)

        temp = [name.text for name in phone_names]
        path = "C:\\Users\\eavilov\\PycharmProjects\\PythonTesting\\DataSource\\data.json"
        with open(path, "r") as f:
            json_data = json.load(f)

        for i in temp:
            if i == json_data["model"]:
                # phone adding
                self.driver.find_element(By.XPATH, f"//a[text()='{i}']/../../following-sibling::div/button").click()
                # clicking checkout
                self.driver.find_element(*self.phone_checkout).click()
                sleep(1)
