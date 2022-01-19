n, L, a = map(int, input().split())
memo = []
for i in range(n):
    t, l = map(int, input().split())
    memo.append([t, t + l])

cnt = ((memo[0][0] if n > 0 else 0) - 0) // a
for i in range(1, n):
    cnt += (memo[i][0] - memo[i - 1][1]) // a
cnt += (L - (memo[-1][1] if n > 0 else 0)) // a

print(cnt)