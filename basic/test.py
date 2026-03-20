# ========== 표준 출력 함수 print ==========

# 기본형
print("hello")  # 문자열은 따옴표("") 사용
print(1)        # 숫자


# 여러개의 자료를 동시에 출력
# 콤마(,) 사용
print("hi", 1)          


# 특수 문자 사용
print("안녕\n반가워")   # \n : 줄바꿈
print("안녕\t반가워")   # \t : 탭만큼 띄우기


# f-string 사용
# 문자열 안에 변수나 표현식을 직접 넣어서 출력
name = "경기"  
age = 50       
print(name)
print(f"내 이름은 {name}야.")

# format : {}에 변수 값이 순서대로 들어감
print("내 이름은 {}야. 그리고 나이는 {}이야.".format(name, age))