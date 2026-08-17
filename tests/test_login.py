import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


# 1. Override the global context to NOT use the saved login state
@pytest.fixture
def browser_context_args(browser_context_args):
    """
    This local fixture overrides the session-level one in conftest.py.
    By setting storage_state to None, we force a fresh, logged-out browser.
    """
    return {**browser_context_args, "storage_state": None}


# 2. Parametrize the test with multiple data sets
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
        (
            "standard_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
    ],
)
def test_invalid_login_shows_error(page: Page, username, password, expected_error):
    """
    This single test function will run 4 separate times,
    once for each row of data in the parametrize decorator above.
    """
    login_page = LoginPage(page)

    # Navigate to the site
    login_page.navigate()

    # Attempt to log in with the bad credentials
    login_page.login(username, password)

    # Verify the correct error message is displayed
    expect(login_page.error_message).to_have_text(expected_error)
