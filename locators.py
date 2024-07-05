from selenium.webdriver.common.by import By


class StellarBurgerLocators:
    class Login:
        # Headers
        LOGIN_TITLE = (By.XPATH, ".//h2[contains(text(), 'Вход')]")                                 # заголовок 2 "Вход"
        REGISTRATION_TITLE = (By.XPATH, ".//h2[contains(text(), 'Регистрация')]")                   # заголовок 2 "Регистрация"

        # Links
        LOGIN_LINK = (By.XPATH, ".//div/p/a[contains(text(), 'Войти')]")                            # href button "Войти"
        REGISTER_LINK = (By.XPATH, ".//div/p/a[contains(text(), 'Зарегистрироваться')]")            # href button "Зарегистрироваться"
        RECOVER_PASSWORD_LINK = (By.XPATH, ".//div/p/a[contains(text(), 'Восстановить пароль')]")   # href button "Восстановить пароль"

        # Buttons
        REGISTER_BUTTON = (By.XPATH, ".//button[contains(@class, 'button_button__33qZ0')]")         # кнопка "Зарегистрироваться"
        LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")    # кнопка "Войти в аккаунт"
        LOGIN_BUTTON = (By.XPATH, ".//div[@class='Auth_login__3hAey']/..//button")                  # кнопка "Войти"

        # Forms
        USERNAME_FIELD = (By.XPATH, ".//label[text()='Имя']/..//input")                             # поле "Имя"
        EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/..//input")                              # поле "Email"
        PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/..//input")                          # поле "Пароль"

        # Errors
        WRONG_PASSWORD_ERROR = (By.XPATH, ".//p[starts-with(@class,'input__error') and text()='Некорректный пароль']")  # идентификатор ошибки "Неверный пароль"

    class Account:
        # Logo
        STELLAR_BURGER_LOGO = (By.XPATH, ".//div[starts-with(@class, 'AppHeader_header__logo')]")   # кнопка Logo

        # Headers
        ASSEMBLE_BURGER_TITLE = (By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")            # заголовок 1 "Соберите бургер"
        PASSWORD_RECOVERY_TITLE = (By.XPATH, ".//h2[contains(text(), 'Восстановление пароля')]")    # заголовок 2 "Восстановление пароля"
        PROFILE_TITLE = (By.XPATH, ".//li[starts-with(@class, 'Account_list')]/a[1]")               # заголовок 2 "Профиль" в Личном Кабинете

        # Buttons
        CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")                       # кнопка "Оформить заказ"
        LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]")                          # кнопка "Выход"
        PERSONAL_SPACE_BUTTON = (By.LINK_TEXT, "Личный Кабинет")                                    # кнопка "Личный Кабинет"

    class Constructor:
        CONSTRUCTOR_BUTTON = (By.XPATH, ".//header/nav/ul/li[1]/a")                                                             # кнопка "Конструктор"
        CONTAINER_INGREDIENTS = (By.XPATH, ".//div[starts-with(@class,'BurgerIngredients_ingredients__menuContainer')]")        # контейнер "Ингридиенты"

        @staticmethod
        def get_div_selected_ingredients(ingredients: str):
            return By.XPATH, f".//div[contains(@class, 'current')]//span[text()='{ingredients}']"

        @staticmethod
        def get_span_ingredients(ingredients: str) -> tuple[str, str]:
            return By.XPATH, f".//span[text()='{ingredients}']"

        @staticmethod
        def get_title_ingredients(ingredients: str) -> tuple[str, str]:
            return By.XPATH, f".//h2[text()='{ingredients}']"
