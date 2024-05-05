from account import *
from urls import URL_PROFILE


class TestLogin:
    @staticmethod
    def test_login_registration_form(driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_registration_form(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE in driver.current_url, "Failed: login after registration"

    @staticmethod
    def test_login_main_page(driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_main_page(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE in driver.current_url, "Failed: login from the main page"

    @staticmethod
    def test_login_personal_space(driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_personal_space(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE in driver.current_url, "Failed: login from the personal space"

    @staticmethod
    def test_login_recover_password(driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_recover_password(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE in driver.current_url, "Failed: login from the password recovery section"
