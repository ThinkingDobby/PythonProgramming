import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ans = [-1] * n
    ans[0] = 501

    for i in range(n - 1):
        ans[i + 1] = ans[i] + data[i]

    print(*ans)