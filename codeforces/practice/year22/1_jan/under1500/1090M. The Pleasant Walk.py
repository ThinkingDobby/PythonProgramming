n, k = map(int, input().split())
data = [0] + list(map(int, input().split()))

cnt = 0
mv = 0
for i in range(1, n + 1):
    if data[i - 1] != data[i]:
        cnt += 1
    else:
        mv = max(mv, cnt)
        cnt = 1

mv = max(mv, cnt)
print(mv)