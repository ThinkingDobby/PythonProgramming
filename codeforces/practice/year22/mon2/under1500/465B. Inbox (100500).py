n = int(input())
data = list(map(int, input().split())) + [0]

cnt = 0
for i in range(1, n + 1):
    if data[i - 1] == 1 and data[i] == 0:
        cnt += 1

print(max(0, cnt + data.count(1) - 1))