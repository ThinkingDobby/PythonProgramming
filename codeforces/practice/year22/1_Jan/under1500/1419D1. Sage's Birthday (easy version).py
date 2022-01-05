import sys
inp = sys.stdin.readline

n = int(inp())
data = sorted(map(int, inp().split()))
cnt = 0
print((n - 1) // 2)
for i in range(n // 2, n):
    print(data[i], end=' ')
    if cnt < n // 2:
        print(data[cnt], end=' ')
        cnt += 1