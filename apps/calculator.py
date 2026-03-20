# apps/calculator.py

class Calculator:
    
    # 두 수를 입력하면 더해주는 함수
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("입력 값은 숫자이어야 합니다.")
        return a + b

    # 두수의 차를 구하는 함수 subtract()를 추가
    def subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError ("입력 값은 숫자이어야 합니다.")
        return a - b


    # 부동 소수점 비교
    def divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("입력 값은 숫자이어야 합니다.")
        if b == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        return a / b
        
    