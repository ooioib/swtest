# ========== 리스트(list) ==========
# 생성
data1 = []
data2 = [1, 2, 3, 4, 5]
data3 = ['henry', 'max', 'tom']    # 순서를 가짐
data4 = ['henry', 24, 178.5, True]


# 요소 추가
# .append(추가할 요소)
# .insert(위치, 추가할 요소)
data3.append('ben')
data3.insert(1, 'jin') # 1번째 위치에 'jin' 추가
print(data3)


# 수정
data3[0] = 'HENRY'  # 대문자로 변경
print(data3)


# 삭제
# .remove(삭제할 요소)
# .pop(삭제할 인덱스)
# .clear()
data3.remove('HENRY')
print(data3)

data3.pop(0)
print(data3)

data3.clear()
print(data3)


# ========== 튜플(tuple) ==========
# 생성
t1 = ()
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, )   # 데이터가 하나 있는 튜플
t5 = ('herny', 25, False)

# 요소 추가, 삭제, 수정 불가능
#t5[0] = 'HENRY'
print(t5[0])

fruit = ('apple', 'banana', 'orange')
a, b, c = fruit # unpacking
print(a, b, c)

a, *b = fruit
print(a, b)


# ========== 딕셔너리(dictionary) ==========
d1 = {}
d2 = {'이름' : '철수', '나이' : 39, '결혼유무' : False, '몸무게' : 56.7} 

# 값 추출
print(d2['이름'])  # 순서가 없음

# 추가 / 수정
# 딕셔너리['추가할 키'] = '추가할 값'
# 키 값이 이미 있으면 update, 없으면 추가
d2['이름'] = '영희'     # update
d2['취미'] = '노래'     # 추가
print(d2)

# 삭제
d2.pop('이름')  # 이름 삭제
print(d2)       

#d2.clear()     # 전부 삭제
#print(d2)

# items / keys / values
print(d2.items())   # key-value를 리스트 형태로 한 쌍으로 가져옴
print(d2.keys())    # 리스트 형태로 key 값만 가져옴
print(d2.values())  # 리스트 형태로 value 값만 가져옴

