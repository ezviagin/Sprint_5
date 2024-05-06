from account import *
from urls import URL_BASE, URL_PROFILE


class TestAccount:
    def test_go_to_personal_space(self, driver: WebDriver, account: Account):
        credentials = Credentials()
        account.login_main_page(credentials)
        account.click_on_personal_space_button()

        assert f"{URL_PROFILE}" == driver.current_url, "Failed: couldn't go to the personal space"

    def test_click_on_constructor_from_personal_space(self, driver: WebDriver, account: Account):
        credentials = Credentials()
        account.login_main_page(credentials)

        account.click_on_personal_space_button()

        driver.find_element(*locate.Constructor.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Account.ASSEMBLE_BURGER_TITLE))

        assert "Оформить заказ" == WebDriverWait(driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Account.CREATE_ORDER_BUTTON)).text, "Failed: couldn't go to the Constructor"

    def test_click_on_logo_from_personal_space(self, driver: WebDriver, account: Account):
        credentials = Credentials()
        account.login_main_page(credentials)

        account.click_on_personal_space_button()

        driver.find_element(*locate.Account.STELLAR_BURGER_LOGO).click()
        WebDriverWait(driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Account.ASSEMBLE_BURGER_TITLE))

        assert URL_BASE == driver.current_url
