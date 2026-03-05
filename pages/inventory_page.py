from playwright.sync_api import Page, expect

from locators.inventory_locators import InventoryLocators
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def is_at(self) -> None:
        container = self.page.locator(InventoryLocators.INVENTORY_CONTAINER)
        header = self.page.locator(InventoryLocators.HEADER_LABEL)

        expect(container).to_be_visible()
        expect(header).to_have_text("Products")

    def get_products(self) -> list[str]:
        items = self.page.locator(InventoryLocators.INVENTORY_ITEM_NAME)
        return items.all_inner_texts()

    def add_to_cart(self, product_slug: str) -> None:
        self.page.click(f"[data-test='add-to-cart-{product_slug}']")

    def remove_from_cart(self, product_slug: str) -> None:
        self.page.click(f"[data-test='remove-{product_slug}']")

    def sort_by(self, option_value: str) -> None:
        self.page.select_option(
            InventoryLocators.SORT_DROPDOWN,
            value=option_value,
        )

    def open_cart(self) -> None:
        self.page.click(InventoryLocators.CART_LINK)

    def get_cart_badge_count(self) -> int:
        badge = self.page.locator(InventoryLocators.CART_BADGE)
        if badge.is_visible():
            return int(badge.inner_text())
        return 0
