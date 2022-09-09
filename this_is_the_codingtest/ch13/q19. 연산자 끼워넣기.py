import math
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
ops = list(map(int, input().split()))

min_v = math.inf
max_v = -math.inf


def dfs(s, idx):
    global min_v, max_v
    if idx == n:
        min_v = min(min_v, s)
        max_v = max(max_v, s)
        return
    for i in range(4):
        if ops[i]:
            ops[i] -= 1
            dfs(opchk(i, s, data[idx]), idx + 1)
            ops[i] += 1


def opchk(i, a, b):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    else:
        return a // b if a >= b else -(abs(a) // b)


dfs(data[0], 1)

print(max_v)
print(min_v)
