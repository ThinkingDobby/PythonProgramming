import collections
import sys

input = sys.stdin.readline

n = int(input())
data = list(input().rstrip())
print("Yes" if max(collections.Counter(data).values()) > 1 or n == 1 else "NO")
