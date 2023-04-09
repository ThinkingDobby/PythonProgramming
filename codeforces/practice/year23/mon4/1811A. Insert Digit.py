import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, d = map(int, input().split())
    data = input().rstrip()

    chk = False
    for i in range(n):
        if d > int(data[i]):
            data = data[:i] + str(d) + data[i:]
            chk = True
            break

    if not chk:
        data = data + str(d)
    print(data)
