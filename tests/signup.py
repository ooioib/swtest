# tests/signup.py

import pytest
from pages.signup import SignupPage

@pytest.fixture
def signup_page(driver):
    page = SignupPage(driver)
    page.open()
    return page

# 테스트 케이스
SIGNUP_CASES = [
    {
        "email":"user@ex.com", 
        "username":"max",
        "pw":"abc12345", 
        "confirm":"abc12345",
        "terms":True,
        "expect" : "가입이 완료되었습니다!"
    },
    {
        "email":"", 
        "username":"max",
        "pw":"abc12345", 
        "confirm":"abc12345",
        "terms":True,
        "expect" : "입력값을 다시 확인해주세요"      
    },
]
@pytest.mark.parametrize("case",SIGNUP_CASES)
def test_signup(signup_page, case):
    signup_page.signup(
        case["email"],
        case["username"],
        case["pw"],
        case["confirm"],
        case["terms"] 
    )

    flash_msg = signup_page.flash_message()
    assert case["expect"] in flash_msg

