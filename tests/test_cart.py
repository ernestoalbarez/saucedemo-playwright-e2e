import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


@pytest.mark.cart
def test_add_product_to_cart(
    logged_in_inventory: InventoryPage,
    cart_page: CartPage,
) -> None:
    logged_in_inventory.add_to_cart("sauce-labs-backpack")

    cart_page.open()

    items = cart_page.get_items()

    assert "Sauce Labs Backpack" in items


@pytest.mark.cart
def test_remove_product_from_cart(
    logged_in_inventory: InventoryPage,
) -> None:
    logged_in_inventory.add_to_cart("sauce-labs-backpack")
    logged_in_inventory.remove_from_cart("sauce-labs-backpack")


@pytest.mark.cart
def test_cart_content_validation(
    logged_in_inventory: InventoryPage,
    cart_page: CartPage,
) -> None:
    logged_in_inventory.add_to_cart("sauce-labs-backpack")
    logged_in_inventory.add_to_cart("sauce-labs-bike-light")

    cart_page.open()

    items = cart_page.get_items()

    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Bike Light" in items
    assert len(items) == 2
