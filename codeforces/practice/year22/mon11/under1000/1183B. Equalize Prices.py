import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    l = data[0] - k
    r = data[0] + k

    ans = True
    for i in range(1, n):
        if r < data[i] - k or l > data[i] + k:
            ans = False

        l = max(l, data[i] - k)
        r = min(r, data[i] + k)

    print(-1 if not ans else r)
