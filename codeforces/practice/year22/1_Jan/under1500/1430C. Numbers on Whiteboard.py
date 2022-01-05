import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    n = int(inp())
    print(2)
    if n == 2:
        print(1, 2)
    else:
        print(n - 2, n)
        print(n - 1, n - 1)
    for i in range(n - 3, 0, -1):
        print(i, i + 2)
