import allure
from playwright.sync_api import Page

from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    PageObject для страницы логина saucedemo.

    Содержит:
    - локаторы полей и кнопки
    - действия: заполнить форму, кликнуть логин, выполнить логин целиком
    - проверки: отображение/текст ошибки
    """

    ERROR_INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
    ERROR_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    ERROR_USERNAME_REQUIRED = "Epic sadface: Username is required"
    ERROR_PASSWORD_REQUIRED = "Epic sadface: Password is required"

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = Input(page, 'username', 'Username')
        self.password_input = Input(page, 'password', 'Password')
        self.login_button = Button(page, 'login-button', 'Login button')
        self.error_element = Text(page, 'error', 'Error')

    def fill_login_form(self, username: str, password: str):
        self.username_input.check_visible()
        self.username_input.fill(username)
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def click_login_button(self):
        self.login_button.check_visible()
        self.login_button.check_enabled()
        self.login_button.click()

    def login(self, username: str, password: str) -> None:
        """
        Бизнес-метод: выполнить логин (заполнить + submit).
        Инкапсулирует детали UI-реализации.
        """
        with allure.step(f'Login as "{username}", with password: "{password}"'):
            self.fill_login_form(username=username, password=password)
            self.click_login_button()

    @allure.step("Check visible login error")
    def check_visible_login_error(self, expected_text: str, timeout_ms: int = 5000) -> None:
        """
        Проверяет, что виден соответствующий текст ошибки
        """
        self.error_element.check_visible(timeout_ms=timeout_ms)
        self.error_element.check_have_text(expected_text, timeout_ms=timeout_ms)
