import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    cnt = 0
    mv = data[-1]
    for i in range(n - 2, -1, -1):
        if data[i] > mv:
            mv = data[i]
            cnt += 1

    print(cnt)
