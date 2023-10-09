import collections
import sys

sys.stdin = open("sample_input.txt", "r")

dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def check_crash(points, i, j):
    xi = points[i][0]
    yi = points[i][1]
    xj = points[j][0]
    yj = points[j][1]
    di = points[i][2]
    dj = points[j][2]
    
    # x가 같고 방향이 상/하인 경우
    if xi == xj:
        if yi > yj and di == 1 and dj == 0: return abs(yi - yj)
        elif yi < yj and di == 0 and dj == 1: return abs(yi - yj)
    # y가 같고 방향이 좌/우인 경우
    elif yi == yj:
        if xi > xj and di == 2 and dj == 3: return abs(xi - xj)
        elif xi < xj and di == 3 and dj == 2: return abs(xi - xj)
    
    elif abs(xi - xj) == abs(yi - yj):
        if xi > xj: # i의 x가 클 때
            if yi > yj: # i의 y가 클 때
                if (di == 2 and dj == 0) or (di == 1 and dj == 3): return abs(xi - xj) * 2
            elif yi < yj:   # i의 y가 작을 때
                if (di == 0 and dj == 3) or (di == 2 and dj == 1): return abs(xi - xj) * 2
        elif xi < xj:   # i의 x가 작을 때
            if yi > yj: # i의 y가 클 때
                if (di == 3 and dj == 0) or (di == 1 and dj == 2): return abs(xi - xj) * 2
            elif yi < yj:   # i의 y가 작을 때
                if (di == 0 and dj == 2) or (di == 3 and dj == 1): return abs(xi - xj) * 2


def solve():
    result = ""

    for t in range(int(input())):
        n = int(input())
        points = [list(map(int, input().split())) for _ in range(n)]

        crash = collections.defaultdict(list)
        crashed = [False] * n

        for i in range(n - 1):
            for j in range(i + 1, n):
                second = check_crash(points, i, j)
                if second:
                    crash[second].append([i, j])

        cnt = 0
        for second in sorted(crash):
            memo = set()
            for i, j in crash[second]:
                if not crashed[i] and not crashed[j]:
                    memo.add(i)
                    memo.add(j)

            for i in memo:
                # print(second, i)
                crashed[i] = True
                cnt += points[i][3]

        result += f"#{t + 1} {cnt}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if result.rstrip() == output.rstrip():
    print("Correct")
else:
    print("Wrong")


"""
1
14
-6 5 3 1
-3 5 2 1
-5 2 1 1
3 5 3 1
5 7 1 1
6 7 3 1
7 5 2 1
5 3 0 1
-4 -4 1 1
-4 -6 0 1
5 -3 2 1
4 -6 0 1
6 -4 1 1
9 -7 2 1
"""