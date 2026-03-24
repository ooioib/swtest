# pages/login.py

from selenium import webdriver                                # 브라우저를 실행 및 제어하기 위한 클래스
from selenium.webdriver.chrome.options import Options         # 크롬 브라우저 설정을 위한 클래스
from selenium.webdriver.common.by import By                   # 웹 요소를 찾기 위한 클래스
from selenium.webdriver.common.keys import Keys               # 키보드 입력을 제어하기 위한 클래스
from selenium.webdriver.support.ui import WebDriverWait       # 명시적 대기를 사용하기 위한 클래스
from selenium.webdriver.support import expected_conditions as EC     # 대기 조건을 제공하는 클래스


# 로그인 페이지 클래스
class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"         # 로그인 페이지 주소
    
    # 페이지 요소
    USERNAME = (By.ID, "username")                           # 아이디 입력창
    PASSWORD = (By.ID, "password")                           # 비밀번호 입력창
    LOGIN = (By.CSS_SELECTOR, "button[type='submit']")       # 로그인 버튼
    FLASH = (By.ID, "flash")                                 # 결과 메시지 영역
    LOGOUT = (By.CSS_SELECTOR, 'a[href="/logout"]')          # 로그아웃 버튼

    def __init__(self, d, timeout=20):
        self.driver = d                                      # 브라우저 저장
        self.wait = WebDriverWait(d, timeout)                # 최대 timeout초 대기

    def open(self):
        self.driver.get(self.URL)                            # 로그인 페이지 열기
        
    def input_username(self, username):
        # 아이디 입력창이 보일 때까지 기다림
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME))
        username_input.clear()                               # 기존 값 삭제
        username_input.send_keys(username)                   # 아이디 입력

    def input_password(self, password):
        # 비밀번호 입력창이 보일 때까지 기다림
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD))
        password_input.clear()                               # 기존 값 삭제
        password_input.send_keys(password)                   # 비밀번호 입력

    def click_login(self):
        # 로그인 버튼이 클릭 가능할 때까지 대기
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN))
        login_btn.click()                                    # 로그인 버튼 클릭

    def login(self, username, password):
        # 로그인 전체 과정 (아이디 + 비밀번호 + 클릭)
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def get_message(self):
        # 결과 메시지가 나타날 때까지 기다린 후 텍스트 반환
        flash_msg = self.wait.until(
            EC.visibility_of_element_located(self.FLASH)).text
        return flash_msg
    
    def click_logout(self):
        # 로그아웃 버튼 클릭
        logout_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT))
        logout_btn.click()

    def current_url(self):
        return self.driver.current_url                       # 현재 URL 반환
    

# 실행 코드
if __name__ == "__main__":
    d = webdriver.Chrome()                                  # 크롬 실행
    page = LoginPage(d, 10)

    page.open()                                             # 페이지 열기
    page.login("tomsmith", "SuperSecretPassword!")           # 로그인 실행

    print(page.get_message())                               # 결과 메시지 출력
    print(page.current_url())                               # 현재 URL 출력

    # input("종료하려면 Enter")