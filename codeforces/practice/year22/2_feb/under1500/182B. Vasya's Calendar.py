d = int(input())
n = int(input())
data = list(map(int, input().split()))

s = 0
for i in range(1, n):
    s += d - data[i - 1]
print(s)