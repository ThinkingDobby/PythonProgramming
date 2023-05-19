import collections
import sys

input = sys.stdin.readline

data = collections.deque(input().rstrip())
memo = set()

for i in range(len(data)):
    data.appendleft(data.pop())
    memo.add(''.join(data))

print(len(memo))

