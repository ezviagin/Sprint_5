from account import *
from urls import URL_PROFILE


class TestLogin:
    def test_login_registration_form(self, driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_registration_form(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE == driver.current_url, "Failed: login after registration"

    def test_login_main_page(self, driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_main_page(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE == driver.current_url, "Failed: login from the main page"

    def test_login_personal_space(self, driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_personal_space(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE == driver.current_url, "Failed: login from the personal space"

    def test_login_recover_password(self, driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_recover_password(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE == driver.current_url, "Failed: login from the password recovery section"
