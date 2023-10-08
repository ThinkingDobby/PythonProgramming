import heapq
import sys

sys.stdin = open("sample_input.txt", "r")


dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def progress(heap, memo, w, h):
    while heap:
        p_time, p_x, i, j = heapq.heappop(heap)
        x, start = memo[i][j]

        if memo[i][j][0] == 0:
            continue

        for a, b in dirs:
            if 0 <= i + a < h and 0 <= j + b < w and memo[i + a][j + b][0] == 0:
                memo[i + a][j + b][0] = x
                memo[i + a][j + b][1] = p_time
                heapq.heappush(heap, [x + p_time + 1, -x, i + a, j + b])


def solve():
    result = ""

    for t in range(int(input())):
        n, m, k = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(n)]
        memo = [[[0, 0] for _ in range(m + k * 2)] for _ in range(n + k * 2)]

        heap = []
        for i in range(n):
            for j in range(m):
                memo[i + k][j + k][0] = data[i][j]  # 생명력, 생성 시간
                memo[i + k][j + k][1] = 0

                heapq.heappush(heap, [data[i][j] + 1, -data[i][j], i + k, j + k])   # 우선순위: 생성시간 + 생명력 + 1, -생명력

        for i in range(n):
            for j in range(m):
                progress(heap, memo, m + k * 2, n + k * 2)

        cnt = 0
        for i in range(n + k * 2):
            for j in range(m + k * 2):
                # print(f"{memo[i][j][1]:02}", end=' ')
                if memo[i][j][1] <= k <= memo[i][j][0] * 2 + memo[i][j][1] - 1:
                    cnt += 1
            # print()

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