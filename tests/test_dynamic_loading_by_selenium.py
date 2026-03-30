# tests/test_dynamic_loading_by_selenium.py
# 실행 명령어 : pytest tests/test_dynamic_loading_by_selenium.py -v
# driver -> page.goto
# wait -> page 변경

# Selenium 관련 라이브러리 가져오기
from selenium.webdriver.common.by import By  # 요소 찾기 방식 지정
from selenium.webdriver.support.ui import WebDriverWait  # 명시적 대기 기능
from selenium.webdriver.support import expected_conditions as EC  # 대기 조건 정의


# 테스트할 페이지 URL
URL = "https://the-internet.herokuapp.com/dynamic_loading/2"


def test_dynamic_loading_selenium(driver):

    # 최대 10초 동안 대기하는 객체 생성
    wait = WebDriverWait(driver, 10)

    # 브라우저로 페이지 열기
    driver.get(URL)

    # Start 버튼 요소 찾기 (CSS 선택자 사용)
    # driver.find_element(By.CSS_SELECTOR, "#start button")

    # Start 버튼이 클릭 가능할 때까지 대기 후 클릭
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))).click()

    # 로딩 완료 요소가 화면에 나타날 때까지 대기 후 텍스트 읽기
    flash_msg = wait.until(EC.visibility_of_element_located((By.ID, "finish"))).text

    # 'Hello World'가 flash_msg 안에 포함되어 있는지 텍스트 확인
    assert "Hello World" in flash_msg
    
