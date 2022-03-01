n = int(input())
data = list(map(int, input()))

cnt = data.count(8)
mv = 0
for i in range(1, cnt + 1):
    mv = max(min((n - i) // 10, i), mv)
print(mv)