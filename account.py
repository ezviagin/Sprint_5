from selenium import webdriver as WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators import StellarBurgerLocators as locate
from urls import URL_BASE, URL_ACCOUNT
from helpers import get_email, get_password, ATTRIBUTE_WAIT_TIMEOUT


class Credentials:
    def __init__(self, email="ezviagin_test@oulook.com", password="Test123!"):
        self.name = email
        self.email = email
        self.password = password


class Account:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = URL_BASE

    def __goto_main_page(self) -> None:
        self.driver.get(self.base_url)

    def click_on_personal_space_button(self) -> None:
        self.driver.find_element(*locate.Account.PERSONAL_SPACE_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(
            ec.visibility_of_element_located(locate.Account.PROFILE_TITLE))

    def __fill_credentials(self, credentials: Credentials) -> None:
        email_field = self.driver.find_element(*locate.Login.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(credentials.email)
        #WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
       #     locate.Login.get_email_field_value(credentials.email)))

        password_field = self.driver.find_element(*locate.Login.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(credentials.password)
        #WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
        #    locate.Login.get_password_field_value(credentials.password)))

    def register(self, email=get_email(), password=get_password()) -> Credentials:
        self.driver.find_element(*locate.Login.LOGIN_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Login.LOGIN_TITLE))

        self.driver.find_element(*locate.Login.REGISTER_LINK).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Login.REGISTRATION_TITLE))

        self.driver.find_element(*locate.Login.USERNAME_FIELD).send_keys(email)
        self.driver.find_element(*locate.Login.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*locate.Login.PASSWORD_FIELD).send_keys(password)

        self.driver.find_element(*locate.Login.REGISTER_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Login.LOGIN_BUTTON))

        return Credentials(email, password)

    def login_registration_form(self, credentials: Credentials):
        self.__goto_main_page()
        self.driver.find_element(*locate.Login.LOGIN_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Login.LOGIN_TITLE))

        self.__fill_credentials(credentials)
        self.driver.find_element(*locate.Login.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Account.CREATE_ORDER_BUTTON))

    def login_main_page(self, credentials: Credentials):
        self.__goto_main_page()
        self.driver.find_element(*locate.Login.LOGIN_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Login.LOGIN_TITLE))

        self.__fill_credentials(credentials)
        self.driver.find_element(*locate.Login.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Account.CREATE_ORDER_BUTTON))

    def login_personal_space(self, credentials: Credentials):
        self.__goto_main_page()
        link = WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.element_to_be_clickable(
            locate.Account.PERSONAL_SPACE_BUTTON))
        self.driver.get(link.get_attribute("href"))

        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Login.LOGIN_TITLE))

        self.__fill_credentials(credentials)

        self.driver.find_element(*locate.Login.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Account.CREATE_ORDER_BUTTON))

    def login_recover_password(self, credentials: Credentials):
        self.__goto_main_page()

        self.driver.find_element(*locate.Login.LOGIN_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Login.LOGIN_TITLE))

        self.driver.find_element(*locate.Login.RECOVER_PASSWORD_LINK).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Account.PASSWORD_RECOVERY_TITLE))

        self.driver.find_element(*locate.Login.LOGIN_LINK).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Login.LOGIN_TITLE))

        self.__fill_credentials(credentials)

        self.driver.find_element(*locate.Login.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Account.CREATE_ORDER_BUTTON))

    def logout(self):
        self.driver.get(f"{URL_ACCOUNT}")
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.presence_of_element_located(
            locate.Account.PROFILE_TITLE))

        self.driver.find_element(*locate.Account.LOGOUT_BUTTON).click()
        WebDriverWait(self.driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.presence_of_element_located(
            locate.Login.LOGIN_TITLE))
