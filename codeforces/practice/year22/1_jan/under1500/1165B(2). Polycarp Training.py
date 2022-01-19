import heapq

n = int(input())
data = sorted(map(int, input().split()))

heapq.heapify(data)

cnt = 1
while data:
    now = heapq.heappop(data)
    if cnt <= now:
        cnt += 1

print(cnt - 1)