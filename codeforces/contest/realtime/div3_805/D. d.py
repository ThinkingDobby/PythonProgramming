import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    w = input().rstrip()
    p = int(input())

    memo = [ord(i) - 96 for i in w]
    s = sum(memo)

    cnts = dict(collections.Counter(memo))
    scnts = sorted(list(cnts.items()), reverse=True)
    tmp = s - p
    # print(cnts)
    # print(scnts)

    for i in scnts:
        if tmp - i[0] * i[1] <= 0:
            cnts[i[0]] -= ((tmp + i[0] - 1) // i[0])
            break
        else:
            tmp -= i[0] * i[1]
            cnts[i[0]] = 0

    for i in memo:
        if cnts[i]:
            print(chr(i + 96), end='')
            cnts[i] -= 1

    print()



