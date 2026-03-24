# pages/signup.py

from selenium import webdriver                                # 브라우저를 실행 및 제어하기 위한 클래스
from selenium.webdriver.common.by import By                   # 웹 요소를 찾기 위한 클래스
from selenium.webdriver.support.ui import WebDriverWait       # 명시적 대기를 사용하기 위한 클래스
from selenium.webdriver.support import expected_conditions as EC     # 대기 조건을 제공하는 클래스

# 회원가입 페이지 클래스 
class SignupPage:
    # 로컬 HTML 파일 경로
    URL = "file:///C:/Users/USER/Documents/swtest/pages/signup.html" 

    # 페이지 요소 정의 
    EMAIL    = (By.ID, "email")                             # 이메일 입력창
    USERNAME = (By.ID, "username")                          # 아이디 입력창
    PASSWORD = (By.ID, "password")                          # 비밀번호 입력창
    CONFIRM  = (By.ID, "confirm")                           # 비밀번호 확인 입력창
    TERMS    = (By.ID, "terms")                             # 약관 체크박스
    SUBMIT   = (By.CSS_SELECTOR, "button[type='submit']")   # 가입 버튼
    FLASH    = (By.ID, "flash")                             # 결과 메시지 영역

    # 초기화
    def __init__(self, driver, timeout=10):
        self.driver = driver                                # 브라우저 객체 저장
        self.wait = WebDriverWait(driver, timeout)          # 최대 timeout 동안 요소 대기


    # 페이지 열기
    def open(self):
        self.driver.get(self.URL)                           # 지정된 URL로 이동


    # 입력 공통 함수 (재사용)
    def clear_and_type(self, locator, value):
        elem = self.wait.until(                             # 요소가 보일 때까지 기다림
            EC.visibility_of_element_located(locator) )
        elem.clear()                                        # 기존 입력값 삭제
        elem.send_keys(value)                               # 새로운 값 입력


    # 체크박스 처리 함수
    def set_checkbox(self, locator, should_be_checked):
        elem = self.wait.until(                             # 체크박스가 클릭 가능할 때까지 대기
            EC.element_to_be_clickable(locator))
        
        if elem.is_selected() != should_be_checked:         # 현재 상태와 원하는 상태가 다르면 클릭
            elem.click()


    # 회원가입 전체 흐름
    def signup(self, email="", username="", pw="", confirm="", terms=False):
        self.clear_and_type(self.EMAIL, email)              # 이메일 입력
        self.clear_and_type(self.USERNAME, username)        # 아이디 입력
        self.clear_and_type(self.PASSWORD, pw)              # 비밀번호 입력
        self.clear_and_type(self.CONFIRM, confirm)          # 비밀번호 확인 입력
        self.set_checkbox(self.TERMS, terms)                # 약관 체크 여부 설정

        btn = self.wait.until(                              # 가입 버튼이 클릭 가능할 때까지 대기
            EC.element_to_be_clickable(self.SUBMIT))
        btn.click()                                         # 가입 버튼 클릭


    # 결과 메시지 가져오기
    def flash_message(self):
        msg = self.wait.until(                              # 메시지가 DOM에 존재할 때까지 대기
            EC.presence_of_element_located(self.FLASH)).text
        return msg                                            # 메시지 텍스트 반환


# 실행 테스트 코드
if __name__ == "__main__":
    d = webdriver.Chrome()               # 크롬 브라우저 실행
    page = SignupPage(d, 10)             # 페이지 객체 생성
    page.open()                          # 회원가입 페이지 열기

    # 테스트용 입력값
    page.signup(
        email="user@example.com",        # 이메일
        username="tester",               # 아이디
        pw="abc12345",                   # 비밀번호
        confirm="abc12345",              # 비밀번호 확인
        terms=True                       # 약관 동의
    )

    print("msg:", page.flash_message())  # 결과 메시지 출력