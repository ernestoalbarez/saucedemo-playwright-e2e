from playwright.sync_api import Locator, Page, expect

from locators.example_locators import ExampleLocators
from pages.base_page import BasePage


class ExamplePage(BasePage):
    URL = "https://example.com"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def heading(self) -> Locator:
        return self.locator(ExampleLocators.HEADING)

    def open(self) -> None:
        self.navigate(self.URL)

    def expect_heading(self, text: str) -> None:
        expect(self.heading).to_have_text(text)
