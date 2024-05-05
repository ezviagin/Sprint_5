import pytest

from selenium import webdriver
from selenium.webdriver import Chrome as WebDriver

from account import Account
from urls import URL_BASE


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL_BASE)
    yield driver
    driver.quit()


@pytest.fixture()
def account(driver: WebDriver) -> Account:
    return Account(driver)
