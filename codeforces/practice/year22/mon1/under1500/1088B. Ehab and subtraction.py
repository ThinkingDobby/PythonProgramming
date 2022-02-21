n, k = map(int, input().split())
data = list(map(int, input().split()))
sdata = sorted(set(data))

print(sdata[0])
for i in range(1, min(k, len(sdata))):
    print(sdata[i] - sdata[i - 1])

for i in range(k - len(sdata)):
    print(0)