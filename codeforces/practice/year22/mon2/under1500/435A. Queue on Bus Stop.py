n, m = map(int, input().split())
data = list(map(int, input().split()))

i = 0
cnt = 0
s = 0
while i < n:
    s += data[i]
    if s <= m:
        i += 1
    else:
        cnt += 1
        s = 0

if s != 0 and s <= m:
    cnt += 1

print(cnt)
