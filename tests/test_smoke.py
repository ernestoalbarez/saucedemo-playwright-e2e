import pytest
from playwright.sync_api import Page


@pytest.mark.smoke
def test_smoke_page_load(page: Page) -> None:
    page.goto("/")
    assert page.title() == "Swag Labs"
