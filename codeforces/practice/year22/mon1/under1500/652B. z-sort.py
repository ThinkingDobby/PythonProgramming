n = int(input())
data = list(map(int, input().split()))
sdata = sorted(data)
a = sdata[:(n + 1) // 2]
b = sdata[(n + 1) // 2:]
for i in range((n + 1) // 2):
    print(a[i], end=' ')
    if i < len(b):
        print(b[i], end=' ')