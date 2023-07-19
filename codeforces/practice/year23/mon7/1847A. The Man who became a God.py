import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    memo = sorted([abs(data[i] - data[i - 1]) for i in range(1, n)], reverse=True)
    ans = sum(memo[k - 1:])
    print(ans)
