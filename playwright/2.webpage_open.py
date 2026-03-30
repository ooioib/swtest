# playwright/2.webpage_open.py
# browser context 생성하여 페이지 만들기

# playwright 라이브러리에서 sync_playwright 함수를 가져옴
# sync_playwright : 동기 방식으로 브라우저 자동화를 수행
from playwright.sync_api import sync_playwright


# 1. Playwright 환경 실행
# with 문을 사용하면 블록이 끝난 후 자동으로 브라우저 종료
with sync_playwright() as p:

    # 브라우저 실행                               # headless=True : 창 없이 백그라운드 실행
    browser = p.chromium.launch(headless=False)  # headless=False : 창이 화면에 표시

    # 새로운 브라우저 컨텍스트 생성
    # 독립적인 브라우저 환경 생성 (쿠키, 로그인 상태 등 분리 가능)
    context = browser.new_context()

    # 새 페이지 생성
    page = browser.new_page()

    # 웹 사이트 이동
    page.goto("https://google.com")             
    print(page.title())  # 페이지 제목 출력    

    # 화면 캡처
    # 현재 폴더에 screenshot.png 파일 생성
    page.screenshot(path="screenshot.png") 

    page.pause()        # 코드 일시 정지
    
    context.close()     # 컨텍스트 종료
    browser.close()     # 브라우저 종료