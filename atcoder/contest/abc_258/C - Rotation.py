import sys

input = sys.stdin.readline

n, q = map(int, input().split())
data = input().rstrip()

tmp = 0
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        tmp += x
    else:
        if x - 1 - tmp < 0:
            print(data[-((abs(x - 1 - tmp) + n - 1) % n + 1)])
        else:
            print(data[x - 1 - tmp])