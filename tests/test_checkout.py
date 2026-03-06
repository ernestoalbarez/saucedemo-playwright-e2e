import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.checkout
def test_successful_checkout(
    logged_in_inventory: InventoryPage,
    cart_page: CartPage,
    page
) -> None:

    inventory = logged_in_inventory

    step_one = CheckoutStepOnePage(page)
    step_two = CheckoutStepTwoPage(page)
    complete = CheckoutCompletePage(page)

    inventory.add_to_cart("sauce-labs-backpack")
    inventory.open_cart()

    cart_page.checkout()

    step_one.fill_information("John", "Doe", "10001")
    step_one.continue_checkout()

    items = step_two.get_items()
    assert "Sauce Labs Backpack" in items

    step_two.finish_checkout()

    message = complete.get_confirmation_message()

    assert "Your order has been dispatched" in message
