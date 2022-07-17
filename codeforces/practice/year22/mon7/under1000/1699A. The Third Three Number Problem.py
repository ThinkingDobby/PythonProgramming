import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n % 2 == 1:
        print(-1)
    else:
        tmp = bin(n)[2:]
        if tmp == '1':
            t = 0
        else:
            t = int('1' * (len(tmp) - 1), 2)
        print(t, t, t ^ (n // 2))