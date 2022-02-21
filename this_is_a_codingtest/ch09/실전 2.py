import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[math.inf] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = graph[1][k] + graph[k][x]
if ans == math.inf:
    print(-1)
else:
    print(ans)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""

"""
4 2
1 3
2 4 
3 4
"""