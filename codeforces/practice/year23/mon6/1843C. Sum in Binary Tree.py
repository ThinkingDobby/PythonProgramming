import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    cnt = 0
    while n > 0:
        cnt += n
        n //= 2

    print(cnt)