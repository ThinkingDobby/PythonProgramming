import sys

MAX = sys.maxsize

n, x, y = map(int, input().split())
data = [MAX] * x + list(map(int, input().split())) + [MAX] * y

for i in range(x, n + x):
    if min(data[i - x:i + y + 1]) == data[i]:
        print(i + 1 - x)
        break
