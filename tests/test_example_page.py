from playwright.sync_api import Page

from pages.example_page import ExamplePage


def test_example_page_loads(page: Page) -> None:
    example = ExamplePage(page)

    example.open()
    example.expect_title("Example Domain")
    example.expect_heading("Example Domain")
