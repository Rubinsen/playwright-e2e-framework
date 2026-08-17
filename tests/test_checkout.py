from playwright.sync_api import expect, Page


def test_checkout_with_seeded_cart(page: Page):
    """
    Demonstrates state seeding by bypassing the UI to inject items
    directly into the browser's local storage before navigating.
    """

    # 1. Navigate to the domain first. (You cannot set localStorage for a domain
    # until the browser is actively on that domain).
    page.goto("https://www.saucedemo.com/inventory.html")

    # 2. SEED THE STATE: Bypass the UI clicks entirely.
    # We inject JavaScript to forcefully write the cart data into memory.
    # [4, 1] represent the internal IDs for the Backpack and the Bolt T-Shirt.
    page.evaluate("window.localStorage.setItem('cart-contents', '[4, 1]')")

    # 3. Navigate directly to the cart page.
    # The application will read our injected memory and render the UI accordingly.
    page.goto("https://www.saucedemo.com/cart.html")

    # 4. Assert the UI properly built itself around our backend/memory data
    expect(page.locator(".cart_item")).to_have_count(2)
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()
    expect(page.get_by_text("Sauce Labs Bolt T-Shirt", exact=True)).to_be_visible()
