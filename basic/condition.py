# ========== 조건문 ==========
score = 90

if score >= 80:
    print('A')
elif score >= 60:
    print('B')
else :
    print('C')


# 주민번호를 가지고 있는 id에서 성별을 분석하여
# 남성, 여성으로 출력하세요.
id = '123456-3******'
gender = id[7]

if gender == '1' or gender =='3':
    print('남성')
elif gender == '2' or gender =='4':
    print('여성')
else:
    print('오류가 발생하였습니다.')


id = '123456-3******'

if id[7] == '1' or id[7] =='3':
    print('남성')
elif id[7] == '2' or id[7] =='4':
    print('여성')
else:
    print('오류가 발생하였습니다.')



# 날짜가 짝수면 "짝수 번호 차량 통행 가능"
# 날짜가 홀수면 "홀수 번호 차량 통행 가능"
date = "2026-03-13"
num = int(date.split('-')[2])

if num % 2 == 0:
    print("짝수 번호 차량 통행 가능")

else:
    print("홀수 번호 차량 통행 가능")


# 구매 금액 + 배송비(3,000원), 50,000원 이상은 무료배송
# 총 결제 금액 출력
# 조건 if만 사용
price = 25000

if price < 50000:
    price = price + 3000
    
    print(f"결제금액 : {price}")


