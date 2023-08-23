ways = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def search(i, j, w, h, maps):
    s = int(maps[i][j])
    maps[i][j] = 'X'

    for x, y in ways:
        if 0 <= i + y < h and 0 <= j + x < w and maps[i + y][j + x] != 'X':
            s += search(i + y, j + x, w, h, maps)

    return s


def solution(maps):
    w = len(maps[0])
    h = len(maps)

    for i in range(h):
        maps[i] = list(maps[i])

    ans = []
    for i in range(h):
        for j in range(w):
            if maps[i][j] != 'X':
                ans.append(search(i, j, w, h, maps))

    if not ans:
        return [-1]
    else:
        return sorted(ans)


maps = ["123123", "123123"]
ans = solution(maps)
print(ans)