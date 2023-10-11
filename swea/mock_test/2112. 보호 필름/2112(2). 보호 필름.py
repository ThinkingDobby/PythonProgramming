import math
import sys

sys.stdin = open("input.txt", "r")


def print_list(data):
    for i in data:
        for j in i:
            print(j, end=' ')
        print()
    print()


def copy_list(data):
    memo = [i[:] for i in data]
    return memo


def check(data, d, w, k, cnt, now, typ):
    if cnt > 0:
        data[now] = [typ] * w

    # print("cnt:", end='')
    # print(cnt, now, typ)
    # print_list(data)

    for j in range(w):
        cnts = [0, 0]
        cnts[data[0][j]] += 1

        row_check = False
        for i in range(1, d):
            if data[i - 1][j] == data[i][j]:
                cnts[data[i][j]] += 1
                if cnts[data[i][j]] >= k:
                    row_check = True
                    break
            else:
                cnts[data[i][j - 1]] = 0
                cnts[data[i][j]] = 1

        if not row_check:
            return False

    return True


def dfs(data, d, w, k, cnt, now, typ):
    if cnt > k:
        return k

    if check(data, d, w, k, cnt, now, typ):
        return cnt

    mv = math.inf
    for next in range(now + 1, d):
        first = dfs(copy_list(data), d, w, k, cnt + 1, next, 0)
        if first != -1: mv = min(mv, first)

        second = dfs(copy_list(data), d, w, k, cnt + 1, next, 1)
        if second != -1: mv = min(mv, second)

    return -1 if mv == math.inf else mv


def solve():
    result = ""

    for t in range(int(input())):
        d, w, k = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(d)]

        if check(data, d, w, k, 0, 0, -1) or k == 1:
            ans = 0
        else:
            ans = math.inf
            for now in range(d):
                first = dfs(copy_list(data), d, w, k, 1, now, 0)
                if first != -1:
                    ans = min(ans, first)
                second = dfs(copy_list(data), d, w, k, 1, now, 1)
                if second != -1:
                    ans = min(ans, second)

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