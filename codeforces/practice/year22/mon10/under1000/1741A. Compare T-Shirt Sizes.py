import sys

input = sys.stdin.readline


def check(size):
    if size[-1] == "M":
        return 10000
    elif size[-1] == "S":
        return 1000 - len(size)
    else:
        return 100000 + len(size)


for _ in range(int(input())):
    a, b = input().rstrip().split()

    ca = check(a)
    cb = check(b)

    if ca == cb:
        print("=")
    elif ca > cb:
        print(">")
    else:
        print("<")
