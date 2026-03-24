# tests/test_login_func.py

from selenium import webdriver                                # 브라우저를 실행 및 제어하기 위한 클래스
from selenium.webdriver.chrome.options import Options         # 크롬 브라우저 설정을 위한 클래스
from selenium.webdriver.common.by import By                   # 웹 요소를 찾기 위한 클래스
from selenium.webdriver.common.keys import Keys               # 키보드 입력을 제어하기 위한 클래스
from selenium.webdriver.support.ui import WebDriverWait       # 명시적 대기를 사용하기 위한 클래스
from selenium.webdriver.support import expected_conditions as EC     # 대기 조건을 제공하는 클래스


def test_login_success():
    driver = webdriver.Chrome()                                  # 크롬 브라우저 실행
    wait = WebDriverWait(driver, 10)                             # 최대 10초 동안 요소가 나타날 때까지 기다림
    driver.get("https://the-internet.herokuapp.com/login")       # 로그인 페이지로 이동

    # Username 입력
    username = wait.until(                                       # 입력창이 화면에 나타날 때까지 대기 후
        EC.visibility_of_element_located( (By.ID, "username")))  # 요소 가져오기
    username.clear()                                             # 기존 입력값 제거
    username.send_keys("tomsmith")                               # 아이디 입력

    # password 입력
    password = wait.until(                                       # 입력창이 화면에 나타날 때까지 대기 후
        EC.visibility_of_element_located((By.ID, "password")))   # 요소 가져오기
    password.clear()                                             # 기존 입력값 제거
    password.send_keys("SuperSecretPassword!")                   # 비밀번호 입력

    # 로그인 버튼 클릭
    login_btn = wait.until(                                      # 로그인 버튼이 클릭 가능할 때까지  대기
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))   
    login_btn.click()                                            # 로그인 버튼 클릭

    # flash 메시지 가져오기
    flash_msg = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))).text  # flash 메시지가 화면에 나타날 때까지 대기 후 텍스트 추출                             
    print(flash_msg)                                              # 콘솔에 메시지 출력 

    assert "You logged into a secure area!" in flash_msg          # 성공 메시지가 포함되어 있는지 확인
    assert "/secure" in driver.current_url                        # URL이 로그인 성공 페이지인지 확인
