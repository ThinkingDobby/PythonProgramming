import math
import sys

sys.stdin = open("sample_input.txt", "r")


def copy(data, w):
    new = [data[i][:] for i in range(w)]

    return new


def pop(data, x, y, w, h):
    v = data[x][y]

    for i in range(x - v + 1, x + v):
        if 0 <= i < w:
            if data[i][y] > 1 and i != x:
                pop(data, i, y, w, h)
            data[i][y] = 0

    for i in range(y - v + 1, y + v):
        if 0 <= i < h:
            if data[x][i] > 1 and i != y:
                pop(data, x, i, w, h)
            data[x][i] = 0


def rearrange(data, h):
    new = []
    for i in range(len(data)):
        tmp = list(map(int, ''.join(map(str, data[i])).replace("0", "")))
        new.append([0] * (h - len(tmp)) + tmp)

    return new


def shot(data, w, h, cnt):
    mv = math.inf

    if cnt == 0:
        now = 0
        for i in range(w):
            now += data[i].count(0)
        return w * h - now

    for i in range(w):
        for j in range(h):
            if data[i][j] != 0:
                new = copy(data, w)
                pop(new, i, j, w, h)
                new = rearrange(new, h)
                mv = min(shot(new, w, h, cnt - 1), mv)
                break

    return mv if mv != math.inf else 0


def solve():
    result = ""

    for t in range(int(input())):
        n, w, h = map(int, input().split())
        data = [list(map(int, input().split())) for _ in range(h)]
        data = [[data[j][i] for j in range(h)] for i in range(w)]

        result += f"#{t + 1} {shot(data, w, h, n)}\n"

    return result


result = solve()
print(result)


with open("sample_output.txt", "r") as file:
    output = file.read()

if output.rstrip() == result.rstrip():
    print("Correct")
else:
    print("Wrong")