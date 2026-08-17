import os
from pathlib import Path
import pytest
from playwright.sync_api import Browser, expect
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Force Playwright to use local browsers ONLY if not running in CI
if not os.environ.get("CI"):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

ROOT_DIR = Path(__file__).parent
AUTH_DIR = ROOT_DIR / ".auth"
AUTH_FILE = AUTH_DIR / "state.json"

@pytest.fixture(scope="session", autouse=True)
def setup_auth(browser: Browser):
    """Logs in once and saves the state for all tests."""
    
    AUTH_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch credentials dynamically from the environment
    username = os.getenv("VALID_USERNAME")
    password = os.getenv("VALID_PASSWORD")
    
    if not username or not password:
        raise ValueError("Missing credentials! Check your .env file or GitHub Secrets.")

    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='username']").fill(username)
    page.locator("[data-test='password']").fill(password)
    page.locator("[data-test='login-button']").click()
    
    # Ensure login is successful before saving state
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Save the authenticated state and close the browser context
    context.storage_state(path=str(AUTH_FILE))
    context.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": str(AUTH_FILE),
    }