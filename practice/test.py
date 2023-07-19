N, T, M = map(int, input().split())
A, B = [], []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a - 1)
    B.append(b - 1)


def f(x, t, u):
    if x == N:
        if u != T:
            return 0
        ret = 1
        for i in range(M):
            ret &= t[A[i]] != t[B[i]]
    else:
        ret = 0
        for i in range(u + 1):
            t[x] = i
            ret += f(x + 1, t, max(u, i + 1))
    return ret


print(f(0, [-1] * N, 0))

