n = int(input())
data = list(map(int, input().split()))
s = data[-1]
prev = data[-1]
for i in range(n - 2, -1, -1):
    prev = min(prev - 1, data[i])
    s += max(0, prev)
print(s)