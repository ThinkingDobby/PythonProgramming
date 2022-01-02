import sys

for t in range(int(input())):
    n = int(input())
    memo = [0 for _ in range(n)]
    rmemo = []
    for i in range(n):
        a, b = map(lambda x: int(x) - 1, input().split(" "))
        for j in range(a, b + 1):
            memo[j] += 1
        rmemo.append((a, b))
    for i in range(n):
        a, b = rmemo[i]
        idx = memo[a:b + 1].index(min(memo[a:b + 1]))
        print(a + 1, b + 1, idx + a + 1)
        memo[idx + a] = sys.maxsize
