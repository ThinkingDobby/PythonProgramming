import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue
    hdata = data[:]
    heapq.heapify(hdata)

    memo = [0] * n
    for i in range(n):
        tmp = heapq.heappop(hdata)
        if tmp == data[i]:
            if i == n - 1 and len(hdata) == 0:
                memo[n - 1] = memo[n - 2]
                memo[n - 2] = tmp
            else:
                memo[i] = heapq.heappop(hdata)
                heapq.heappush(hdata, tmp)
        else:
            memo[i] = tmp

    print(*memo)