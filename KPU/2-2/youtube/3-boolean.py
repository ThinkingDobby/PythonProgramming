a = True
print(type(a))

# 빈 자료구조, 빈 문자열, None -> False
# 반대 -> True

b = "Hi"
if b:
    print(b)

a = [1, 2, 3, 4]
while a:
    print(a)
    a.pop()