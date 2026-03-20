# tests/test_calculator_param.py

import pytest
from data_loader import load_test_data

add_test_case = [
    (2, 3, 5), (-1, -1, -2), (5, -3, 2), (10, 0, 10), 
    (0.1, 0.2, pytest.approx(0.3)),
    pytest.param(100, 200, 300, id="large_number")]

@pytest.mark.parametrize("a, b, expected", add_test_case)
def test_add_case(calculator_instance, a, b, expected):
    assert calculator_instance.add(a, b) == expected


# 예외 테스트
divide_test_case = [("2", 1, TypeError),
                    (10, "2", TypeError),
                    (2, 0, ZeroDivisionError),
                    (-1, 2, ValueError),
                    pytest.param(None, 2, TypeError, id="None_input")]

@pytest.mark.parametrize("a, b, expected", divide_test_case)
def test_add_case(calculator_instance, a, b, expected):
    with pytest.raises(expected):
        calculator_instance.divide(a, b)


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 100])
def test_stacked_cases(x, y):
    assert isinstance(x, int)
    assert isinstance(y, int)


# file 불러오기
@pytest.mark.parametrize("a, b, expected", load_test_data("add.csv"))
def test_add(calculator_instance, a, b, expected):
    if expected == TypeError:
        with pytest.raises(expected):
            calculator_instance.add(a, b)
    else:
        assert calculator_instance.add(a, b) == expected


def test_add2(calculator_instance, ADDCASES):
    a, b,expected = ADDCASES
    if expected == TypeError:
        with pytest.raises(expected):
            calculator_instance.add(a, b)
    else:
        assert calculator_instance.add(a, b) == expected
