# playwright/3.multi_page.py
# 여러 페이지 열기(각 페이지가 서로 다른 context )

# playwright 라이브러리에서 sync_playwright 함수를 가져옴
# sync_playwright : 동기 방식으로 브라우저 자동화를 수행
from playwright.sync_api import sync_playwright


# 1. Playwright 환경 실행
# with 문을 사용하면 블록이 끝난 후 자동으로 브라우저 종료
with sync_playwright() as p:

    # 브라우저 실행                               # headless=True : 창 없이 백그라운드 실행
    browser = p.chromium.launch(headless=False)  # headless=False : 창이 화면에 표시

    # 첫 번째 페이지 생성
    page1 = browser.new_page()         # 새 페이지 생성
    page1.goto("https://google.com")   # 사이트 이동
    
    # 두 번째 페이지 생성
    page2 = browser.new_page()
    page2.goto("https://www.naver.com")

    input("아무 키나 누르면 끝납니다.")

    browser.close()     # 브라우저 종료