import sys

sys.stdin = open("sample_input.txt", "r")


def check_row(row, n, x):
    cnt = 1
    for i in range(1, n):
        if row[i - 1] == row[i]:
            cnt += 1
        elif row[i - 1] + 1 == row[i] and cnt >= x:
            cnt = 1
        elif row[i - 1] == row[i] + 1 and cnt >= 0:
            cnt = 1 - x
        else:
            return 0
    return cnt >= 0


def solve():
    result = ""

    for t in range(int(input())):
        n, x = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(n)]

        ans = 0
        for i in range(n):
            ans += check_row(data[i], n, x)

        for j in range(n):
            tmp = []
            for i in range(n):
                tmp.append(data[i][j])
            ans += check_row(tmp, n, x)

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