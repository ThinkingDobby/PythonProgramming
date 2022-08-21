import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    dq = collections.deque()
    for i in data:
        if dq:
            if i == 'A':
                dq.append(i)
            else:
                dq.pop()
        else:
            dq.append(i)

    print(len(dq))
