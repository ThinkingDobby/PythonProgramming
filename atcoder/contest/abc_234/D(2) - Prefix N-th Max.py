import heapq

n, k = map(int, input().split())
data = list(map(int, input().split()))

q = data[:k]
heapq.heapify(q)
print(q[0])

for i in range(k, n):
    heapq.heappush(q, data[i])
    heapq.heappop(q)
    print(q[0])