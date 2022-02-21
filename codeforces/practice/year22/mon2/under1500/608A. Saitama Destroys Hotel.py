n, s = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)] + [[0, 0]]
data.sort(reverse=True)

now = max(s - data[0][0], data[0][1])
for i in range(1, n + 1):
    now = max(now + data[i - 1][0] - data[i][0], data[i][1])

print(now)