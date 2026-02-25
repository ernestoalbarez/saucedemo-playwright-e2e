from playwright.sync_api import Page


def test_smoke_page_load(page: Page) -> None:
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
