import re

import allure
from playwright.sync_api import Page

from elements.text import Text
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    PageObject для страницы inventory (Products) после успешного логина.
    """

    INVENTORY_URL_PATTERN = re.compile(r".*/inventory\.html(\?.*)?$")

    def __init__(self, page: Page):
        super().__init__(page)

        self.inventory_title = Text(page, 'title', 'Title')

    def check_visible_inventory_title(self, timeout_ms: int = 10000) -> None:
        """
        Проверяет, что заголовок 'Products' (title) виден.
        """
        with allure.step("Check inventory title is visible"):
            self.inventory_title.check_visible(timeout=timeout_ms)
            self.inventory_title.check_have_text("Products", timeout=timeout_ms)

    def check_inventory_url(self, timeout_ms: int = 10000) -> None:
        """
        Проверяет, что мы на странице inventory.
        """
        with allure.step("Check inventory URL"):
            self.check_current_url(self.INVENTORY_URL_PATTERN, timeout_ms=timeout_ms)
