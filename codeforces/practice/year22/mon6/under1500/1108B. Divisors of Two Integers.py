import collections
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

mfv = max(data)
memo = dict(collections.Counter(data))
f = [mfv // i for i in range(1, mfv + 1) if mfv % i == 0]

for i in f:
    memo[i] -= 1

msv = (max([i for i in memo.keys() if memo[i] != 0]))

print(mfv, msv)