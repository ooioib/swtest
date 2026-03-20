# apps/calculator.py

# from apps.calculator import Calculator
import pytest

# -------------------------------
# fixture: 테스트에서 공통으로 사용할 객체 생성

# @pytest.fixture
# def calculator_instance():      # 픽스처 함수
#     calc = Calculator()         # Calculator 객체 생성
#     return calc                 # 테스트 함수로 객체 반환


# -------------------------------
# 덧셈 기능 테스트

def test_add(calculator_instance):
    assert calculator_instance.add(2, 3) == 5     # 2 + 3 = 5 검증
    assert calculator_instance.add(-1, 1) == 0    # -1 + 1 = 0 검증


# -------------------------------
# 뺄셈 기능 테스트

def test_subtract(calculator_instance):
    assert calculator_instance.subtract(2, 3) == -1     # 2 - 3 = -1 검증
    assert calculator_instance.subtract(-1, 1) == -2    # -1 - 1 = -2 검증


# -------------------------------
# 나눗셈 기능 테스트

def test_divide(calculator_instance):
    assert calculator_instance.divide(6, 3) == 2    # 6 / 3 = 2 검증
    assert calculator_instance.divide(1, 3) == pytest.approx(1/3)    # 1 / 3은 무한소수 → 근사값 비교 사용


# -------------------------------
# 0으로 나누는 경우 예외 발생 테스트

 # ZeroDivisionError 발생 여부 확인
def test_divide_by_zero(calculator_instance):
    with pytest.raises(ZeroDivisionError):
        calculator_instance.divide(1, 0)