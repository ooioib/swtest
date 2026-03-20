# 문자열 함수
data = "python is programming language"
print(data.count('p'))             # 개수
print(data.find('p'))              # 위치 (없으면 -1)
print(data.index('p'))             # 위치 (없으면 오류)
print(data.replace('python', 'c')) # 문자열 변경

data2 = " henry, 010-1234-5678 "
print(data2.strip())       # 문자열의 양쪽 공백 제거
print(data2.split(','))    # 콤마 기준으로 문자열을 나눠 리스트로 반환
