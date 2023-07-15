import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = {}
    for i in range(n):
        memo[data[i]] = i

    mv = -1
    rmv = -1
    for i in range(1, n):
        mv = max(mv, memo[data[i - 1]])
        if i - 1 <= rmv or data[i - 1] > data[i]:
            rmv = mv

    tmp = [i for i in memo.values() if i <= rmv]
    print(len(tmp))
