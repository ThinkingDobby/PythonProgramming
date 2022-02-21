n = int(input())
s = 0

while True:
    s += n
    flag = False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            flag = True
            n //= i
            break
    if not flag:
        s += 1
        break

print(s)