import collections


def solution(p):
    if check(p):
        return p

    return func(p)


def func(data):
    if data == '':
        return data

    f = 1 if data[0] == ')' else 0
    s = 1 if data[0] == '(' else 0
    idx = 1
    for i in range(1, len(data)):
        if data[i] == ')':
            f += 1
        else:
            s += 1
        if f == s:
            idx = i
            break

    u = data[:idx + 1]
    v = data[idx + 1:]
    if check(u):
        return u + func(v)
    else:
        return '(' + func(v) + ')' + ''.join(map(lambda x: '(' if x == ')' else ')', u[1:-1]))


def check(data):
    q = collections.deque()
    for i in data:
        if i == ')':
            if q:
                q.popleft()
            else:
                return False
        else:
            q.append('(')

    return len(q) == 0
