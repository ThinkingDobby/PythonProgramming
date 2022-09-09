import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    chk1 = False
    chk2 = False
    idxs = []

    now = data[0]
    nidx = 0
    for i in range(1, n):
        if not chk1:
            if data[i] > now:
                idxs.append(nidx)
                chk1 = True
            now = data[i]
            nidx = i
        elif chk1:
            if data[i] > now:
                now = data[i]
                nidx = i
            else:
                idxs.append(i)
                chk2 = True
                break

    if chk2:
        print("YES")
        print(idxs[0] + 1, nidx + 1, idxs[1] + 1)
    else:
        print("NO")

