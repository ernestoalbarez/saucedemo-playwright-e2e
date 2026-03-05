import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.cart
def test_add_product_updates_cart(page: Page) -> None:
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.is_at()

    inventory.add_to_cart("sauce-labs-backpack")

    badge = page.locator(".shopping_cart_badge").inner_text()
    assert badge == "1"

    cart.open()

    items = cart.get_items()
    assert "Sauce Labs Backpack" in items


@pytest.mark.cart
def test_remove_product_from_cart(page: Page) -> None:
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.is_at()

    inventory.add_to_cart("sauce-labs-backpack")
    inventory.remove_from_cart("sauce-labs-backpack")

    badge = page.locator(".shopping_cart_badge")
    assert badge.count() == 0


@pytest.mark.cart
def test_cart_content_validation(page: Page) -> None:
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")

    cart.open()

    items = cart.get_items()

    assert "Sauce Labs Backpack" in items
    assert "Sauce Labs Bike Light" in items
    assert len(items) == 2
