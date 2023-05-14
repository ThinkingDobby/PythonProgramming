import collections
import sys

input = sys.stdin.readline

n = int(input())
data = list(input().rstrip())

f = collections.deque()
s = collections.deque()

chk = True
for i in range(n - 1, -1, -1):
    if chk:
        s.appendleft(data[i])
    else:
        f.append(data[i])

    chk = not chk

print(''.join(f + s))
