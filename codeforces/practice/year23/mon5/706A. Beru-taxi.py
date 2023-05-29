import math
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
mv = math.inf
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    ans = math.sqrt((a - x)**2 + (b - y)**2) / z
    mv = min(mv, ans)

print(mv)