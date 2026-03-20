# ========== 표준 입력 함수 input ==========

# input() : 사용자로부터 값 입력 받기
num1 = input("첫번째 숫자를 입력하세요. : ")
print(num1)

num2 = input("두번째 숫자를 입력하세요. : ")
print(num2)

# print(num1+num2) => 타입 캐스팅 필요
print(f"{num1} + {num2} = {num1+num2}")


# 형변환
num1 = int(input("첫번째 숫자를 입력하세요. : "))
print(num1)

num2 = int(input("두번째 숫자를 입력하세요. : "))
print(num2)

print(f"{num1} + {num2} = {num1+num2}")


# 자료형
# type() : 자료형 확인
# bool : 빈 문자열은 F, 공백이 하나라도 있으면 T
print(type(bool("")))  
print(type(bool(" ")))