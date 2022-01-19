# 미완성

n, l, k = map(int, input().split())
d = list(map(int, input().split())) + [l]
a = list(map(int, input().split()))

# mv = a[0]
# memo = [0] * n
s = a[0] * (d[1] - d[0])
#
# print(s - sum(sorted(memo, reverse=True)[:k]))

memo = [[0] * i for i in range(n, 0, -1)]
for t in range(1, n + 1):
    for i in range(1, n + 1 - t):
        tmp = 0
        for j in range(i, i + t):
            if t == 1:
                s += a[i] * (d[i + 1] - d[i])
            tmp += (a[j] - a[i]) * (d[i + 1] - d[i])
        memo[t - 1][i] = tmp

print(memo)
