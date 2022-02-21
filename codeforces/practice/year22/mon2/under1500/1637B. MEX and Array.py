import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    cnt = 0
    for i in range(1, n + 1):
        for j in [data[l:l + i] for l in range(n - i + 1)]:
            cnt += j.count(0) * 2 + i - j.count(0)
    print(cnt)