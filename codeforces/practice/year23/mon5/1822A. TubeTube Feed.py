import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    now = 0
    mv = -1
    midx = -1
    for i in range(n):
        if now + a[i] <= t:
            if mv < b[i]:
                mv = b[i]
                midx = i + 1
        now += 1

    print(midx)
