import collections

n, m = map(int, input().split())
data = list(enumerate(map(int, input().split())))
q = collections.deque(data)

while q:
    now = q.popleft()
    if not q:
        print(now[0] + 1)
        break
    if now[1] > m:
        q.append((now[0], now[1] - m))
