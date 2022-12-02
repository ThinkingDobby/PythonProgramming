import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = collections.defaultdict(int)
    mv = min(data)
    for i in data:
        memo[i % mv] = max(memo[i % mv], i // mv)

    print(sum(memo.values()))

