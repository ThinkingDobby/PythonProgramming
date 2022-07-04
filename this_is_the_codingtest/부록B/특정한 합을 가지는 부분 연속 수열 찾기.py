n, m = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        if s + data[j] > m:
            break
        s += data[j]
        if s == m:
            cnt += 1
            break

print(cnt)