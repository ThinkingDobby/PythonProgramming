# 1
input = [80, 75, 55]
avg = sum(input) / len(input)
print(avg)

# 2
input = 13
ans = input % 2
if ans == 1:
    print("odd")
else:
    print("even")

# 3
input = "881120-1068234"
print(input[0: input.find('-')], end = ' ')
print(input[input.find('-') + 1:])
#print(input.split("-"))

#4
pin = "881120-1068234"
print(pin[pin.find('-') + 1])

#5
a = "a:b:c:d"
print(a.replace(':', '#'))

#6
input = [1, 3, 5, 4, 2]
input.sort()
input.reverse()
print(input)

#7
input = ['Life', 'is', 'too', 'short']
print(" ".join(input))

# 8
input = (1, 2, 3)
new = input + (4, )
print(new)

# 9
# dictionary의 키로는 가변 값 넣을 수 없음
# 3번의 리스트는 가변 값이므로 오류 발생

# 10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

# 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)
print(b)

# 12
# 바뀜, 변수에 리스트의 주소가 저장되기 때문