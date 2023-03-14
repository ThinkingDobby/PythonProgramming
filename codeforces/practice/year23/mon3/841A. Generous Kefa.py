import collections
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = input().rstrip()

print("NO" if max(collections.Counter(data).values()) > k else "YES")