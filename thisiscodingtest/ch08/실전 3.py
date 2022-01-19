n = int(input())
data = list(map(int, input().split()))
data[2] += data[0]

for i in range(3, n):
    data[i] += max(data[i - 2], data[i - 3])


print(max(data[n - 2], data[n - 1]))