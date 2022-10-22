import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [input().split() for _ in range(3)]

    chk = [0] * n
    v = [1, 2, 4]

    memo = collections.defaultdict(int)

    for i in range(3):
        for j in data[i]:
            memo[j] += v[i]

    ans = [0] * 3
    for i in memo.values():
        if i == 1:
            ans[0] += 3
        elif i == 2:
            ans[1] += 3
        elif i == 4:
            ans[2] += 3
        elif i == 3:
            ans[0] += 1
            ans[1] += 1
        elif i == 5:
            ans[0] += 1
            ans[2] += 1
        elif i ==6:
            ans[1] += 1
            ans[2] += 1

    print(*ans)


