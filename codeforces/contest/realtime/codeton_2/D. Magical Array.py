import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    memo_tot = set()
    idxs = dict()
    for i in range(n):
        memo = [0] * m
        for j in range(m):
            memo[j] = data[i][j] * (j + 1)
        memo_tot.add(sum(memo))
        idxs[sum(memo)] = i

    memo_tot = sorted(memo_tot)
    print(idxs[memo_tot[1]] + 1, memo_tot[1] - memo_tot[0])
