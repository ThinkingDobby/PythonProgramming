n, k = map(int, input().split())
data = [int(input()) for i in range(n)]
memo = [0] * k
for i in data:
    memo[i - 1] += 1

s = 0
cnt = (n + 1) // 2
for i in memo:
    s += i // 2 * 2
    cnt -= i // 2
print(cnt + s)