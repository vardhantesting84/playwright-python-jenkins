from playwright.sync_api import Page,expect

def test_verify_title_tap(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page).to_have_title("Automation Testing Practice")
    # page.pause()
    page.locator("//input[@id='name']").fill("Sachin")
    page.locator("//input[@id='email']").fill("Sachin@gmail.com")
    page.locator("//input[@id='phone']").fill("1234567890")
