# 사각형의 넓이 계산
def rect_area(x, y):
    print(f"사각형의 넓이는 {x*y} 입니다.")


# 사각형 넓이 계산 후 
def rect_area1(x, y):
    return x*y

# 사격형의 넓이와 둘레 계산
def rect_area2(x, y):
    return x*y, (x+y)*2

print(rect_area1(10, 20))
area, length = rect_area2(10, 20)
print(area, length)


# ==================================


# 정수를 입력하면 짝수인지 홀수인지 판별해주는 함수
def odd_even(x):
    if x % 2 == 0:         # 2로 나눴을 때 나머지가 0이면 짝수

        result = "짝수"     # 조건이 참이면 result 변수에 "짝수" 저장
    else:
        result = "홀수"     # 위 조건이 거짓이면

    return result           # result에 "홀수" 저장

print(odd_even(2))
print(odd_even(7))


# ==================================


def like_fruit(name, fruit = "apple"):
    print(f"{name}님이 좋아하는 과일은 {fruit}입니다.")

like_fruit("이순신")
like_fruit("이순신", "orange")
like_fruit(fruit="orange", name="이순신")


# ==================================
# 여러 숫자의 평균을 구하는 함수

def avg(*num):
    sum = 0             
    cnt = len(num)       # 입력된 숫자의 개수

    for i in num:        # num 안에 있는 숫자를 하나씩 꺼내 반복

        sum = sum + i    # 합계 누적

    return sum / cnt     # 평균 계산

print(avg(10, 20, 30))
print(avg(10, 20, 30, 50, 60))
print(avg(10, 20))


# ==================================
# 지역변수, 전역 변수
pi = 3.14

# 원의 넓이 계산
def circle_area(r) :
    pi = 3.1
    area = r * r * pi                # 원의 넓이(넓이 = 반지름 × 반지름 × π)
    return area
result = circle_area(10)             # r = 10
print(f"원의 넓이는 {result}입니다")  # 결과 : 원의 넓이는 310입니다

# global 키워드
pi = 3.14

# 원의 넓이 계산
def circle_area(r) :
    global pi
    area = r * r * pi               # 원 넓이 계산
    return area

result = circle_area(10)
print(f"원의 넓이는{result}입니다")  # 원의 넓이는 314입니다


# ==================================
# lambda
add = lambda x, y : x + y   # add에 lambda 함수를 저장
                            # 입력값(매개변수) : 반환할 값
print(add(10, 5))           # 10 + 5 → 15


# 짝수 / 홀수 판별
# 조건이 참 → 값1 / 조건이 거짓 → 값2
is_even = lambda x : "짝수" if x % 2 == 0 else "홀수"  # 2 % 2 = 0 
print(is_even(2))                                      # 0 == 0 → True (짝수)

is_even = lambda x : "짝수" if x % 2 == 0 else "홀수"   # 9 % 2 = 1
print(is_even(9))                                      # 1 == 0 → False (홀수)


grade = lambda x : "A" if x >= 90 else ("B" if x >= 80 else "C")  # 95 >= 90 → True
print(grade(95))                                                  # A


# ==================================
# 예외 처리 (try-except)

try:
    # 사용자에게 인원 수 입력 받기
    # input()은 문자열로 입력되기 때문에
    # int로 형변환
    a = int(input("인원을 입력하세요"))

    # 사용자에게 금액 입력 받기
    b = int(input("금액을 입력하세요"))

    # 한 사람당 나눌 금액 계산
    c = b / a


# ==================================

# 숫자가 아닌 값을 입력했을 때 발생하는 오류
except ValueError:
    print("숫자를 입력하세요")

# 0으로 나눴을 때 발생하는 오류
except ZeroDivisionError as e:
    print(f"{e}, 0으로 나눌 수 없습니다.")

# 그 외 모든 오류 처리
except Exception as e:
    print(f"에러, {e}")

# try문에서 오류가 발생하지 않았을 때 실행
else:
    # 정상적으로 계산되었을 때 결과 출력
    print(f"한사람당 {c}원씩 나누면 됩니다.")

# 예외 발생 여부와 상관없이 항상 실행
finally:
    print("계산이 완료 되었습니다")
    
    
# ==================================
# 파일 오픈

# 현재 실행 폴더에서 "output.txt" 파일을 읽기 모드로 열기
try:
    f = open("output.txt", "r")

# 파일이 없거나 접근 불가할 때 발생하는 오류 처리
except Exception as e :
    print(f"에러, {e}")

# 파일이 정상적으로 열렸을 때 실행
else:
    print("파일 열기 설공")
    f.close()


# ==================================
# 사용자 정의 예외 발생 (raise)

# 나이가 0보다 작으면 비정상적인 값
def set_age(age):
    if age < 0 :
        raise ValueError("나이는 0 이상이어야 합니다.")
    
    # 정상적인 값일 경우 실행
    return f"당신의 나이는 {age} 살 입니다."

print(set_age(3))
    

# ==================================
