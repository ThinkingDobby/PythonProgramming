a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][2])

print(a * 3)
print(a[::-1])  # 문자열과 slice 동일


b = ['a','b','c']
print(b)
del(b[0])   # 항목 삭제
print(b)
print(b[0])
b.remove('c')
print(b)