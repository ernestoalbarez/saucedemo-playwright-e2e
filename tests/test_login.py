from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_success(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.is_at()


def test_login_invalid_credentials(page: Page) -> None:
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    error_msg = login_page.get_error_message()
    assert "Epic sadface" in error_msg
