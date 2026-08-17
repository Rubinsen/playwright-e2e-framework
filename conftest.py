import os
import pytest
from playwright.sync_api import Browser, expect
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Force Playwright to use local browsers ONLY if not running in CI
if not os.environ.get("CI"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

AUTH_FILE = ".auth/state.json"

@pytest.fixture(scope="session", autouse=True)
def setup_auth(browser: Browser):
    """Logs in once and saves the state for all tests."""

    context = browser.new_context()
    
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    
    # Fetch credentials dynamically from the environment
    username = os.getenv("VALID_USERNAME")
    password = os.getenv("VALID_PASSWORD")
    
    if not username or not password:
        raise ValueError("Missing credentials! Check your .env file or GitHub Secrets.")

    page.locator("[data-test='username']").fill(username)
    page.locator("[data-test='password']").fill(password)
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