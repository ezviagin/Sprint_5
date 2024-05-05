from account import *
from urls import URL_BASE, URL_PROFILE, URL_REGISTER


class TestRegistration:
    @staticmethod
    def test_registration_success(driver: WebDriver, account: Account) -> None:
        credentials = account.register()
        account.login_registration_form(credentials)

        account.click_on_personal_space_button()

        assert URL_PROFILE in driver.current_url, "Failed: successful registration"

    @staticmethod
    def test_registration_with_short_password_failed(driver: WebDriver, account: Account) -> None:
        # Registration and Login with a "Short" password (less than 6 chars)
        account.register(password="Short")
        WebDriverWait(driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.presence_of_element_located(
            locate.Login.WRONG_PASSWORD_ERROR))

        assert driver.current_url == f"{URL_BASE}{URL_REGISTER}", \
            "Failed: registratiion is not allowed with a password less than 6 symbols"
