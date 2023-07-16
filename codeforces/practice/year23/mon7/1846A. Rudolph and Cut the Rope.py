import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    ans = len([i for i in range(n) if data[i][0] > data[i][1]])
    print(ans)