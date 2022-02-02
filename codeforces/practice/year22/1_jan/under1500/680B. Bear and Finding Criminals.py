n, a = map(int, input().split())
data = [0] + list(map(int, input().split()))

cnt = 0
for i in range(min(a, n - a + 1)):
    if data[a - i] == data[a + i] == 1:
        cnt += 1 if i == 0 else 2

if a > n - a + 1:
    cnt += data[:a - (n - a + 1) + 1].count(1)
else:
    cnt += data[a * 2:].count(1)

print(cnt)