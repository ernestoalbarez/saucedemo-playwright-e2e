from playwright.sync_api import Page, expect

from locators.cart_locators import CartLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.click(CartLocators.CART_LINK)

    def is_at(self) -> None:
        expect(self.page.locator(CartLocators.CART_CONTAINER)).to_be_visible()

    def get_items(self) -> list[str]:
        items = self.page.locator(CartLocators.CART_ITEM_NAME)
        return items.all_inner_texts()

    def get_items_count(self) -> int:
        return self.page.locator(CartLocators.CART_ITEM).count()

    def remove_item(self, product_slug: str) -> None:
        self.page.click(f"[data-test='remove-{product_slug}']")

    def checkout(self) -> None:
        self.page.click(CartLocators.CHECKOUT_BUTTON)

    def get_cart_items(self) -> list[str]:
        items = self.page.locator(CartLocators.CART_ITEM_NAME)
        return items.all_inner_texts()
