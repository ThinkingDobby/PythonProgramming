import sys

sys.stdin = open("input.txt", "r")

dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]


def solve():
    result = ""

    for t in range(int(input())):
        n = int(input())
        data = [list(map(int, input().split())) for _ in range(n)]

        ans = -1
        for i in range(n):
            for j in range(n):
                for start_way in range(4):  # 각 점에서의 시작 방향

                    for w in range(1, (n + 1) // 2 + 1):    # 0, 2번째 변 길이
                        for h in range(1, (n + 1) // 2 + 1):    # 1, 3번째 변 길이
                            visited = [False] * 101
                            flag = True
                            visited[data[i][j]] = True

                            ni = i
                            nj = j

                            for way in range(4):    # way: 순서
                                now_way = (start_way + way) % 4 # 실제 방향

                                if way == 0 or way == 2:
                                    for step in range(w):
                                        ni += dirs[now_way][0]
                                        nj += dirs[now_way][1]
                                        if not (0 <= ni < n and 0 <= nj < n) or visited[data[ni][nj]]:
                                            flag = False
                                            break
                                        else:
                                            visited[data[ni][nj]] = True

                                    if not flag: break

                                elif way == 1 or way == 3:
                                    for step in range(h):
                                        ni += dirs[now_way][0]
                                        nj += dirs[now_way][1]
                                        if not (0 <= ni < n and 0 <= nj < n) or (not (way == 3 and step == h - 1) and visited[data[ni][nj]]):
                                            flag = False
                                            break
                                        else:
                                            visited[data[ni][nj]] = True

                                    if not flag: break

                            if flag:
                                ans = max(ans, visited.count(True))

        result += f"#{t + 1} {ans}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if result.rstrip() == output.rstrip():
    print("Correct")
else:
    print("Wrong")