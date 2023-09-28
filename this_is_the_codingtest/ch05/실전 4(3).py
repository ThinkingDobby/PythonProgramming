import collections
import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(input().rstrip()) for _ in range(n)]
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

dq = collections.deque()
dq.append([0, 0])

memo = [[math.inf] * m for _ in range(n)]
memo[0][0] = 1

while dq:
    r, c = dq.popleft()

    for a, b in dirs:
        if 0 <= r + a < n and 0 <= c + b < m and data[r + a][c + b] == '1' and memo[r + a][c + b] == math.inf:
            dq.append([r + a, c + b])
            memo[r + a][c + b] = min(memo[r + a][c + b], memo[r][c] + 1)

print(memo[n - 1][m - 1])

"""
5 6
101010
111111
000001
111111
111111
"""