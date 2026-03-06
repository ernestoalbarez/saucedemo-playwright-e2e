import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.checkout
def test_checkout_end_to_end_flow(page: Page) -> None:

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    step_one = CheckoutStepOnePage(page)
    step_two = CheckoutStepTwoPage(page)
    complete = CheckoutCompletePage(page)

    # Login
    login.open()
    login.login("standard_user", "secret_sauce")

    # Add product
    inventory.is_at()
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.open_cart()

    # Cart validation
    cart.is_at()
    items = cart.get_cart_items()
    assert "Sauce Labs Backpack" in items

    cart.checkout()

    # Checkout step one
    step_one.is_at()
    step_one.fill_information("John", "Doe", "10001")
    step_one.continue_checkout()

    # Checkout step two
    step_two.is_at()

    items = step_two.get_items()
    assert "Sauce Labs Backpack" in items

    # Validate total calculation
    item_total = step_two.get_item_total()
    tax = step_two.get_tax()
    total = step_two.get_total()

    assert total == item_total + tax

    step_two.finish_checkout()

    # Complete page
    complete.is_at()

    title = complete.get_title()
    assert "Thank you for your order!" in title
