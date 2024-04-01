import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    cnt = 0
    for i in range((n - 1) // 2 + 1, n):
        if data[(n - 1) // 2] == data[i]:
            cnt += 1

    print(cnt + 1)