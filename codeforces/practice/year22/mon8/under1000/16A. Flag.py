import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = [-1] * n

data = [list(map(int, list(input().rstrip()))) for _ in range(n)]

tmp = data[0]
if len(set(tmp)) == 1:
    memo[0] = tmp[0]
    ans = True
    for i in range(1, n):
        tmp = data[i]
        if len(set(tmp)) != 1 or tmp[0] == memo[i - 1]:
            ans = False
            break
        memo[i] = tmp[0]
    print("YES" if ans else "NO")
else:
    print("NO")
