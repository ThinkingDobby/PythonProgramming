import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    memo = [0] * k
    for i in range(n):
        memo[i % k] = max(memo[i % k], data[i])

    print(sum(memo))
