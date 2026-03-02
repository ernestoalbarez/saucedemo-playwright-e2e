from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_success(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 1. Navigate to login page
    login_page.open()

    # 2. Login with standard_user
    login_page.login("standard_user", "secret_sauce")

    # 3. Verify successful login
    inventory_page.is_at()
