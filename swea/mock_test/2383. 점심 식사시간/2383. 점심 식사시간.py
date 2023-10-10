import heapq
import itertools
import math
import sys

sys.stdin = open("sample_input.txt", "r")


def calc(ap, da, db, sa, sb):    # a로 가는 사람들, a까지 거리, b까지 거리, a 시간, b 시간
    sda = sorted(da)
    sdb = sorted(db)

    abuf = []
    bbuf = []

    for i in sda:
        if i[1] in ap:
            if len(abuf) < 3:   # 3명까지는 지연 없이 내려감
                heapq.heappush(abuf, i[0] + sa)
            else:
                tmp = heapq.heappop(abuf)   # 3명 중 가장 빨리 내려가는 경우의 완료 시간
                if tmp < i[0]:  # 완료 시간 이후에 계단 도착 시 딜레이 없음
                    heapq.heappush(abuf, i[0] + sa)
                else:   # 완료 시간 전에 계단 도착 시, 완료 후 내려감
                    heapq.heappush(abuf, tmp + sa)

    for i in sdb:
        if i[1] not in ap:
            if len(bbuf) < 3:
                heapq.heappush(bbuf, i[0] + sb)
            else:
                tmp = heapq.heappop(bbuf)
                if tmp < i[0]:
                    heapq.heappush(bbuf, i[0] + sb)
                else:
                    heapq.heappush(bbuf, tmp + sb)

    return max(abuf + bbuf) + 1


def solve():
    result = ""
    for t in range(int(input())):
        n = int(input())
        data = [list(map(int, input().split())) for _ in range(n)]

        p = []
        s = []
        for i in range(n):
            for j in range(n):
                if data[i][j] == 1:
                    p.append([i, j])
                elif data[i][j] != 0:
                    s.append([i, j])

        da = [[0, 0] for _ in range(len(p))]
        db = [[0, 0] for _ in range(len(p))]
        for i in range(len(p)):
            da[i][0] = abs(p[i][0] - s[0][0]) + abs(p[i][1] - s[0][1])
            da[i][1] = i

            db[i][0] = abs(p[i][0] - s[1][0]) + abs(p[i][1] - s[1][1])
            db[i][1] = i

        mv = math.inf
        for i in range(len(p) + 1):
            tmp = list(itertools.combinations(range(len(p) + 1), i))    # 두 그룹으로 나뉘는 모든 경우
            for check in tmp:
                mv = min(mv, calc(set(check), da, db, data[s[0][0]][s[0][1]], data[s[1][0]][s[1][1]]))

        result += f"#{t + 1} {mv}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if output.rstrip() == result.rstrip():
    print("Correct")
else:
    print("Wrong")