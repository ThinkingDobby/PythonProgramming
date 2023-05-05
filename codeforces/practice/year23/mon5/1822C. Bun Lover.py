import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = n * n + 10 + 2 * (n - 4)
    print(ans)