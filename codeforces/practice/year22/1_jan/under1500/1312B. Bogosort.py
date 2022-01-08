import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    n = int(inp())
    data = sorted(map(int, inp().split()), reverse=True)
    print(*data)