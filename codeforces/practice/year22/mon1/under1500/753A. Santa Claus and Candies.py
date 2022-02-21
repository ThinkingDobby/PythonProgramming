n = int(input())
s = 0
idx = -1
for i in range(1, n + 1):
    s += i
    if s > n:
        break
    idx = i

print(idx)
for i in range(1, idx):
    print(i, end=' ')

if n == 1:
    print(1)
else:
    print(n - (s - 2 * idx - 1))