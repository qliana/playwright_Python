from playwright.sync_api import sync_playwright

def check_price():
  price2=500
  if price<price2:
    print("Price is less than 500, proceeding with the purchase.")
    # Add code to proceed with the purchase
     
with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.amazon.in/")
        page.locator("xpath=//div[@id='nav-link-groceries']").click()
        try:
        # Wait for "Skip" button if it appears (e.g., within 10 seconds)
          page.wait_for_selector("text=Skip", timeout=10000)
          page.click("text=Skip")
          print("✅ Skip button clicked.")
        except:
          print("⏭️ Skip button not found, continuing...")
        if page.locator(".a-modal-scroller").is_visible():
          page.keyboard.press("Escape")  # Or try to close it manually
          page.wait_for_selector(".a-modal-scroller", state="detached")

        page.locator("xpath=//img[@alt='Fruits & vegetables']").click()
        page.locator("xpath=//span[text()='Fresh Onion, 1kg']").click()
        price1=page.wait_for_selector("span.a-price-whole").text_content()
        fraction = page.wait_for_selector("span.a-price-fraction").text_content()
        price = f"{price1}.{fraction}"
        print(f"Price of Fresh Onion, 1kg: {price}")

        