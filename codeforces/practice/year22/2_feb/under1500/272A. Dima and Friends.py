n = int(input()) + 1
data = list(map(int, input().split()))
cnt = 0
for i in range(1, 6):
    if (sum(data) + i + n - 1) % n + 1 != 1:
        cnt += 1

print(cnt)