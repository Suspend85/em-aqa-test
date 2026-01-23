import allure
import pytest
from allure_commons.types import Severity

import config
from pages.authentication.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
class TestAuthorization:
    @allure.title('User login with correct credentials')
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.parametrize('username, password', [('standard_user', 'secret_sauce')])
    def test_successful_authorization(
            self,
            username: str, password: str,
            login_page: LoginPage,
            inventory_page: InventoryPage
    ):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username=username, password=password)
        inventory_page.check_visible_inventory_title()
        inventory_page.check_inventory_url()

    @allure.title('User login with wrong credentials')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize('username, password', [('standard_user', 'wrong_password')])
    def test_wrong_username_or_password_authorization(self, username: str, password: str, login_page: LoginPage):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username=username, password=password)
        login_page.check_visible_login_error(LoginPage.ERROR_INVALID_CREDENTIALS)

    @allure.title('User login with locked out user credentials')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize('username, password', [('locked_out_user', 'secret_sauce')])
    def test_locked_out_user_authorization(self, username: str, password: str, login_page: LoginPage):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username=username, password=password)
        login_page.check_visible_login_error(LoginPage.ERROR_LOCKED_OUT)

    @allure.title('User login with empty credentials')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize('username, password', [('', '')])
    def test_empty_username_and_password_authorization(self, username: str, password: str, login_page: LoginPage):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username=username, password=password)
        login_page.check_visible_login_error(LoginPage.ERROR_USERNAME_REQUIRED)

    @allure.title('User login with performance_glitch_user credentials')
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.performance
    @pytest.mark.parametrize('username, password', [('performance_glitch_user', 'secret_sauce')])
    def test_performance_glitch_user_authorization(
            self,
            username: str, password: str,
            login_page: LoginPage,
            inventory_page: InventoryPage
    ):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username=username, password=password)
        inventory_page.check_visible_inventory_title(timeout_ms=15000)
        inventory_page.check_inventory_url(timeout_ms=15000)
