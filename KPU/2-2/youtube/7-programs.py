def gugu(num):
    result = []
    for i in range(1, 10):
        result.append(num * i)
    return result

result = gugu(2)
print(result)


def calcSum(num):
    i = 1
    sum = 0
    while i <= num:
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        i += 1
    return sum

print(calcSum(1000))


def getTotalPage(m, n):
    return (m + n - 1) // n

print(getTotalPage(25, 10))