# tests/test_assertion.py

from apps.mycalc import add, subtract, divide    
import pytest
import warnings

def test_various_assertion():

    # 참 / 거짓 검증 
    assert True
    assert [1, 2, 3]
    assert not []
    assert "hello"
    assert not ""
    assert False == 0
    assert True == 1

    # 비교 검증 
    assert 5 > 3
    assert 10 <= 10
    assert 7 != 8

    # 멤버십 검증 
    assert "pytest" in "pytest is easy"
    assert "world" not in "hello universe"
    assert 3 in [1, 2, 3, 4]
    assert 5 not in (1, 2, 3)

    # 동일성 검증 
    a = [1, 2]
    b = [1, 2]
    c = a
    assert a == b       # a와 b 값이 같다
    assert a is not b   # a와 b 값이 같지 않다
    assert a is c


# ========================================
# 부동 소수점 비교
def test_float_approx():

    # 1 / 3 = 0.33333... (무한소수)
    result = divide(1, 3)

    # 1. 정확한 값끼리 비교 (같은 연산끼리 비교)
    assert result == pytest.approx(1/3)

    # 2. 절대 허용 오차 (abs)
    # |실제값 - 기대값|
    assert result == pytest.approx(0.33333, abs=3.4e-6)

    # 3. 상대 허용 오차 (rel)
    # |실제값 - 기대값| / 기대값
    assert result == pytest.approx(0.33333, rel=1.1e-5)


# --- 예외 발생 테스트: pytest.raises ---
def test_divide_wrong_type_raises_exception():
    with pytest.raises(ValueError):     # 예외 미발생
        divide(10, 2)
        
    with pytest.raises(ValueError):     # 다른 종류 예외 발생 시 실패
        divide(10, "2")


def function_that_warns():
    warnings.warn("이 함수는 곧 제거될 예정입니다.", DeprecationWarning)
    return True

def test_deprecation_warning():
    with pytest.warns(DeprecationWarning):
        assert function_that_warns()