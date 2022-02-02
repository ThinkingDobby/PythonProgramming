n, x = map(int, input().split())
data = set(map(int, input().split()))
cnt = 0
for i in range(0, x):
    if i not in data:
        cnt += 1

if x in data:
    cnt += 1

print(cnt)