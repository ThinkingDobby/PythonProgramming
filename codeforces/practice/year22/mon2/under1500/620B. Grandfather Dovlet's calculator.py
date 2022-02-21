a, b = map(int, input().split())
memo = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
s = 0
for i in range(a, b + 1):
    tmp = i
    while tmp:
        s += memo[tmp % 10]
        tmp //= 10

print(s)