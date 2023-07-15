# 참조한 코드
from collections import deque

n = int(input())
data = input()

dq = deque([n])

for i in range(n)[::-1]:
    if data[i] == 'R':
        dq.appendleft(i)
    else:
        dq.append(i)

print(*dq)