import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    data = list(map(int, input().split()))

    max_heap = []

    ans = 0
    for i in range(n):
        if data[i] == 0:
            if max_heap:
                ans += heapq.heappop(max_heap)[1]
        else:
            heapq.heappush(max_heap, (-data[i], data[i]))

    print(ans)