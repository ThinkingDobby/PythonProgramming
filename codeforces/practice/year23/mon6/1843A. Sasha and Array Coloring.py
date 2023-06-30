import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    ans = sum(data[(n + 1) // 2:]) - sum(data[:n // 2])
    print(ans)