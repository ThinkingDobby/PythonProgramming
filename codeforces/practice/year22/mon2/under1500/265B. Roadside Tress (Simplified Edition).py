n = int(input())
data = [int(input()) for i in range(n)]
cnt = data[0] + 1
for i in range(1, n):
    if data[i - 1] <= data[i]:
        cnt += data[i] - data[i - 1] + 2
    else:
        cnt += data[i - 1] - data[i] + 2

print(cnt)