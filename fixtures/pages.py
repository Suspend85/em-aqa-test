import pytest
from playwright.sync_api import Page

from pages.authentication.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)

@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page=page)
