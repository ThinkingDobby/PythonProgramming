# 1
# "shirt"

# 2
sum = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        sum += i
    i += 1
print(sum)

# 3
i = 0
while i < 5:
    print("*" * (i + 1), end='')
    print()
    i += 1


# 4
for i in range(1, 101):
    print(i, end=' ')
print()


# 5
input = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in input:
    sum += i
print(sum / len(input))

# 6
numbers = [1, 2, 3, 4, 5]
result = [num * 2 for num in numbers if num % 2 == 1]
print(result)