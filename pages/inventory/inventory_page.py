import re
import allure
from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    PageObject для страницы inventory (Products) после успешного логина.
    """

    INVENTORY_URL_PATTERN = re.compile(r".*/inventory\.html(\?.*)?$")

    def __init__(self, page: Page):
        super().__init__(page)

        self.inventory_title: Locator = page.get_by_test_id("title")
        self.inventory_items: Locator = page.locator(".inventory_item")

    def check_visible_inventory_title(self, timeout_ms: int = 10000) -> None:
        """
        Проверяет, что заголовок 'Products' (title) виден.
        """
        with allure.step("Check inventory title is visible"):
            expect(self.inventory_title).to_be_visible(timeout=timeout_ms)
            expect(self.inventory_title).to_have_text("Products", timeout=timeout_ms)

    def check_inventory_url(self, timeout_ms: int = 10000) -> None:
        """
        Проверяет, что мы на странице inventory.
        """
        with allure.step("Check inventory URL"):
            self.check_current_url(self.INVENTORY_URL_PATTERN, timeout_ms=timeout_ms)
