import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    ans = True
    cnt = 0
    for i in range(n - 1, 0, -1):
        if data[i] == 0:
            ans = False
            break
        while data[i - 1] >= data[i]:
            data[i - 1] //= 2
            cnt += 1

    print(cnt if ans else -1)
