import sys

inp = sys.stdin.readline

n, q = map(int, input().split())
data = list(map(int, input().split()))
ones = data.count(1)
for _ in range(q):
    x, k = map(int, inp().rstrip().split())
    if x == 1:
        if data[k - 1] == 1:
            data[k - 1] = 0
            ones -= 1
        else:
            data[k - 1] = 1
            ones += 1
    else:
        if k <= ones:
            print(1)
        else:
            print(0)