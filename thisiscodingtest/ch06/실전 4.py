n, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)

s = 0
for i in range(n):
    if a[i] < b[i] and k:
        s += b[i]
        k -= 1
    else:
        s += a[i]

print(s)