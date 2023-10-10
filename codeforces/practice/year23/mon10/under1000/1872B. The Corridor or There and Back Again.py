import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    ans = min(map(lambda x: x[0] + (x[1] - 1) // 2, data))
    print(ans)