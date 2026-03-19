from playwright.sync_api import Page

from flows.login_flow import LoginFlow
from pages.inventory_page import InventoryPage


def test_login_success(page: Page, login_flow: LoginFlow) -> None:
    """Verifies a successful user login utilizing the Flow Layer."""
    inventory_page = InventoryPage(page)

    login_flow.login_as_standard_user("standard_user", "secret_sauce")
    inventory_page.is_at()


def test_login_invalid_credentials(page: Page, login_flow: LoginFlow) -> None:
    """Verifies that attempting login with invalid credentials displays the appropriate error."""
    login_flow.login_as_standard_user("locked_out_user", "secret_sauce")
    error_msg = login_flow.login_page.get_error_message()
    assert "Epic sadface" in error_msg
