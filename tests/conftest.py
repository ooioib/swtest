#tests/conftest.py

import pytest
from apps.calculator import Calculator
from tests.data_loader import load_test_data
from selenium import webdriver                 
from selenium.webdriver.chrome.options import Options as Option           


@pytest.fixture(scope="module")
def calculator_instance(): #픽스쳐함수
    print("\n--Calculator 인스턴스 생성(conftest.py)")
    calc = Calculator()
    return calc

def pytest_generate_tests(metafunc):
    print(f"metafunc: {metafunc.fixturenames}")

    if "ADDCASES" in metafunc.fixturenames:
        cases = load_test_data("add.csv")
        metafunc.parametrize("ADDCASES", cases)
        
    elif "SUBCASES" in metafunc.fixturenames:
        cases = load_test_data("sub.csv")
        metafunc.parametrize("SUBCASES", cases)        

# headless 옵션 등록
# 터미널 실행 : pytest tests/실행할 파일명.py --headless
# pytest tests/conftest.py --headless
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")

# 웹 페이지 셀레니움 크롬 드라이버
@pytest.fixture(scope="function") # Session
def driver(request):
    headless = request.config.getoption("--headless")  # 명령줄 옵션 확인
    opts = Option()
    
    if headless:
        opts.add_argument("--headless")  # headless 모드로 실행
        opts.add_argument("--window-size=1280,900")  

    d = webdriver.Chrome(options=opts)            
    print("#### driver 시작 ####")
    yield d
    d.quit()


@pytest.fixture(autouse=True)
def reset_browser_state(driver):
    driver.delete_all_cookies()
    driver.get("about:blank")


# playwright
from playwright.sync_api import sync_playwright
# 브라우저는 한 번만 띄우고
@pytest.fixture(scope="session")
def browser(request):
    headless = request.config.getoption("--headless")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()

# 각 테스트마다 독립된 페이지 사용
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()