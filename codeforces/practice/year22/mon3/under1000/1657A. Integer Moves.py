import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    tmp = x**2 + y**2
    if x == 0 and y == 0:
        print(0)
    elif int(math.sqrt(tmp))**2 == tmp:
        print(1)
    else:
        print(2)