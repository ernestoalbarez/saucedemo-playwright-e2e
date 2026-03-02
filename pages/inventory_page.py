from playwright.sync_api import Page, expect
from locators.inventory_locators import InventoryLocators
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def is_at(self) -> None:
        expect(self.page.locator(InventoryLocators.INVENTORY_CONTAINER)).to_be_visible()
        expect(self.page.locator(InventoryLocators.HEADER_LABEL)).to_have_text("Products")
