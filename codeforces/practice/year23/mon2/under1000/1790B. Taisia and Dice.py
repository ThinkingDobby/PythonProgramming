import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, r = map(int, input().split())

    print(*([s - r] + [r // (n - 1) + 1] * (r % (n - 1)) + [r // (n - 1)] * (n - 1 - (r % (n - 1)))))
