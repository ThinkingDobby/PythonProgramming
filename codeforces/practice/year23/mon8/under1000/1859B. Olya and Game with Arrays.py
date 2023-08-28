import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    fms = []
    sms = []

    for _ in range(n):
        m = int(input())
        data = sorted(map(int, input().split()))

        fms.append(data[0])
        sms.append(data[1])

    sfms = sorted(fms)
    ssms = sorted(sms)
    print(sfms[0] + sum(ssms[1:]))
