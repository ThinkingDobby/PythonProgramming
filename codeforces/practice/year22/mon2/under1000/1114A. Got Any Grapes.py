import sys

input = sys.stdin.readline

x, y, z = map(int, input().split())
g, p, b = map(int, input().split())

if g >= x:
    if g - x + p >= y:
        if g - x + p - y + b >= z:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")