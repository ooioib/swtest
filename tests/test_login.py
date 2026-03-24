import pytest
from pages.login import LoginPage


def test_login_success(driver):
    page = LoginPage(driver, 10)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    flash_msg = page.get_message()

    assert "You logged into a secure area!" in flash_msg
    assert "/secure" in page.current_url()


def test_logout(driver):
    page = LoginPage(driver, 10)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    page.click_logout()

    flash_msg = page.get_message()

    assert "You logged out of the secure area!" in flash_msg
    assert "/login" in page.current_url()


LOGIN_CASES = [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", "/secure"),
    ("tomsmith", "wrongpassword", "Your password is invalid!", "/login"),
    ("wronguser", "SuperSecretPassword!", "Your username is invalid!", "/login"),
]


@pytest.mark.parametrize("username, password, expected_text, expected_url", LOGIN_CASES)
def test_login(driver, username, password, expected_text, expected_url):
    page = LoginPage(driver, 10)
    page.open()
    page.login(username, password)

    flash_msg = page.get_message()

    assert expected_text in flash_msg
    assert expected_url in page.current_url()