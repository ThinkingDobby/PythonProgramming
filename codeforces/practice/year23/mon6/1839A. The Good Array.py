import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = (n + k - 1) // k + (1 if (n + 1) % k != 0 else 0)
    print(ans)