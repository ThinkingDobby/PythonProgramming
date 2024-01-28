import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, f, a, b = map(int, input().split())
    m = [0] + list(map(int, input().split()))

    tot = 0
    cnt = 0
    ans = False
    for i in range(1, n + 1):
        tot += min((m[i] - m[i - 1]) * a, b)
        if tot >= f:
            break

        cnt += 1
        if cnt >= n:
            ans = True
            break

    print("YES" if ans else "NO")