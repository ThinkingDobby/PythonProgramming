import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = collections.Counter(map(int, input().split()))

print(min(data.values()) if len(set(data.keys())) == n else 0)