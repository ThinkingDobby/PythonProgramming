import sys

sys.stdin = open("sample_input.txt", "r")


def count_house(data, n, a, b, k):
    cnt = 0

    tmp = 1
    for i in range(a - k + 1, a + k):
        if tmp > k:
            ntmp = k * 2 - tmp
        else:
            ntmp = tmp
        for j in range(b - ntmp + 1, b + ntmp):
            if 0 <= i < n and 0 <= j < n and data[i][j] == 1:
                cnt += 1
        tmp += 1

    return cnt


def solve():
    result = ""
    for t in range(int(input())):
        n, m = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(n)]

        mv = 1
        for i in range(n):
            for j in range(n):
                for k in range(1, n + 2):
                    cost = k * k + (k - 1) * (k - 1)
                    cnt = count_house(data, n, i, j, k)
                    limit = m * cnt

                    if limit >= cost and mv < cnt:
                        # print(i, j, k, cnt, cost, limit)
                        mv = cnt

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