n, k = map(int, input().split())
tmp = 1
cnt = 0

while True:
    if tmp * k > n: break
    tmp *= k
    cnt += 1
print(n - tmp + cnt)
