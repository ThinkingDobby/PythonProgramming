# 01:20 소요

import collections
import heapq
import sys

input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def adjacent_search(memo, i, j, like):
    like_cnt = empty_cnt = 0

    n = len(memo)
    for r, c in dirs:
        ni = i + r
        nj = j + c
        if 0 <= ni < n and 0 <= nj < n:
            if memo[ni][nj] == 0:
                empty_cnt += 1
            elif memo[ni][nj] in like:
                like_cnt += 1

    return like_cnt, empty_cnt


def whole_search(memo):
    mv = -1
    mi = mj = -1
    n = len(memo)
    for i in range(n):
        for j in range(n):
            if memo[i][j] == 0:
                result = adjacent_search(memo, i, j, [])[1]
                if result > mv:
                    mv = result
                    mi = i
                    mj = j

    return mi, mj


n = int(input())
student = [[] for _ in range(n * n + 1)]
order = []
for _ in range(1, n * n + 1):
    data = list(map(int, input().split()))
    order.append(data[0])   # 순서대로
    student[data[0]] = data[1:] # 번호, 좋아하는 학생 리스트

memo = [[0] * n for _ in range(n)]  # 실제 이차원 배열
entered = collections.defaultdict(tuple)    # 번호, 저장된 지점

memo[1][1] = order[0]
entered[order[0]] = (1, 1)

ans = 0
for i in range(1, n * n):
    # for k in memo:
    #     print(k)
    # print()

    now = order[i]
    heap = []    # 후보 위치 주변 친구 수, 빈칸 수 저장할 최대 힙
    for like_student in student[now]:
        if like_student in entered:   # 좋아하는 친구가 들어갔으면
            li, lj = entered[like_student]
            for r, c, in dirs:  # 그 친구 주변만 탐색
                ni = li + r
                nj = lj + c
                if 0 <= ni < n and 0 <= nj < n and memo[ni][nj] == 0:
                    result = adjacent_search(memo, ni, nj, student[now])
                    heapq.heappush(heap, (-result[0], -result[1], li + r, lj + c))
                    # print(li, lj, ni, nj, heap)

    if heap:
        result = heapq.heappop(heap)
        ri = result[2]
        rj = result[3]
    else:
        ri, rj = whole_search(memo)

    memo[ri][rj] = now
    entered[now] = (ri, rj)

for i in range(n):
    for j in range(n):
        result = adjacent_search(memo, i, j, student[memo[i][j]])
        if result[0] > 0:
            ans += 10**(result[0] - 1)

print(ans)
