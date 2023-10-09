import sys

sys.stdin = open("sample_input.txt", "r")


def progress(data, n, x):
    ans = 0

    for i in range(n):
        chk = True
        visited = [False] * n
        for j in range(1, n):
            if data[i][j - 1] < data[i][j]:
                cnt = 0
                for k in range(max(0, j - x), j):
                    if data[i][k] != data[i][j] - 1:
                        chk = False
                        break
                    else:
                        visited[k] = True
                        cnt += 1
                if cnt < x:
                    chk = False

        if chk:
            for j in range(n - 1):
                if data[i][j] > data[i][j + 1]:
                    cnt = 0
                    for k in range(j + 1, min(n, j + x + 1)):
                        if visited[k]:
                            chk = False
                            break

                        if data[i][k] != data[i][j] - 1:
                            chk = False
                            break
                        else:
                            cnt += 1
                    if cnt < x:
                        chk = False

        if chk:
            ans += 1

    return ans


def solve():
    result = ""

    for t in range(int(input())):
        n, x = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(n)]
        rdata = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rdata[i][j] = data[j][i]

        ans = progress(data, n, x) + progress(rdata, n, x)

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