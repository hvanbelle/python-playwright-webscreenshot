from playwright.sync_api import sync_playwright

this_site = "https://www.vanbellenet.eu/"
result_image = "vanbellenet.eu.png"

def run(playwright):
    # launch the browser
    browser = playwright.chromium.launch()
    # opens a new browser page
    page = browser.new_page()
    # navigate to the website
    page.goto(this_site)
    # take a full-page screenshot
    page.screenshot(path=result_image, full_page=True)
    # always close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)