"""
Login flow encapsulating authentication-related business actions.
"""
from playwright.sync_api import Page

from pages.login_page import LoginPage


class LoginFlow:
    """
    Orchestrates the login process using Page Objects.
    """

    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)

    def login_as_standard_user(self, username: str, password: str) -> None:
        """
        Logs in a user with the provided credentials.
        
        Steps:
        - Navigate to the login page
        - Fill credentials
        - Submit form
        """
        self.login_page.open()
        self.login_page.login(username, password)
