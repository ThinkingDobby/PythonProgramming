import collections
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

cnts = dict(collections.Counter(data))

if any([True if cnts[i] > 2 else False for i in cnts if i != 0]):
    print(-1)
else:
    print(len([1 for i in cnts if i != 0 and cnts[i] == 2]))