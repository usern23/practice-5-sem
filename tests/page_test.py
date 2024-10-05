import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], "../pages"))

import pytest
from playwright.sync_api import Page, expect, sync_playwright
from LoginPage import LoginPage
from ProductPage import ProductPage

def browser():
    headless =  os.getenv("HEADLESS", 'false').lower() == "true"
    browser_type = os.getenv("BROWSER", 'chromium')
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=headless)
        yield browser
        browser.close()

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(browser):
    page = browser.new_page()
    yield
    page.close()

def test_emptyLoginOrPassword(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "secret_sauce")
    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text("Epic sadface: Username is required")

def test_invalid_login(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "wrong_password")
    error_message = page.inner_text(".error-message-container")
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

def test_product_sort(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    product_page.sort_products_by("Price (low to high)")
    product_prices = product_page.get_product_prices()
    assert product_prices == sorted(product_prices)
