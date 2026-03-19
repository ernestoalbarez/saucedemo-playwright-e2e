from playwright.sync_api import Page

from pages.example_page import ExamplePage


def test_example_page_loads(page: Page) -> None:
    """Verifies that the example page loads correctly and asserts the page title."""
    example = ExamplePage(page)

    example.open()
    example.expect_title("Swag Labs")
