from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.title = page.locator("#title")
        self.error = page.locator("[data-test=\"error\"]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
    
    def emptyLogin(self):
        return self.error.innertext()
