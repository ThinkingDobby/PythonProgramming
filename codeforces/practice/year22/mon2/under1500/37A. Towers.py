import collections

n = int(input())

data = list(map(int, input().split()))
memo = dict(collections.Counter(data))
print(max(memo.values()), len(memo.keys()))