# selenium/page_navi.py


# 브라우저를 실행 및 제어하기 위한 도구
from selenium import webdriver

# 크롬 브라우저 설정을 위한 도구
from selenium.webdriver.chrome.options import Options

# 시간 지연을 위한 모듈
import time

# 크롬 옵션 객체 생성
opts = Options()

# 브라우저 닫아도 창 유지
opts.add_experimental_option("detach", True)

# 브라우저를 화면 없이 실행 (백그라운드 실행)
# opts.add_argument("--headless=new")

# 브라우저 창 크기 설정
opts.add_argument("--window-size=1280, 900")

# 옵션 적용 후 크롬 브라우저 실행
driver = webdriver.Chrome(options = opts)

try:
    driver.get("https://www.python.org")    # 첫번째 페이지 이동
    print(f"Title: {driver.title}")         # 페이지 제목 출력
    time.sleep(3)                           # 3초 대기

    driver.get("https://www.naver.com")     # 두번째 페이지 이동
    print(f"Title: {driver.title}")         # 페이지 제목 출력
    time.sleep(3)                           # 3초 대기

    driver.back()        # 뒤로가기
    time.sleep(3)

    driver.forward()    # 앞으로 가기  
    time.sleep(3)

    driver.refresh()     # 새로고침    

finally:
#    driver.quit()      # 브라우저 종료
    pass                # 아무런 동작 X