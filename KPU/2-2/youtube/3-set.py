# 순서 없음, 중복되는 요소 없음

#s1 = set([1, 2, 3])
a = {1, 2, 3}

b = set("Hello")   # 문자열도 변환 가능
print(b)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)  # 교집합
print(s1.intersection(s2))  # 코틀린 s1.intersect(s2)
print(s1 | s2)  # 합집합
print(s1.union(s2)) # 코틀린과 동일
print(s1 - s2)  # 차집합
print(s1.difference(s2))    # 코틀린 s1.subtract(s2)

a.add(4)    # list는 append, set은 add
print(a)
a.update([1, 2, 7, 8, 9])   # list는 update 사용 불가
print(a)
a.update({9, 10})   # set은 iterable로 update 가능
print(a)
a.remove(7)
print(a)