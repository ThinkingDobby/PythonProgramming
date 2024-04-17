import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    memo = [data[0], data[-1], data[1], data[-2]]
    ans = abs(memo[0] - memo[1]) + abs(memo[1] - memo[2]) + abs(memo[2] - memo[3]) + abs(memo[3] - memo[0])

    print(ans)