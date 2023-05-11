import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if (i + 1 - data[i]) % k != 0:
            cnt += 1

    if cnt == 0:
        print(0)
    else:
        print(-1 if cnt > 2 else 1)