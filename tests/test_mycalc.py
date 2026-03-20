# test/test_mycalcs.py

from apps.mycalc import add, subtract     
import pytest                       # 테스트 대상 함수 가져오기 

def test_add_positive_numbers():    # 매개변수가 양수인지 테스트

    a = 12
    b = 13
    expect = 25

    actual = add(a, b)
    assert expect == actual         # 결과 검증


# ==================================
# 음수를 포함하여 더하는 경우

def test_add_negative_numbers():    # 매개변수가 양수인지 테스트

    a = -3
    b = -5
    expect = -8

    actual = add(a, b)
    assert expect == actual         # 결과 검증


# ==================================
# [미션] mycalc.py 에 두수의 차를 구하는 함수 subtract()를 추가하고,
# test_mycalc.py 에서 subtract()를 테스트 하는 코드를 추가해 주세요


# 1. 양수끼리의 뺄셈을 테스트
def test_substract_positive_numbers():
    assert subtract(10, 3) == 7

# 2. 결과가 음수가 되는 뺄셈을 테스트
def test_substract_negative_numbers():
    assert subtract(5, 8) == -3


# 3. 음수를 포함한 뺄셈 테스트
def test_substract_with_negative_number():
    assert subtract(5, -3) == 8
    assert subtract(-3, 5) == -8

# 실패 보고서 읽기
# def tests_fail_example():
#   assert add(1, 1) == 3