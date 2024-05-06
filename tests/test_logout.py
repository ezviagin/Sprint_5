from account import *
from urls import URL_LOGIN


class TestLogout:
    def test_logout_from_personal_space(self, driver: WebDriver, account: Account) -> None:
        credentials = Credentials()
        account.login_registration_form(credentials)

        account.logout()

        assert f"{URL_LOGIN}" == driver.current_url, "Failed: logout"
