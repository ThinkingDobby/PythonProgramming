import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = [False for _ in range(m + 1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in tmp[1:]:
        memo[j] = True

print("YES" if all(memo[1:]) else "NO")