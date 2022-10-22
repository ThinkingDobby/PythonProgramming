import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int, input().split())
    data = list(map(int, input().split()))

    sv = sum(data)
    evens = [i for i in data if i % 2 == 0]
    ecnt = len(evens)
    ocnt = n - ecnt

    for i in range(q):
        t, v = map(int, input().split())
        if t % 2 == 0:
            sv += ecnt * v
        else:
            sv += ocnt * v

        if t == 1 and v % 2 == 1:
            ecnt += ocnt
            ocnt = 0
        elif t == 0 and v % 2 == 1:
            ocnt += ecnt
            ecnt = 0

        print(sv)
