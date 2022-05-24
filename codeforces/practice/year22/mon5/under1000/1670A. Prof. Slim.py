import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    cnt = len([i for i in data if i < 0])

    ans = True
    for i in range(1, cnt):
        if abs(data[i - 1]) < abs(data[i]):
            ans = False
            break

    for i in range(cnt + 1, n):
        if abs(data[i - 1]) > abs(data[i]):
            ans = False
            break

    print("YES" if ans else "NO")