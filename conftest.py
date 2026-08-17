import os

if not os.environ.get("CI"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

import pytest
from playwright.sync_api import Browser

AUTH_FILE = ".auth/state.json"

@pytest.fixture(scope="session")
def setup_auth(browser: Browser):
    """
    This fixture runs once per test session.
    It logs into the application and saves the storage state using the 
    built-in 'browser' fixture provided by pytest-playwright.
    """
    # Create the .auth directory if it doesn't exist
    os.makedirs(".auth", exist_ok=True)
    
    # Use the session-scoped browser provided by pytest-playwright
    context = browser.new_context()
    page = context.new_page()
    
    # 1. Navigate to the login page
    page.goto("https://www.saucedemo.com/")
    
    # 2. Perform the login
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    
    # 3. Wait for navigation to complete
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    
    # 4. Save the authenticated state
    context.storage_state(path=AUTH_FILE)
    
    # Close the setup context to free up memory
    context.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, setup_auth):
    """
    This fixture overrides the default pytest-playwright browser_context_args.
    It injects the saved storage state into every test's browser context.
    """
    return {
        **browser_context_args,
        "storage_state": AUTH_FILE
    }