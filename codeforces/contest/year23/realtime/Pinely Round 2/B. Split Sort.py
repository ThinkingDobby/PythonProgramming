import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    chk = [False] * (n + 1)

    cnt = 0
    for i in range(n):
        chk[data[i]] = True
        if not chk[data[i] - 1]:
            cnt += 1

    print(cnt - 1)