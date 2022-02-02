import collections

n = int(input())

indegree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
cost = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

q = collections.deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

tmp = cost[:]
while q:
    now = q.popleft()
    for i in graph[now]:
        tmp[i] = max(tmp[i], cost[i] + tmp[now])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in tmp[1:]:
    print(i)


"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""