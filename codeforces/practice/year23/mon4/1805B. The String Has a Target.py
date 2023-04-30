import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    sd = sorted(data)

    f = -1
    s = -1
    for i in range(n - 1, -1, -1):
        if f == -1 and data[i] == sd[0]:
            f = i
        if s == -1 and n > 1 and data[i] == sd[1]:
            s = i

    fa = data[f] + data[:f] + data[f + 1:]
    if s != -1:
        fa = min(fa, data[s] + data[:s] + data[s + 1:])

    print(fa)

