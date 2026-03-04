import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.mark.auth
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (
            "standard_user",
            "invalid_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "",
            "secret_sauce",
            "Epic sadface: Username is required",
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        )
    ],
    ids=["invalid_credentials", "empty_username", "locked_user"],
)
def test_login_negative_scenarios(
    page: Page,
    username: str,
    password: str,
    expected_error: str,
) -> None:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    error_msg = login_page.get_error_message()
    assert error_msg.strip() == expected_error
