# tests\test_dynamic_loading_by_playwright.py

import pytest
from playwright.sync_api import expect
from pages.login_by_playwright import LoginPage


LOGIN_CASES = [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", "https://the-internet.herokuapp.com/secure"),
    ("tomsmith", "wrongpassword", "Your password is invalid!", "https://the-internet.herokuapp.com/login"),
    ("wronguser", "SuperSecretPassword!", "Your username is invalid!", "https://the-internet.herokuapp.com/login"),
]


@pytest.mark.parametrize("username, password, expected_msg, expected_url", LOGIN_CASES)
def  test_login(page, username, password, expected_msg, expected_url):
    p = LoginPage(page)
    p = open()
    p.login(username, password)

    expect(p.flash).to_contain_text(expected_msg, timeout=10000)
    expect(page).to_have_url(expected_url)