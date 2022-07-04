import math
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

mv = math.inf
ans = math.inf
basic = 0

for i in range(n):
    basic += data[i][0] + data[i][1]
    mv = min(mv, data[i][1])
    ans = min(ans, basic + mv * (x - (i + 1)))

print(ans)