# selenium/melon.py

# 브라우저를 실행 및 제어하기 위한 클래스
from selenium import webdriver

# 크롬 브라우저 설정을 위한 클래스
from selenium.webdriver.chrome.options import Options

# 웹 요소를 찾기 위한 클래스
from selenium.webdriver.common.by import By

# 키보드 입력을 제어하기 위한 클래스
from selenium.webdriver.common.keys import Keys

# 명시적 대기를 사용하기 위한 클래스
from selenium.webdriver.support.ui import WebDriverWait

# 대기 조건을 제공하는 클래스
from selenium.webdriver.support import expected_conditions as EC    


opts = Options()                                # 크롬 옵션 객체 생성
opts.add_experimental_option("detach", True)    # 브라우저를 닫아도 창이 유지
opts.add_argument("--window-size=1280, 900")    # 브라우저 백그라운드 실행

driver = webdriver.Chrome(options = opts)    # 옵션 적용 후 크롬 브라우저 실행
wait = WebDriverWait(driver, 10)             # 최대 10초 동안 조건을 만족할 때까지 대기

try:
    driver.get("https://www.melon.com")     # 해당 URL로 이동 (웹페이지 열기)
    wait.until(lambda d : d.title != "")     # 페이지 제목이 공백이 아님
    print(f"Title: {driver.title}")          # 페이지 제목 출력

    elem = wait.until(EC.visibility_of_element_located(
        (By.ID, "top_search")))    # 검색 입력창이 화면에 보일 때까지 대기 후 요소 가져오기
    elem.clear()                        # 입력 필드 초기화
    elem.send_keys("bts")               # 검색어 입력
    elem.send_keys(Keys.ENTER)          # 엔터키 입력(검색 실행)


    # 앨범 탭으로 이동
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[title="앨범 - 페이지 이동"]' ))).click()
    

    # 첫번째 앨범 선택
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[title="ARIRANG - 페이지 이동"]'))).click()


    # 곡 정보 아이콘 선택
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[title="Body to Body 곡정보"]'))).click()


    # 노래 제목 가져오기
    title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, 'song_name'))).text


    # 노래 가사 가져오기
    lyrics = wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'd_video_summary'))).text

    with open(title + ".txt", "w", encoding="utf-8") as f:
        f.write(lyrics)

    print(f"{title}.txt 파일에 노래 가사가 저장되었습니다.")


finally:
#    driver.quit()      # 브라우저 종료
    pass                # 아무런 동작 X