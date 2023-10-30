import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = input().rstrip()

if data[-1] == '#':
    print("NO")
else:
    tmp = map(lambda x: len(x), data.split('.'))
    print("NO" if max(tmp) >= k else "YES")