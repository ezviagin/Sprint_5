from account import *
from urls import URL_PROFILE, URL_REGISTER


class TestRegistration:
    def test_registration_success(self, driver: WebDriver, account: Account) -> None:
        credentials = account.register()
        account.login_registration_form(credentials)
        account.click_on_personal_space_button()

        assert URL_PROFILE == driver.current_url, "Failed: successful registration"

    def test_registration_with_short_password_failed(self, driver: WebDriver, account: Account) -> None:
        account.register(password="Short")
        WebDriverWait(driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.presence_of_element_located(
            locate.Login.WRONG_PASSWORD_ERROR))

        assert driver.current_url == f"{URL_REGISTER}", \
            "Failed: registration is not allowed with a password less than 6 symbols"
