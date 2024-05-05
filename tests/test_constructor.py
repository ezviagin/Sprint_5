from account import *
import pytest


class TestConstructor:
    @staticmethod
    @pytest.mark.parametrize('ingredients', ['Булки', 'Соусы', 'Начинки'])
    def test_go_to_ingredients(driver: WebDriver, account: Account, ingredients: str):
        driver.find_element(*locate.Constructor.CONSTRUCTOR_BUTTON).click()

        ingredient = driver.find_elements(
            *locate.Constructor.get_div_selected_ingredients(ingredients))

        if len(ingredient) == 0:
            driver.find_element(*locate.Constructor.get_span_ingredients(ingredients)).click()

        ingredients_visible = WebDriverWait(driver, ATTRIBUTE_WAIT_TIMEOUT).until(ec.visibility_of_element_located(
            locate.Constructor.get_title_ingredients(ingredients)))

        assert ingredients_visible, f"Selected ingredient group {ingredients} is not visible"
