#tests/conftest.py

from apps.calculator import Calculator
import pytest

from tests.data_loader import load_test_data

@pytest.fixture(scope="module")
def calculator_instance(): #픽스쳐함수
    print("\n--Calculator 인스턴스 생성(conftest.py)")
    calc = Calculator()
    return calc


def pytest_generate_tests(metafunc):
    print(f"metafunc: {metafunc.fixturenames}")

    if "ADDCASES" in metafunc.fixturenames:
        cases = load_test_data("add.csv")
        metafunc.parametrize("ADDCASES", cases)
        
    elif "SUBCASES" in metafunc.fixturenames:
        cases = load_test_data("sub.csv")
        metafunc.parametrize("SUBCASES", cases)        