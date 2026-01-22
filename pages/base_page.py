from typing import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    """
    Базовая страница для POM.

    Содержит методы:
    - навигацию (visit)
    - ожидания URL
    """

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str, wait_until: str = 'domcontentloaded', timeout_ms: int = 30000) -> None:
        step = f'Opening the url "{url}"'
        with allure.step(step):
            self.page.goto(url, wait_until=wait_until, timeout=timeout_ms)

    def check_current_url(self, expected_url: Pattern[str], timeout_ms: int = 30000) -> None:
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            expect(self.page).to_have_url(expected_url, timeout=timeout_ms)
