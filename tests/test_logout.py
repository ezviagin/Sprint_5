from account import *
from urls import URL_BASE, URL_LOGIN


class TestLogout:
    @staticmethod
    def test_logout_from_personal_space(driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_registration_form(credentials)

        account.logout()

        assert f"{URL_BASE}{URL_LOGIN}" == driver.current_url, "Failed: logout"
