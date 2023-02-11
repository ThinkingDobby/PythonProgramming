import collections
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = collections.Counter(map(int, input().split()))
tmp = (max(data.values()) + k - 1) // k
print(sum([tmp * k - i for i in data.values()]))