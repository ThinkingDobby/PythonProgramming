m = list(map(int, input().split()))
w = list(map(int, input().split()))
x = [500, 1000, 1500, 2000, 2500]
hs, hu = map(int, input().split())

s = hs * 100 - hu * 50
for i in range(5):
    tmp = max(int(0.3 * x[i]), x[i] - m[i] * x[i] // 250 - 50 * w[i])
    s += tmp

print(s)