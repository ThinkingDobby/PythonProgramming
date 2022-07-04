n, m, k = map(int, input().split(" "))
data = sorted(list(map(int, input().split(" "))))

tmp = (m // (k + 1))
print(data[-1] * (m - tmp) + data[-2] * tmp)