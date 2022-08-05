import sys

input = sys.stdin.readline

n = int(input())
data = [input().rstrip() for _ in range(n)]

p_len = len(data[0])
for i in range(1, n):
    for j in range(p_len):
        if data[i][j] != data[i - 1][j]:
            p_len = j + 1
            break

print(p_len - 1)
