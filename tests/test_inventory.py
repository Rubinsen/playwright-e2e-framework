import re
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

def test_bypass_login_and_view_inventory(page: Page):
    """
    This test uses the InventoryPage object to interact with the DOM,
    keeping assertions clean and separated from page mechanics.
    """
    # 1. Instantiate the page object
    inventory_page = InventoryPage(page)
    
    # 2. Navigate directly to the inventory page (relying on our auth fixture)
    inventory_page.navigate()
    
    # 3. Perform assertions (Assertions stay in the test file, actions stay in the page object)
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(inventory_page.products_header).to_have_text("Products")
    expect(inventory_page.inventory_items).to_have_count(6)