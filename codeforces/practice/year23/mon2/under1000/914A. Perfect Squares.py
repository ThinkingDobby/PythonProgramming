import math
import sys

input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()), reverse=True)

ans = -1
for i in range(n):
    if data[i] < 0:
        ans = i
        break
    tmp = int(math.sqrt(data[i]))
    if tmp * tmp != data[i]:
        ans = i
        break

print(data[ans])
