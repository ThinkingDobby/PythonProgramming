from collections import deque

n, k = map(int, input().split())
data = list(map(int, input().split()))

q = deque()
for i in data:
    if i in q:
        continue
    else:
        if len(q) == k:
            q.popleft()
        q.append(i)

print(len(q))
while q:
    print(q.pop(), end=' ')