from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

def test_inventory_survives_cdn_outage(page: Page):
    """
    Simulates a network failure where the image hosting server crashes.
    Verifies that the application remains functional and doesn't white-screen.
    """
    # 1. Intercept all image requests and force a 500 Internal Server Error
    page.route("**/*.{png,jpg,jpeg}", lambda route: route.fulfill(
        status=500,
        content_type="text/plain",
        body="Internal Server Error: CDN Unreachable"
    ))
    
    # 2. Instantiate the page object and navigate (using the saved auth state)
    inventory_page = InventoryPage(page)
    inventory_page.navigate()
    
    # 3. Verify the core application still rendered successfully
    expect(inventory_page.products_header).to_be_visible()
    expect(inventory_page.inventory_items).to_have_count(6)
    
    # 4. Verify that the "Add to cart" buttons are still operational
    # This proves the user can still interact with the system during a partial outage
    first_item_button = inventory_page.inventory_items.first.locator("button")
    expect(first_item_button).to_be_enabled()
    expect(first_item_button).to_have_text("Add to cart")