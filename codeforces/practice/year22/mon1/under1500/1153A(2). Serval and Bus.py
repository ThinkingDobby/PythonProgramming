n, t = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]

memo = [0] * n
for i in range(n):
    s, d = data[i]
    if s >= t:
        memo[i] = s - t
    else:
        memo[i] = (s - t) % d

print(memo.index(min(memo)) + 1)