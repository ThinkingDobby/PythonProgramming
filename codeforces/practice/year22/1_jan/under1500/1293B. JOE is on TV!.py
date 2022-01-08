import sys
inp = sys.stdin.readline

s = 0
for i in range(1, int(inp()) + 1):
    s += 1 / i

print(s)