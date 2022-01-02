# 주석은 코틀린에서 동일 기능을 수행하는 함수

a = [3, 2, 1]
print(a)
a.append(0) # a.add(0)
print(a)

a.sort()
print(a)

b = [(4, 3), (1, 3), (1, 2)]
print([i for j in b for i in j])
b = sorted(b, key = lambda x : (x[0], -x[1]))
print(b)

a.reverse()
print(a)
print(a.index(2))   # a.indexOf(2)

a.insert(0, 4)  # a.add(0, 4)
print(a)

a.remove(4)
print(a)

print(a.pop())
print(a)

print(a.count(3))   # a.count{it == 3}

print(*a)   # 리스트 요소 언패킹
