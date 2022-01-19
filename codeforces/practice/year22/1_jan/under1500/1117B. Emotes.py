n, m, k = map(int, input().split())
data = sorted(map(int, input().split()), reverse=True)

tmp = m // (k + 1)
print((m - tmp) * data[0] + tmp * data[1])
