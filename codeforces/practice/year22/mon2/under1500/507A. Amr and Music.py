n, k = map(int, input().split())
data = sorted(enumerate(map(int, input().split())), key=lambda x:x[1])
s = 0
idx = -1
for i in range(n):
    if s + data[i][1] > k:
        break
    s += data[i][1]
    idx = i

print(idx + 1)
for i in range(idx + 1):
    print(data[i][0] + 1, end=' ')