n = int(input())

d = [1] * (n + 1)
for i in range(2, n + 1):
    d[i] = (d[i - 2] % 796796 * 2 + d[i - 1] % 796796) % 796796

print(d[n])