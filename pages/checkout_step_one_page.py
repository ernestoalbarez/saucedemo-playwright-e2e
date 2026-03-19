from playwright.sync_api import Page, expect

from locators.checkout_locators import CheckoutStepOneLocators
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    """Page object for the first checkout step containing shipping information."""
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def is_at(self) -> None:
        expect(self.page.locator(CheckoutStepOneLocators.FIRST_NAME)).to_be_visible()

    def fill_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.page.fill(CheckoutStepOneLocators.FIRST_NAME, first_name)
        self.page.fill(CheckoutStepOneLocators.LAST_NAME, last_name)
        self.page.fill(CheckoutStepOneLocators.POSTAL_CODE, postal_code)

    def continue_checkout(self) -> None:
        self.page.click(CheckoutStepOneLocators.CONTINUE_BUTTON)
