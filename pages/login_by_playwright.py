#pages/login_by_playwright.py

from playwright.sync_api import Page

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    
    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")
        self.logout_button = page.locator('a[href="/logout"]')

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()

    def get_flash_msg(self):
        return self.flash.inner_text()

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 브라우저 실행
        page = browser.new_page()    
        
        p = LoginPage(page)
        p.open()
        p.login("tomsmith","SuperSecretPassword!")
        
        print(p.get_flash_msg())

        browser.close()