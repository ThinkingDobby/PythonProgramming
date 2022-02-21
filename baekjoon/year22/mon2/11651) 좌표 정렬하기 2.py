import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
ans = sorted(data, key=lambda x: [x[1], x[0]])
for i in ans:
    print(*i)