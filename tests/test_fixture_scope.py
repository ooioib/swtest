# tests/test_fixture_scope.py

import pytest

# fixture 정의
@pytest.fixture(scope="class")
def sample_data():
    print("\n data laod")                # fixture가 실행될 때 출력 (언제 실행되는지 확인용)
    data = {"id":1, "name":"henry"}      # 테스트에서 사용할 공통 데이터 생성
    return data                          # 값을 테스트 함수로 전달


# 첫 번째 테스트 클래스
class TestUser:
    def test_id(self, sample_data):          # sample_data를 인자로 받으면 pytest가 자동으로 fixture 주입
        assert sample_data['id'] == 1        # id 값 검증

    def test_name(self, sample_data):        # name 값 검증
        assert sample_data['name'] == "henry"


# 두 번째 테스트 클래스
class TestGuest:
    def test_id(self, sample_data):           # 동일한 fixture 사용
        assert sample_data['id'] == 1

    