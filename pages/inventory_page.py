from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.products_header = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")

    def navigate(self):
        """Navigate directly to the inventory page."""
        self.page.goto("https://www.saucedemo.com/inventory.html")