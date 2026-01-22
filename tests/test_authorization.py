import config
import pytest

from pages.authentication.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    def test_successful_authorization(self, login_page: LoginPage, inventory_page: InventoryPage):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username='standard_user', password='secret_sauce')
        inventory_page.check_visible_inventory_title()
        inventory_page.check_inventory_url()

    def test_wrong_username_or_password_authorization(self, login_page: LoginPage):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username='standard_user', password='wrong_password')
        login_page.check_visible_login_error(LoginPage.ERROR_INVALID_CREDENTIALS)

    def test_locked_out_user_authorization(self, login_page: LoginPage):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username='locked_out_user', password='secret_sauce')
        login_page.check_visible_login_error(LoginPage.ERROR_LOCKED_OUT)

    def test_empty_username_and_password_authorization(self, login_page: LoginPage):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username='', password='')
        login_page.check_visible_login_error(LoginPage.ERROR_USERNAME_REQUIRED)

    @pytest.mark.performance
    def test_performance_glitch_user_authorization(self, login_page: LoginPage, inventory_page: InventoryPage):
        login_page.visit(config.settings.get_base_url())
        login_page.login(username='performance_glitch_user', password='secret_sauce')
        inventory_page.check_visible_inventory_title(timeout_ms=15000)
        inventory_page.check_inventory_url(timeout_ms=15000)

