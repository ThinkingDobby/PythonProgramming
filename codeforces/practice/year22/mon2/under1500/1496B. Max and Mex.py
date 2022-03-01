import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = sorted(map(int, input().split()))

    mv = max(data)
    mex = mv + 1

    for i in range(n):
        if data[i] != i:
            mex = i
            break

    if mex == mv + 1:
        print(mex + k)
    else:
        tmp = (mv + mex) // 2
        if tmp * 2 != mv + mex:
            tmp += 1

        if k >= 1:
            print(n + (1 if tmp not in data else 0))
        else:
            print(n)