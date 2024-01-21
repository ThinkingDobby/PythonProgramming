import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())

    chk_k = set()
    chk_q = set()

    chk_k.add((xk + a, yk + b))
    chk_k.add((xk + a, yk - b))
    chk_k.add((xk - a, yk + b))
    chk_k.add((xk - a, yk - b))

    chk_k.add((xk + b, yk + a))
    chk_k.add((xk + b, yk - a))
    chk_k.add((xk - b, yk + a))
    chk_k.add((xk - b, yk - a))

    chk_q.add((xq + a, yq + b))
    chk_q.add((xq + a, yq - b))
    chk_q.add((xq - a, yq + b))
    chk_q.add((xq - a, yq - b))

    chk_q.add((xq + b, yq + a))
    chk_q.add((xq + b, yq - a))
    chk_q.add((xq - b, yq + a))
    chk_q.add((xq - b, yq - a))

    print(len(chk_k & chk_q))