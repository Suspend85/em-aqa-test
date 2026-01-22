import allure
from playwright.sync_api import Locator, Page, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self):
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid={locator}" at index "{nth}"'
        with allure.step(step):
            return self.page.get_by_test_id(locator).nth(nth)

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f"//*[@data-test='{self.locator}'][{nth + 1}]"

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}" '
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)
