# test_fixture_yield.py

import pytest

@pytest.fixture
def file_writer():

    # [SETUP 단계] 테스트 실행 전에 파일을 열어줌
    # "w" 모드 → 기존 내용 덮어쓰기
    f = open("test.txt", "w", encoding="utf-8")
    print("파일 열기")

    # yield를 만나면 잠시 멈추고
    # f 객체를 테스트 함수로 전달함
    yield f


    # [TEARDOWN 단계] 테스트가 끝나면 다시 여기로 돌아와 실행
    print("파일 닫기")
    f.close()


# [테스트 함수]
# pytest는 함수 인자를 보고 fixture를 자동으로 실행하고
# yield에서 반환된 값을 file_writer에 넣어준다.
def test_write_sentence(file_writer):

    # fixture setup 이후 실행됨
    print("테스트 시작")

    text = "pytest fixture test\n"

    # 파일에 문자열 작성
    file_writer.write(text)

    # 버퍼에 남아있는 데이터를 즉시 파일에 반영
    file_writer.flush()

    # [검증 단계] 파일을 다시 열어서 내용 확인
    with open("test.txt", encoding="utf-8") as f:
        content = f.read()

        # 우리가 쓴 텍스트가 실제로 파일에 있는지 검증
        assert text in content