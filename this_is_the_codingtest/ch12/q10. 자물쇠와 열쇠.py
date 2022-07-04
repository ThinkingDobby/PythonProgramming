def trans(a, n):
    b = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(a[i][j])
        b.append(tmp[::-1])
    return b


def solution(key, lock):
    n = len(lock)
    m = len(key)

    ans = False
    for t in range(4):
        if t != 0:
            key = trans(key, m)
        for a in range(-n + 1, n):
            for b in range(-n + 1, n):
                flag = True
                for i in range(n):
                    for j in range(n):
                        if 0 <= i + a < min(n, m) and 0 <= j + b < min(n, m):
                            if lock[i][j] + key[i + a][j + b] != 1:
                                flag = False
                                break
                        else:
                            if lock[i][j] == 0:
                                flag = False
                                break
                    if not flag:
                        break
                if flag:
                    ans = True
                    break
            if ans:
                break
        if ans:
            break

    return ans


print(solution([[1, 1, 0], [0, 1, 1], [0, 0, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
