import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    n = int(inp())
    data = list(map(int, inp().split()))

    for i in range(1, n):
        if data[i - 1] > 0:
            data[i] += data[i - 1]
            data[i - 1] = 0

    print(data[-1])