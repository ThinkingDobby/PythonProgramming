import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) + [i] for i in range(n)]
    ans = sorted([i for i in data if i[0] <= 10], key=lambda x: x[1])[-1][2]

    print(ans + 1)