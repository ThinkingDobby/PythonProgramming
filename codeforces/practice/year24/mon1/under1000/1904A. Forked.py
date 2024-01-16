import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())

    chk_k = set()
    chk_q = set()

    chk_k.add((xk + a, yk + b))
    if yk - b >= 0: chk_k.add((xk + a, yk - b))
    if xk - a >= 0: chk_k.add((xk - a, yk + b))
    if xk - a >= 0 and yk - b >= 0: chk_k.add((xk - a, yk - b))

    chk_q.add((xq + a, yq + b))
    if yq - b >= 0: chk_q.add((xq + a, yq - b))
    if xq - a >= 0: chk_q.add((xq - a, yq + b))
    if xq - a >= 0 and yq - b >= 0: chk_q.add((xq - a, yq - b))

    print(len(chk_k & chk_q))
    print(chk_k, chk_q)