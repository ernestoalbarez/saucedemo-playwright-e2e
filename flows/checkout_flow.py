"""
Checkout flow encapsulating the entire checkout journey.
"""
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.inventory_page import InventoryPage


class CheckoutFlow:
    """
    Orchestrates the checkout process from adding items to completion.
    """

    def __init__(self, page: Page):
        self.page = page
        self.inventory = InventoryPage(page)
        self.cart = CartPage(page)
        self.step_one = CheckoutStepOnePage(page)
        self.step_two = CheckoutStepTwoPage(page)
        self.complete = CheckoutCompletePage(page)

    def complete_checkout(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Completes the checkout process.
        
        Steps:
        - Proceed to checkout from cart
        - Fill shipping information and continue
        - Finish the checkout on the overview page
        """
        self.cart.checkout()
        self.step_one.is_at()
        self.step_one.fill_information(first_name, last_name, zip_code)
        self.step_one.continue_checkout()
        self.step_two.is_at()
        self.step_two.finish_checkout()
        self.complete.is_at()
