memo = []
i = 0
while True:
    tmp = int('1' * (i + 1) + '0' * i, 2)
    if tmp > 10**5:
        break
    memo.append(tmp)
    i += 1

n = int(input())
for i in memo[::-1]:
    if i <= n and n % i == 0:
        print(i)
        break
