from typing import cast

from playwright.sync_api import Browser, BrowserContext, Playwright

from config import settings


def launch_browser(playwright: Playwright) -> Browser:
    browser_type = getattr(playwright, settings.browser)

    return cast(
        Browser,
        browser_type.launch(
            headless=settings.headless,
            slow_mo=settings.slow_mo,
        ),
    )


def new_context(browser: Browser) -> BrowserContext:
    return browser.new_context(
        base_url=settings.base_url,
        viewport=settings.viewport,
    )
