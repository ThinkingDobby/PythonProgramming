import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    data = list(map(int, input().split()))

    memo = [0] * n
    memo[0] = data[0]

    for i in range(1, n):
        memo[i] = data[i] + memo[i - 1]

    sv = memo[-1]

    for _ in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        r -= 1

        f = memo[r]
        s = memo[l - 1] if l > 0 else 0

        tmp = sv - (f - s) + k * (r - l + 1)
        print("YES" if tmp % 2 == 1 else "NO")
