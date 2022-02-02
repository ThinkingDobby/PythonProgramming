n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

now = 0
start = 1
end = a[now]

i = 0
while i < m:
    if start <= b[i] <= end:
        print(now + 1, b[i] - start + 1)
    else:
        now += 1
        start = end + 1
        end += a[now]
        continue
    i += 1