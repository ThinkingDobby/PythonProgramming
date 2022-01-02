# 1
# shirt

# 2
s = 0
now = 1
while now <= 1000:
    if now % 3 == 0:
        s += now
    now += 1
print(s)

print(sum([i for i in range(1001) if i % 3 == 0]))

# 3
i = 1
while i < 6:
    print("*" *  i, end = ' ')
    print()
    i += 1

# 4
for i in range(1, 101):
    print("%2d" % i, end=' ')
    if i % 10 == 0:
        print()

# 5
input = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in input:
    sum += i
print(sum / len(input))

# 6
numbers = [1, 2, 3, 4, 5]
result = [i * 2 for i in numbers if i % 2 == 1]
print(result)