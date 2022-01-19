n = int(input())
data = list(map(int, input().split()))

cnt = 0
for i in range(1, n - 1):
    if data[i] == 0 and data[i - 1] == data[i + 1] == 1:
        cnt += 1
        data[i + 1] = 0

print(cnt)