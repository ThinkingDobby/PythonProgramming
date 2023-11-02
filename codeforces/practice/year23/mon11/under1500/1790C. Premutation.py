import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    f_memo = collections.defaultdict(int)

    for i in data:
        f_memo[i[0]] += 1
        if f_memo[i[0]] > 1:
            f = i[0]
            break

    for i in data:
        if i[0] != f:
            print(*([f] + i))
            break
