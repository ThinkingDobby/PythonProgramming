import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(input().split())

    memo = []
    for i in data:
        if len(i) == n - 1:
            memo.append(i)

    if memo[0][1:] == memo[1][:-1]:
        tmp = memo[0] + memo[1][-1]
    else:
        tmp = memo[1] + memo[0][-1]

    print("YES" if tmp == tmp[::-1] else "NO")