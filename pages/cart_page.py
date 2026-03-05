from typing import List
from playwright.sync_api import Page

from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.click(CartLocators.CART_LINK)

    def get_items(self) -> List[str]:
        items = self.page.locator(CartLocators.CART_ITEM_NAME)
        return items.all_inner_texts()

    def get_items_count(self) -> int:
        return self.page.locator(CartLocators.CART_ITEMS).count()
