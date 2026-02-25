"""
Global pytest configuration and fixtures.
"""

from collections.abc import Generator
from datetime import datetime
from pathlib import Path
from typing import Any

import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)

from config import settings
from utils.browser import launch_browser


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    """Starts a single Playwright instance for the entire test session."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    """Launches a single browser for the entire test session."""
    browser = launch_browser(playwright_instance)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Creates a fresh browser context per test for full isolation."""
    context = browser.new_context(
        base_url=settings.base_url,
        viewport=settings.viewport,
    )

    context.set_default_timeout(settings.timeout_ms)
    context.set_default_navigation_timeout(settings.navigation_timeout_ms)

    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
    """Provides a clean Page instance and handles failure reporting."""
    page = context.new_page()
    page.set_default_timeout(settings.timeout_ms)

    yield page

    # Screenshot on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        _take_screenshot(page, request.node.name)

    page.close()


def _take_screenshot(page: Page, test_name: str) -> None:
    """Captures a screenshot for failed tests."""
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = screenshots_dir / f"{test_name}_{timestamp}.png"
    page.screenshot(path=str(filepath), full_page=True)
    print(f"\nScreenshot saved to: {filepath}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: Any) -> Generator[None, Any, None]:
    """Hook to make test results available to fixtures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
