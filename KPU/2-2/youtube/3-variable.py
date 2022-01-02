# 파이썬 변수는 객체의 주소를 저장함 (파이썬의 모든 것은 객체)
# -> 단순하게 생각할 것. c의 포인터 개념과 유사 -> 배열 복사 시에만 주의
a = [1, 2, 3]
b = a   # 얕은 복사
b[1] = 0
print(a)
print(id(a))
print(id(b))
print(a is b)   # 주소 비교

c = [1, 2, 3]
d = c[:]    # 깊은 복사
d[1] = 0    # 코틀린: 복사 대상에 toMutableList() 등 명시하면 복사
print(c)    # (ex) a, b가 Mutable List인 경우 val b = a.toMutableList()
print(id(c))
print(id(d))
print(c is d)

from copy import copy
e = [1, 2, 3]
f = copy(e) # 깊은 복사
print(e)
print(id(e))
print(id(f))
print(e is f)

(a, b) = ('python', 'life') # 자료구조 이용해 변수 할당
print(a)
print(b)

[a, b] = ('python', 'life')
print(a)
print(b)

a = b = 3
print(a)
print(b)

a = 3
b = 5
a, b = b, a # swap 단순화
print(a)
print(b)