import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser():
    print("Hello browser")
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    print("Goodbye browser")
    driver.quit()
