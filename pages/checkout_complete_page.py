from playwright.sync_api import Page

from locators.checkout_locators import CheckoutCompleteLocators
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Page object for the final Checkout Complete page, verifying order success."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def is_at(self) -> None:
        self.page.locator(CheckoutCompleteLocators.COMPLETE_CONTAINER).wait_for()

    def get_header(self) -> str:
        return self.page.locator(CheckoutCompleteLocators.COMPLETE_HEADER).inner_text()

    def get_confirmation_message(self) -> str:
        return self.page.locator(CheckoutCompleteLocators.COMPLETE_TEXT).inner_text()

    def get_title(self) -> str:
        return self.page.locator(CheckoutCompleteLocators.TITLE).inner_text()

    def get_message(self) -> str:
        return self.page.locator(CheckoutCompleteLocators.MESSAGE).inner_text()
