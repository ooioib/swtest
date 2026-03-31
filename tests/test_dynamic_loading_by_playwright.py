# tests/test_dynamic_loading_by_playwright.py

from playwright.sync_api import sync_playwright, Page, expect

# 테스트할 페이지 URL
URL = "https://the-internet.herokuapp.com/dynamic_loading/2"


def test_dynamic_loading_playwright(page:Page):

    # 페이지 이동
    page.goto(URL)

    # Start 버튼 클릭
    page.locator("#start button").click()

    flash = page.get_by_role("heading", name="Hello World!")
    expect(flash).to_have_text("Hello World!", timeout=10000)

#    [방법 1]
#    flash_msg = page.locator("#finish").inner_text()
#    print(f"####{flash_msg}###")
#    assert "Hello World" in flash_msg
    

#    [방법 2]
#     # 로딩 완료 요소 선택
#     flash = page.locator("#finish")
#     # 요소가 화면에 나타나고 텍스트가 일치 하는지 검증
#     expect(flash).to_have_text("Hello World!", timeout=10000)


#   [방법3]
#    expect(page.locator("#loading")).to_be_hidden(timeout=10000)
#    flash = page.locator("#finish")
#    expect(flash).to_have_text("Hello World!")


#   [방법4]
#   flash = page.locator("#finish")
#   expect(flash).to_have_text("Hello World!", use_inner_text=True)
    
#     Page.pause()