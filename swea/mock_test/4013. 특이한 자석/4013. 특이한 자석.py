import sys

sys.stdin = open("sample_input.txt", "r")


def check_adjacent(data, num, typ, start):  # typ 0: 왼쪽 확인, 1: 오른쪽 확인
    if typ == 0:
        return data[num - 1][(start[num - 1] + 2) % 8] != data[num][(start[num] + 6) % 8]
    else:
        return data[num + 1][(start[num + 1] + 6) % 8] != data[num][(start[num] + 2) % 8]


# 실제 회전
def rotate(num, way, start):
    if way == -1:
        start[num] = (start[num] + 1) % 8
    else:
        start[num] = (start[num] - 1) % 8


def get_score(data, start):
    cnt = 0
    for i in range(4):
        cnt += data[i][start[i]] * 2**i
    # print(start)

    return cnt


def check(data, num, way, start):
    memo = [False] * 4
    i = num - 1
    while i >= 0:
        memo[i] = check_adjacent(data, i + 1, 0, start)
        if not memo[i]:
            break
        i -= 1

    i = num + 1
    while i < 4:
        memo[i] = check_adjacent(data, i - 1, 1, start)
        if not memo[i]:
            break
        i += 1

    # 일괄 회전
    dirs = [way, -way]
    rotate(num, way, start)
    for i in range(4):
        if memo[i]:
            rotate(i, dirs[(num - i) % 2], start)


def solve():
    result = ""
    for t in range(int(input())):
        k = int(input())
        data = [list(map(int, input().split())) for _ in range(4)]

        start = [0] * 4

        for _ in range(k):
            num, way = map(int, input().split())
            check(data, num - 1, way, start)

        result += f"#{t + 1} {get_score(data, start)}\n"

    return result


result = solve()
print(result)

with open("sample_output.txt", "r") as file:
    output = file.read()

if output.rstrip() == result.rstrip():
    print("Correct")
else:
    print("Wrong")