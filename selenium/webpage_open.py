# selenium/webpage_open.py

# 브라우저를 실행 및 제어하기 위한 클래스
from selenium import webdriver

# 크롬 브라우저 설정을 위한 클래스
from selenium.webdriver.chrome.options import Options

# 크롬 옵션 객체 생성
opts = Options()

# 브라우저를 닫아도 창이 유지
opts.add_experimental_option("detach", True)

# 브라우저 백그라운드 실행
# opts.add_argument("--headless=new")
opts.add_argument("--window-size=1280, 900")

# 옵션 적용 후 크롬 브라우저 실행
driver = webdriver.Chrome(options = opts)

try:
    driver.get("https://www.python.org")  # 해당 URL로 이동 (웹페이지 열기)
    print(f"Title: {driver.title}")       # 페이지 제목 출력

finally:
#    driver.quit()      # 브라우저 종료
    pass                # 아무런 동작 X