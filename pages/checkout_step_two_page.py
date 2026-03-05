from playwright.sync_api import Page, expect

from locators.checkout_locators import CheckoutStepTwoLocators
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def is_at(self) -> None:
        expect(self.page.locator(CheckoutStepTwoLocators.SUMMARY_CONTAINER)).to_be_visible()

    def get_items(self) -> list[str]:
        items = self.page.locator(CheckoutStepTwoLocators.ITEM_NAMES)
        return items.all_inner_texts()

    def finish_checkout(self) -> None:
        self.page.click(CheckoutStepTwoLocators.FINISH_BUTTON)
