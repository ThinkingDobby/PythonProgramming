import math
import sys

input = sys.stdin.readline

n = int(input())
data = [input().rstrip() for _ in range(n)]

ans = 0
for i in range(n):
    cnt = data[i].count('C')
    tmp = 0
    for j in range(n):
        tmp += 1 if data[j][i] == 'C' else 0
    ans += math.comb(cnt, 2) + math.comb(tmp, 2)

print(ans)