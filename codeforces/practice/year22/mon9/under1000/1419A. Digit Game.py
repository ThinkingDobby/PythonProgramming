import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, list(input().rstrip())))

    oc = False
    ec = False

    for i in range(n):
        if i % 2 == 0 and data[i] % 2 == 1:
            oc = True
        if i % 2 == 1 and data[i] % 2 == 0:
            ec = True

    if n % 2 == 1:
        print(1 if oc else 2)
    else:
        print(2 if ec else 1)