import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    ans = 0
    for i in range(1, n):
        ans += data[i] - data[i - 1]

    print(ans)