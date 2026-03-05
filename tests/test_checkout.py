import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.checkout
def test_successful_checkout(page: Page) -> None:

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    step_one = CheckoutStepOnePage(page)
    step_two = CheckoutStepTwoPage(page)
    complete = CheckoutCompletePage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_to_cart("sauce-labs-backpack")
    inventory.open_cart()

    cart.checkout()

    step_one.is_at()
    step_one.fill_information("John", "Doe", "10001")
    step_one.continue_checkout()

    step_two.is_at()
    items = step_two.get_items()
    assert "Sauce Labs Backpack" in items

    step_two.finish_checkout()

    complete.is_at()
    message = complete.get_confirmation_message()

    assert "Your order has been dispatched" in message
