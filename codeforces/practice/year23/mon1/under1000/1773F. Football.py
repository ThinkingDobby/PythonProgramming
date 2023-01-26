import sys

input = sys.stdin.readline

n = int(input())
a = int(input())
b = int(input())

if n == 1:
    print(1 if a == b else 0)
    print("%d:%d" % (a, b))
elif n <= a + b:
    print(0)
    if a >= n:
        if b != 0:
            for _ in range(n - 2):
                print("1:0")
            print("%d:0" % (a - (n - 2)))
            print("0:%d" % (b))
        else:
            for _ in range(n - 1):
                print("1:0")
            print("%d:0" % (a - (n - 1)))
    else:
        for _ in range(a):
            print("1:0")
        for _ in range(n - a - 1):
            print("0:1")
        print("0:%d" % (b - (n - a - 1)))
else:
    print(n - (a + b))
    for _ in range(a):
        print("1:0")
    for _ in range(b):
        print("0:1")
    for _ in range(n - (a + b)):
        print("0:0")
