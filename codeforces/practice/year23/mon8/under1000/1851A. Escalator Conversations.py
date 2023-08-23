import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k, H = map(int, input().split())
    h = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        tmp = abs(H - h[i])
        if tmp != 0 and tmp % k == 0 and tmp // k < m:
            cnt += 1

    print(cnt)