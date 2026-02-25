from playwright.sync_api import Locator, Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, url: str) -> None:
        """Navigates to the given URL and waits for the load state."""
        self.page.goto(url)
        self.wait_for_load_state()

    def wait_for_load_state(self, state: str = "load") -> None:
        """Waits for the specified load state (load, domcontentloaded, networkidle)."""
        self.page.wait_for_load_state(state)  # type: ignore

    def expect_title(self, title: str) -> None:
        """Asserts that the page title matches the expected string."""
        expect(self.page).to_have_title(title)

    def locator(self, selector: str) -> Locator:
        """Returns a Playwright Locator for the given selector."""
        return self.page.locator(selector)
