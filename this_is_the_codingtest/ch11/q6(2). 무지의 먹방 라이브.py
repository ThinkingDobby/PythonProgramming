import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    s = 0
    prev = 0
    l = len(food_times)

    while s + l * (q[0][0] - prev) <= k:
        now = heapq.heappop(q)[0]
        s += l * (now - prev)
        l -= 1
        prev = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - s) % l][1]


while True:
    print(solution([4, 3, 2], int(input())))
