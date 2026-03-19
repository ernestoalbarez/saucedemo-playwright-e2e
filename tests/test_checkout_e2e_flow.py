import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.inventory_page import InventoryPage
from flows.checkout_flow import CheckoutFlow


@pytest.mark.checkout
def test_checkout_end_to_end_flow(
    logged_in_inventory: InventoryPage,
    cart_page: CartPage,
    page: Page,
    checkout_flow: CheckoutFlow,
) -> None:
    """Verifies the complete checkout process end-to-end utilizing the Flow Layer."""

    inventory = logged_in_inventory
    complete = CheckoutCompletePage(page)

    # Add product
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.open_cart()

    # Cart validation (still asserting state here before handing to the flow)
    cart_page.is_at()
    items = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" in items

    # Run remaining workflow via the business flow layer
    checkout_flow.complete_checkout("John", "Doe", "10001")

    # Final complete page validations
    title = complete.get_title()
    assert "Thank you for your order!" in title
