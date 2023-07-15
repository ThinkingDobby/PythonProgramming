import heapq

for _ in range(int(input())):
    n, m = map(int, input().split())

    dist = []
    heapq.heapify(dist)
    for i in range(n):
        for j in range(m):
            heapq.heappush(dist, max(i + j, i + m - 1 - j, n - 1 - i + j, n - 1 - i + m - 1 - j))

    print(*sorted(dist))