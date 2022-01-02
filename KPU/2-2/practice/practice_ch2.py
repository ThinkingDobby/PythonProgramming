# 1
input = {'국어':80, '영어':75, '수학':55}
print(sum(input.values()) / len(input))

# 2
a = True if 13 % 2 == 0 else False
if a:
    print("Even")
else:
    print("Odd")

# 3
input = "881120-1068234"
for i in input.split("-"):
    print(i, end = ' ')
print()

# 4
pin = "881120-1068234"
print(pin[pin.index("-") + 1])

# 5
a = "a:b:c:d"
print(a.replace(":", "#"))

# 6
input = [1, 3, 5, 4, 2]
input.sort()
print(input)

# 7
input = ['Life', 'is', 'too', 'short']
print(" ".join(input))

# 8
input = (1, 2, 3)
print(input + (4,))

# 9
# 3 : 리스트는 가변 값이므로 키가 될 수 없음

# 10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

# 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))

# 12
# b 값도 변경된다.
# a의 주소와 b의 주소가 동일하기 때문