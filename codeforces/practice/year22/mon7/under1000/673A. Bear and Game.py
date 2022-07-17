import sys

input = sys.stdin.readline

n = int(input())
data = [0] + list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    if data[i - 1] + 15 >= data[i]:
       ans = data[i]
    else:
        break

print(min(ans + 15, 90))



