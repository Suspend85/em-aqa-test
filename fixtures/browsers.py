import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config import settings
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright: Playwright) -> None:
    """
    Глобально меняет атрибут для page.get_by_test_id()
    со стандартного data-testid на data-test.
    """
    playwright.selectors.set_test_id_attribute('data-test')


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )

# @pytest.fixture
# def chromium_page(playwright: Playwright) -> Page:
#     browser = playwright.chromium.launch(headless=False)
#     yield browser.new_page()
#     browser.close()
