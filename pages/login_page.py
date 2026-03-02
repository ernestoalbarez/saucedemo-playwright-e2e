from playwright.sync_api import Page

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.navigate(self.URL)

    def login(self, username: str, password: str) -> None:
        self.page.fill(LoginLocators.USERNAME, username)
        self.page.fill(LoginLocators.PASSWORD, password)
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.page.locator(LoginLocators.ERROR_MESSAGE).inner_text()
