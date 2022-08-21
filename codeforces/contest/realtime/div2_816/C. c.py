import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

tot = (n * (n + 1) * (2 * n + 1) + 3 * n * (n + 1)) // 12
for i in range(1, n):
    if data[i - 1] == data[i]:
        tot -= i * (n - i)

for _ in range(m):
    i, x = map(int, input().split())

    if data[i - 1] != x:
        if i > 1 and data[i - 2] == x:
            tot -= (i - 1) * (n - i + 1)
        if i < n and x == data[i]:
            tot -= i * (n - i)

        if i > 1 and data[i - 2] == data[i - 1] and data[i - 2] != x:
            tot += (i - 1) * (n - i + 1)
        if i < n and data[i - 1] == data[i] and x != data[i]:
            tot += i * (n - i)

        data[i - 1] = x

    print(tot)
