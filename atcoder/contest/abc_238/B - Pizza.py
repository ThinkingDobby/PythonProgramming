n = int(input())
data = list(map(int, input().split()))
for i in range(n - 1):
    data[i] += sum(data[i + 1:])
    if data[i] >= 360:
        data[i] %= 360

sdata = sorted(data)
mv = 0
for i in range(1, n):
    mv = max(mv, sdata[i] - sdata[i - 1])
mv = max(mv, 360 - sdata[-1], sdata[0])

print(mv)